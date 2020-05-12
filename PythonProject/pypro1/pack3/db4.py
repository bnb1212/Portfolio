# -*- coding: utf-8 -*- 

###########################################################################
# # Python code generated with wxFormBuilder (version Jun 17 2015)
# # http://www.wxformbuilder.org/
# #
# # PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
# # Class MyFrame2
###########################################################################

import MySQLdb
import sys
import locale

config = {  # dictionary 타입
    'host':'127.0.0.1',
    'user':'root',
    'password':'123',
    'database':'test',
    'port':3306,
    'charset':'utf8',
    'use_unicode':True
}


class MyFrame2 (wx.Frame):
    
    def __init__(self, parent):
        wx.Frame.__init__ (self, parent, id=wx.ID_ANY, title="작성자 : 이지운", pos=wx.DefaultPosition, size=wx.Size(525, 300), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)
        
#         self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        self.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_MENU))
        
        bSizer6 = wx.BoxSizer(wx.VERTICAL)
        
        self.m_panel5 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer9 = wx.BoxSizer(wx.VERTICAL)
        
        self.m_staticText5 = wx.StaticText(self.m_panel5, wx.ID_ANY, u"작성자 : 이지운", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText5.Wrap(-1)
        bSizer9.Add(self.m_staticText5, 0, wx.ALL, 5)
        
        self.m_panel5.SetSizer(bSizer9)
        self.m_panel5.Layout()
        bSizer9.Fit(self.m_panel5)
        bSizer6.Add(self.m_panel5, 0, wx.EXPAND | wx.ALL, 5)
        
        self.m_panel6 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer10 = wx.BoxSizer(wx.HORIZONTAL)
        
        self.labelName = wx.StaticText(self.m_panel6, wx.ID_ANY, u"상품명 :", wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelName.Wrap(-1)
        bSizer10.Add(self.labelName, 0, wx.ALL, 5)
        
        self.txtName = wx.TextCtrl(self.m_panel6, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(100, -1), 0)
        bSizer10.Add(self.txtName, 0, wx.ALL, 5)
        
        self.labelSu = wx.StaticText(self.m_panel6, wx.ID_ANY, u"수량 : ", wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelSu.Wrap(-1)
        bSizer10.Add(self.labelSu, 0, wx.ALL, 5)
        
        self.txtSu = wx.TextCtrl(self.m_panel6, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(50, -1), 0)
        bSizer10.Add(self.txtSu, 0, wx.ALL, 5)
        
        self.labelDan = wx.StaticText(self.m_panel6, wx.ID_ANY, u"단가 : ", wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelDan.Wrap(-1)
        bSizer10.Add(self.labelDan, 0, wx.ALL, 5)
        
        self.txtDan = wx.TextCtrl(self.m_panel6, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(80, -1), 0)
        bSizer10.Add(self.txtDan, 0, wx.ALL, 5)
        
        self.btnInsert = wx.Button(self.m_panel6, wx.ID_ANY, u"등록", wx.DefaultPosition, wx.Size(50, -1), 0)
        bSizer10.Add(self.btnInsert, 0, wx.ALL, 5)
        
        self.m_panel6.SetSizer(bSizer10)
        self.m_panel6.Layout()
        bSizer10.Fit(self.m_panel6)
        bSizer6.Add(self.m_panel6, 0, wx.EXPAND | wx.ALL, 5)
        
        self.m_panel7 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer11 = wx.BoxSizer(wx.VERTICAL)
        
        self.lstSang = wx.ListCtrl(self.m_panel7, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_REPORT)
        bSizer11.Add(self.lstSang, 1, wx.ALL | wx.EXPAND, 5)
        
        self.m_panel7.SetSizer(bSizer11)
        self.m_panel7.Layout()
        bSizer11.Fit(self.m_panel7)
        bSizer6.Add(self.m_panel7, 1, wx.EXPAND | wx.ALL, 5)
        
        self.m_panel8 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer12 = wx.BoxSizer(wx.HORIZONTAL)
        
        self.labelCount = wx.StaticText(self.m_panel8, wx.ID_ANY, u"건수 : 0", wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelCount.Wrap(-1)
        bSizer12.Add(self.labelCount, 0, wx.ALL, 5)
        
        self.m_panel8.SetSizer(bSizer12)
        self.m_panel8.Layout()
        bSizer12.Fit(self.m_panel8)
        bSizer6.Add(self.m_panel8, 0, wx.ALL, 5)
        
        self.SetSizer(bSizer6)
        self.Layout()
        
        self.Centre(wx.BOTH)
        
        # lstSang 객체에 제목을 표사하기
        self.lstSang.InsertColumn(0, '코드', width=50)
        self.lstSang.InsertColumn(1, '상품명', width=150)
        self.lstSang.InsertColumn(2, '수량', width=50)
        self.lstSang.InsertColumn(3, '단가', width=100)
        self.lstSang.InsertColumn(4, '금액', width=150)
        
        # Connect Events
        self.btnInsert.Bind(wx.EVT_BUTTON, self.OnRegist)
    
        self.DisplayData()

    # Virtual event handlers, overide them in your derived class
    def OnRegist(self, event):
        self.DataCheck()
        
    
    # 입력자료 검사
    def DataCheck(self):
        # 상품명
        if self.txtName.GetValue() == '':
            wx.MessageBox('상품명을 입력하세요', '알림', wx.OK)
            self.txtName.SetFocus()
            return
        # 수량 - 공백
        if self.txtSu.GetValue() == "":
            wx.MessageBox("수량을 입력하세요", '알림', wx.OK)
            self.txtSu.SetFocus()
            return
        # 수량 - 숫자
        try:
            su_int = int(self.txtSu.GetValue())
            # 음수체크
            if su_int < 0:
                wx.MessageBox("양수를 입력하세요", '알림', wx.OK)
                self.txtSu.SetFocus()
                return
            
        except TypeError:
            wx.MessageBox("숫자를 입력하세요", '알림', wx.OK)
            self.txtSu.SetFocus()
        # 단가 - 공백
        if self.txtDan.GetValue() == '':
            wx.MessageBox('단가를 입력하세요', '알림', wx.OK)
            self.txtDan.SetFocus()
            return
        
        # 단가- 숫자
        try:
            
            dan_int = int(self.txtDan.GetValue())
            # 음수체크
            if dan_int < 0:
                wx.MessageBox("양수를 입력하세요", '알림', wx.OK)
                self.txtDan.SetFocus()
                return
            
        except TypeError:
            wx.MessageBox("숫자를 입력하세요", '알림', wx.OK)
            self.txtDan.SetFocus()
        
        #검사 완료후 등록
        self.RegistSangpum()

    # 상품 등록
    def RegistSangpum(self):
        try: 
            conn = MySQLdb.connect(**config)
            cursor = conn.cursor()
            
            # 상품 번호 최대치 구하기
            sql = "select max(code) from sangdata"
            cursor.execute(sql)
            codeMax = cursor.fetchone()
    
            # 데이터 삽입
            sql = "insert into sangdata values (%s, %s, %s, %s)"
            sql_data = (str(codeMax[0] +1), self.txtName.GetValue(), self.txtSu.GetValue(), self.txtDan.GetValue()) 
            cursor.execute(sql, sql_data)
            conn.commit()
            
            #다시 출력
            self.DisplayData()
            
        except Exception as err:
            print(err)
            
        finally:
            cursor.close()
            conn.close()    
    
    # 상품 출력
    def DisplayData(self):    
        try:
            conn = MySQLdb.connect(**config)
            cursor = conn.cursor()
            sql = "select * from sangdata"
        
            cursor.execute(sql)
            datas = cursor.fetchall()
        
            self.lstSang.DeleteAllItems()
    
            for d in datas:
                price = float(d[2]) * float(d[3])
                i = self.lstSang.InsertItem(1000, 0)
                self.lstSang.SetItem(i, 0, str(d[0]))
                self.lstSang.SetItem(i, 1, str(d[1]))
                self.lstSang.SetItem(i, 2, str(d[2]))
                self.lstSang.SetItem(i, 3, str(d[3]))
                self.lstSang.SetItem(i, 4, "{0:,.0f}".format(price)) # 금액 포맷팅
            self.labelCount.SetLabelText('건수 : ' + str(len(datas)))
            
        except Exception as err:
            print(err)
            
        finally:
            cursor.close()
            conn.close()

            
if __name__ == '__main__':
    app = wx.App()
    MyFrame2(None).Show()
    app.MainLoop()         
