'''
Created on 2020. 5. 11.

@author: KITCOOP
'''
# -*- coding: utf-8 -*- 

###########################################################################
# # Python code generated with wxFormBuilder (version Jun 17 2015)
# # http://www.wxformbuilder.org/
# #
# # PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx

###########################################################################
# # Class MyCalc
###########################################################################


class MyCalc (wx.Frame):
    
    def __init__(self, parent):
        wx.Frame.__init__ (self, parent, id=wx.ID_ANY, title=u"간단한 계산기", pos=wx.DefaultPosition, size=wx.Size(316, 445), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)
        
        # self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)
        self.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_MENU))
        
        bSizer6 = wx.BoxSizer(wx.VERTICAL)
        
        self.m_panel4 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer7 = wx.BoxSizer(wx.HORIZONTAL)
        
        self.m_staticText5 = wx.StaticText(self.m_panel4, wx.ID_ANY, u"숫자1 : ", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText5.Wrap(-1)
        bSizer7.Add(self.m_staticText5, 0, wx.ALL, 5)
        
        self.textNum1 = wx.TextCtrl(self.m_panel4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer7.Add(self.textNum1, 0, wx.ALL, 5)
        
        self.m_panel4.SetSizer(bSizer7)
        self.m_panel4.Layout()
        bSizer7.Fit(self.m_panel4)
        bSizer6.Add(self.m_panel4, 0, wx.EXPAND | wx.ALL, 5)
        
        self.m_panel5 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer8 = wx.BoxSizer(wx.HORIZONTAL)
        
        self.m_staticText6 = wx.StaticText(self.m_panel5, wx.ID_ANY, u"숫자2 :", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText6.Wrap(-1)
        bSizer8.Add(self.m_staticText6, 0, wx.ALL, 5)
        
        self.textNum2 = wx.TextCtrl(self.m_panel5, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer8.Add(self.textNum2, 0, wx.ALL, 5)
        
        self.m_panel5.SetSizer(bSizer8)
        self.m_panel5.Layout()
        bSizer8.Fit(self.m_panel5)
        bSizer6.Add(self.m_panel5, 0, wx.ALL | wx.EXPAND, 5)
        
        self.m_panel6 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer9 = wx.BoxSizer(wx.HORIZONTAL)
        
        rdoOpChoices = [ u"+", u"-", u"*", u"/" ]
        self.rdoOp = wx.RadioBox(self.m_panel6, wx.ID_ANY, u"연산자 선택", wx.DefaultPosition, wx.DefaultSize, rdoOpChoices, 1, wx.RA_SPECIFY_ROWS)
        self.rdoOp.SetSelection(0)
        bSizer9.Add(self.rdoOp, 0, wx.ALL, 5)
        
        self.m_panel6.SetSizer(bSizer9)
        self.m_panel6.Layout()
        bSizer9.Fit(self.m_panel6)
        bSizer6.Add(self.m_panel6, 0, wx.EXPAND | wx.ALL, 5)
        
        self.m_panel7 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer10 = wx.BoxSizer(wx.HORIZONTAL)
        
        self.m_staticText8 = wx.StaticText(self.m_panel7, wx.ID_ANY, u"연산결과", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText8.Wrap(-1)
        bSizer10.Add(self.m_staticText8, 0, wx.ALL, 5)
        
        self.wxResult = wx.StaticText(self.m_panel7, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.wxResult.Wrap(-1)
        bSizer10.Add(self.wxResult, 0, wx.ALL, 5)
        
        self.m_panel7.SetSizer(bSizer10)
        self.m_panel7.Layout()
        bSizer10.Fit(self.m_panel7)
        bSizer6.Add(self.m_panel7, 1, wx.EXPAND | wx.ALL, 5)
        
        self.m_panel8 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer11 = wx.BoxSizer(wx.HORIZONTAL)
        
        self.btnCalc = wx.Button(self.m_panel8, wx.ID_ANY, u"계산", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer11.Add(self.btnCalc, 0, wx.ALL, 5)
        
        self.btnClear = wx.Button(self.m_panel8, wx.ID_ANY, u"초기화", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer11.Add(self.btnClear, 0, wx.ALL, 5)
        
        self.btnExit = wx.Button(self.m_panel8, wx.ID_ANY, u"종료", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer11.Add(self.btnExit, 0, wx.ALL, 5)
        
        self.m_panel8.SetSizer(bSizer11)
        self.m_panel8.Layout()
        bSizer11.Fit(self.m_panel8)
        bSizer6.Add(self.m_panel8, 0, wx.EXPAND | wx.ALL, 5)
        
        self.SetSizer(bSizer6)
        self.Layout()
        
        self.Centre(wx.BOTH)
    
        self.btnCalc.id = 1  # id는 원하는 것을 주면 된다.
        self.btnClear.id = 2
        self.btnExit.id = 3
        
        self.btnCalc.Bind(wx.EVT_BUTTON, self.OnProcess)
        self.btnClear.Bind(wx.EVT_BUTTON, self.OnProcess)
        self.btnExit.Bind(wx.EVT_BUTTON, self.OnProcess)

#         
    def __del__(self):
        pass

    def input_check(self, txt1, txt2):
                
        try:
            txt1 = float(self.textNum1.GetValue())
            txt2 = float(self.textNum2.GetValue())
            return 1            
        except:
            msgDial = wx.MessageBox('실수 혹은 정수를 입력해 주세요', '경.고.', wx.OK)
            return 0

    def OnProcess(self, event):
        # 버튼 id 받기
        bid = event.GetEventObject().id
        
        # 1번 계산 버튼을 눌렀을 시  
        if bid == 1:
            
            # operation 가져오기       
            cop = self.rdoOp.GetStringSelection()
            
            # 텍스트박스의 값 가져오기
            txt1 = self.textNum1.GetValue()
            txt2 = self.textNum2.GetValue()
            
            # 입력자료 오류검사 잘되었으면 1 나쁘면 0   
            flag = self.input_check(txt1, txt2)
            
            # 잘 되었으면 float 형으로 변경 안되었으면 공백으로 바꾸고 리턴
            if(flag == 1):
                txt1 = float(self.textNum1.GetValue())
                txt2 = float(self.textNum2.GetValue())
            else:
                self.textNum1.SetLabelText('')
                self.textNum2.SetLabelText('')
                return  
            
            # 연사자 별 연산
            if(cop == '+'):
                result = txt1 + txt2
                self.wxResult.SetLabelText(str(result))
            elif(cop == '-'):
                result = txt1 - txt2
                self.wxResult.SetLabelText(str(result))
            elif(cop == '*'):
                result = txt1 * txt2
                self.wxResult.SetLabelText(str(result))
            elif(cop == '/'):
                
                # divide by zero 방지
                if(txt2 == 0):
                    msgDial = wx.MessageBox('0으로 나눌 수는 없습니다', '경.고.', wx.OK)
                    self.textNum1.SetLabelText('')
                    self.textNum2.SetLabelText('')
                    return
                else:
                    result = txt1 / txt2
                    self.wxResult.SetLabelText(str(result))
        
        # 초기화 버튼 실행
        elif bid == 2:
            
            # 텍스트 자리 비우고
            self.textNum1.SetLabelText('')
            self.textNum2.SetLabelText('')
            
            # 결과 자리 비우고
            self.wxResult.SetLabelText('')
            
            # 라디오 버튼 +로 가게
            self.rdoOp.SetSelection(0)
            
        elif bid == 3:
            
            # 종료의사 묻기
            msgDial = wx.MessageBox('종료하시겠습니까?', '궁금', wx.YES_NO)
            
            # 예 : 2 아니오 :8
            if(msgDial == 2):
                self.Close()
            else:
                return  

        
if __name__ == '__main__':
    app = wx.App()
    MyCalc(None).Show()
    app.MainLoop()           

