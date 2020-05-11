import wx
import wx.xrc

class Mycalc ( wx.Frame ):
    
    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"간단계산기", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
        
        #self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        
        bSizer1 = wx.BoxSizer( wx.VERTICAL )
        
        self.m_panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        self.m_panel1.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
        
        bSizer2 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText4 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"숫자1", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText4.Wrap( -1 )
        bSizer2.Add( self.m_staticText4, 0, wx.ALL, 5 )
        
        self.txtNum1 = wx.TextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer2.Add( self.txtNum1, 0, wx.ALL, 5 )
        
        
        self.m_panel1.SetSizer( bSizer2 )
        self.m_panel1.Layout()
        bSizer2.Fit( self.m_panel1 )
        bSizer1.Add( self.m_panel1, 1, wx.EXPAND |wx.ALL, 5 )
        
        self.m_panel2 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        self.m_panel2.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTION ) )
        
        bSizer3 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText5 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"숫자2", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText5.Wrap( -1 )
        bSizer3.Add( self.m_staticText5, 0, wx.ALL, 5 )
        
        self.txtNum2 = wx.TextCtrl( self.m_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer3.Add( self.txtNum2, 0, wx.ALL, 5 )
        
        
        self.m_panel2.SetSizer( bSizer3 )
        self.m_panel2.Layout()
        bSizer3.Fit( self.m_panel2 )
        bSizer1.Add( self.m_panel2, 1, wx.EXPAND |wx.ALL, 5 )
        
        self.m_panel3 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        self.m_panel3.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )
        
        bSizer4 = wx.BoxSizer( wx.HORIZONTAL )
        
        rdoOpChoices = [ u"+", u"-", u"*", u"/" ]
        self.rdoOp = wx.RadioBox( self.m_panel3, wx.ID_ANY, u"연산자선택", wx.Point( 250,250 ), wx.Size( 500,-1 ), rdoOpChoices, 1, wx.RA_SPECIFY_ROWS )
        self.rdoOp.SetSelection( 0 )
        bSizer4.Add( self.rdoOp, 0, wx.ALL, 5 )
        
        
        self.m_panel3.SetSizer( bSizer4 )
        self.m_panel3.Layout()
        bSizer4.Fit( self.m_panel3 )
        bSizer1.Add( self.m_panel3, 1, wx.EXPAND |wx.ALL, 5 )
        
        self.m_panel4 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        self.m_panel4.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )
        
        bSizer5 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.wxStaticText6 = wx.StaticText( self.m_panel4, wx.ID_ANY, u"연산 결과", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.wxStaticText6.Wrap( -1 )
        bSizer5.Add( self.wxStaticText6, 0, wx.ALL, 5 )
        
        self.staResult = wx.StaticText( self.m_panel4, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.staResult.Wrap( -1 )
        bSizer5.Add( self.staResult, 0, wx.ALL, 5 )
        
        
        self.m_panel4.SetSizer( bSizer5 )
        self.m_panel4.Layout()
        bSizer5.Fit( self.m_panel4 )
        bSizer1.Add( self.m_panel4, 1, wx.EXPAND |wx.ALL, 5 )
        
        self.m_panel5 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        self.m_panel5.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_GRAYTEXT ) )
        
        bSizer6 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.btnCalc = wx.Button( self.m_panel5, wx.ID_ANY, u"계산", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer6.Add( self.btnCalc, 0, wx.ALL, 5 )
        
        self.btnClear = wx.Button( self.m_panel5, wx.ID_ANY, u"초기화", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer6.Add( self.btnClear, 0, wx.ALL, 5 )
        
        self.btnExit = wx.Button( self.m_panel5, wx.ID_ANY, u"종료", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer6.Add( self.btnExit, 0, wx.ALL, 5 )
        
        
        self.m_panel5.SetSizer( bSizer6 )
        self.m_panel5.Layout()
        bSizer6.Fit( self.m_panel5 )
        bSizer1.Add( self.m_panel5, 1, wx.EXPAND |wx.ALL, 5 )
        
        
        self.SetSizer( bSizer1 )
        self.Layout()
        
        self.Centre( wx.BOTH )
        
        # Connect Events
        self.btnCalc.Bind( wx.EVT_BUTTON, self.OnProcess )
        self.btnClear.Bind( wx.EVT_BUTTON, self.OnProcess )
        self.btnExit.Bind( wx.EVT_BUTTON, self.OnProcess )
        
        # 버튼에 id 주기
        self.btnCalc.id = 1
        self.btnClear.id = 2
        self.btnExit.id = 3
    
    def __del__( self ):
        pass
    
    #입력자료 검사 함수
    def input_check(self,txt1,txt2):
                
        try:
            txt1 = float(self.txtNum1.GetValue())
            txt2 = float(self.txtNum2.GetValue())
            return 1            
        except:
            msgDial = wx.MessageBox('실수 혹은 정수를 입력해 주세요','경.고.',wx.OK)
            return 0
    
            
    # 이벤트 핸들러
    def OnProcess( self, event ):
        
        # 버튼 id 받기
        bid = event.GetEventObject().id
        
        
        # 1번 계산 버튼을 눌렀을 시  
        if bid == 1:
            
            #operation 가져오기       
            cop = self.rdoOp.GetStringSelection()
            
            # 텍스트박스의 값 가져오기
            txt1 = self.txtNum1.GetValue()
            txt2 = self.txtNum2.GetValue()
            
            # 입력자료 오류검사 잘되었으면 1 나쁘면 0   
            flag = self.input_check(txt1,txt2)
            
            
            # 잘 되었으면 float 형으로 변경 안되었으면 공백으로 바꾸고 리턴
            if(flag == 1):
                txt1 = float(self.txtNum1.GetValue())
                txt2 = float(self.txtNum2.GetValue())
            else:
                self.txtNum1.SetLabelText('')
                self.txtNum2.SetLabelText('')
                return  
            
            # 연사자 별 연산
            if(cop == '+'):
                result = txt1 + txt2
                self.staResult.SetLabelText(str(result))
            elif(cop == '-'):
                result = txt1 - txt2
                self.staResult.SetLabelText(str(result))
            elif(cop == '*'):
                result = txt1 * txt2
                self.staResult.SetLabelText(str(result))
            elif(cop == '/'):
                
                # divide by zero 방지
                if(txt2 == 0):
                    msgDial = wx.MessageBox('0으로 나눌 수는 없습니다','경.고.',wx.OK)
                    self.txtNum1.SetLabelText('')
                    self.txtNum2.SetLabelText('')
                    return
                else:
                    result = txt1 / txt2
                    self.staResult.SetLabelText(str(result))
        
        
        # 초기화 버튼 실행
        elif bid == 2:
            
            # 텍스트 자리 비우고
            self.txtNum1.SetLabelText('')
            self.txtNum2.SetLabelText('')
            
            # 결과 자리 비우고
            self.staResult.SetLabelText('')
            
            #라디오 버튼 +로 가게
            self.rdoOp.SetSelection( 0 )
            
        elif bid == 3:
            
            # 종료의사 묻기
            msgDial = wx.MessageBox('종료하시겠습니까?','궁금',wx.YES_NO)
            
            # 예 : 2 아니오 :8
            if(msgDial == 2):
                self.Close()
            else:
                return  
    
if __name__ == '__main__':
    # 앱 생성자 콜
    app = wx.App()
    Mycalc(None).Show()
    app.MainLoop()
