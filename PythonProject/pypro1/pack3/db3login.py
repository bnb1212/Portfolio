import MySQLdb
import sys

# GUI
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
# # Class MyFrame1
###########################################################################

config = {  # dictionary 타입
    'host':'127.0.0.1',
    'user':'root',
    'password':'123',
    'database':'test',
    'port':3306,
    'charset':'utf8',
    'use_unicode':True
}

class MyFrame1 (wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__ (self, parent, id=wx.ID_ANY, title=u"직원 관리 고객", pos=wx.DefaultPosition, size=wx.Size(500, 300), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)
        
        # self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)
        self.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_MENU))
        
        bSizer1 = wx.BoxSizer(wx.VERTICAL)
        
        self.m_panel1 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer2 = wx.BoxSizer(wx.HORIZONTAL)
        
        self.NoLabel = wx.StaticText(self.m_panel1, wx.ID_ANY, u"사번 : ", wx.DefaultPosition, wx.DefaultSize, 0)
        self.NoLabel.Wrap(-1)
        bSizer2.Add(self.NoLabel, 0, wx.ALL, 5)
        
        self.txtNo = wx.TextCtrl(self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer2.Add(self.txtNo, 0, wx.ALL, 5)
        
        self.NameLabel = wx.StaticText(self.m_panel1, wx.ID_ANY, u"직원명 : ", wx.DefaultPosition, wx.DefaultSize, 0)
        self.NameLabel.Wrap(-1)
        bSizer2.Add(self.NameLabel, 0, wx.ALL, 5)
        
        self.txtName = wx.TextCtrl(self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer2.Add(self.txtName, 0, wx.ALL, 5)
        
        self.btnLogin = wx.Button(self.m_panel1, wx.ID_ANY, u"로그인", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer2.Add(self.btnLogin, 0, wx.ALL, 5)
        
        self.m_panel1.SetSizer(bSizer2)
        self.m_panel1.Layout()
        bSizer2.Fit(self.m_panel1)
        bSizer1.Add(self.m_panel1, 0, wx.EXPAND | wx.ALL, 5)
        
        self.m_panel2 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer3 = wx.BoxSizer(wx.VERTICAL)
        
        self.staMsgLabel = wx.StaticText(self.m_panel2, wx.ID_ANY, u"정보", wx.DefaultPosition, wx.DefaultSize, 0)
        self.staMsgLabel.Wrap(-1)
        bSizer3.Add(self.staMsgLabel, 0, wx.ALL, 5)
        
        self.m_panel2.SetSizer(bSizer3)
        self.m_panel2.Layout()
        bSizer3.Fit(self.m_panel2)
        bSizer1.Add(self.m_panel2, 0, wx.EXPAND | wx.ALL, 5)
        
        self.m_panel3 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer4 = wx.BoxSizer(wx.VERTICAL)
        
        self.lstGogek = wx.ListCtrl(self.m_panel3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_REPORT)
        bSizer4.Add(self.lstGogek, 1, wx.ALL | wx.EXPAND, 5)
        
        self.m_panel3.SetSizer(bSizer4)
        self.m_panel3.Layout()
        bSizer4.Fit(self.m_panel3)
        bSizer1.Add(self.m_panel3, 1, wx.EXPAND | wx.ALL, 5)
        
        self.m_panel4 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer5 = wx.BoxSizer(wx.VERTICAL)
        
        self.staCountLabel = wx.StaticText(self.m_panel4, wx.ID_ANY, u"인원수 : 0", wx.DefaultPosition, wx.DefaultSize, 0)
        self.staCountLabel.Wrap(-1)
        bSizer5.Add(self.staCountLabel, 0, wx.ALL, 5)
        
        self.m_panel4.SetSizer(bSizer5)
        self.m_panel4.Layout()
        bSizer5.Fit(self.m_panel4)
        bSizer1.Add(self.m_panel4, 0, wx.EXPAND | wx.ALL, 5)
        
        self.SetSizer(bSizer1)
        self.Layout()
        
        self.Centre(wx.BOTH)
        
        # lstGogek 객체에 제목을 표사하기
        self.lstGogek.InsertColumn(0, '고객번호', width=100)
        self.lstGogek.InsertColumn(1, '고객명', width=150)
        self.lstGogek.InsertColumn(2, '고객전화', width=200)
        
        # Connect Events
        self.btnLogin.Bind(wx.EVT_BUTTON, self.OnLogin)
    
    class MyFrame1 (wx.Frame):

        def __init__(self, parent):
            pass

        def __del__(self):
            pass
        
    # Virtual event handlers, overide them in your derived class
    def OnLogin(self, event):
        if self.txtNo.GetValue() == '':
            wx.MessageBox('사번을 입력하세여', '알림', wx.OK)
            self.txtName.SetFocus()
            return
        
        if self.txtName.GetValue() == "":
            wx.MessageBox("이름을 입력하세요", '알림', wx.OK)
            self.txtName.SetFocus()
            return 
        
        self.LoginCheck()
        
    def LoginCheck(self):
        try:
            conn = MySQLdb.connect(**config)
            # print(conn)
            cursor = conn.cursor()  # SQL문 수행을 위한 커서 객체 생성
            
            no = self.txtNo.GetValue()
            name = self.txtName.GetValue()
            
            sql = '''
            select count(jikwon_no)
            from jikwon
            where jikwon_no ='{0}' and jikwon_name='{1}'
            '''.format(no, name)
            
            cursor.execute(sql)
            count = cursor.fetchone()
            print(count)

            if len(count) <= 0:
                wx.MessageBox("로그인 실패" , '알림' , wx.OK)
            else:
                self.DisplayData(no)
        except Exception as err:
            print(err)
        finally:
            cursor.close()
            conn.close()
    
    def DisplayData(self, no):
        try:
            conn = MySQLdb.connect(**config)
            # print(conn)
            cursor = conn.cursor()  # SQL문 수행을 위한 커서 객체 생성
            
            sql = '''
            select gogek_no, gogek_name, gogek_tel
            from gogek
            where gogek_damsano={}
            '''.format(no)
        
            cursor.execute(sql)
            datas = cursor.fetchall()
        
            self.lstGogek.DeleteAllItems()
    
            for d in datas:
                i = self.lstGogek.InsertItem(1000, 0)
                self.lstGogek.SetItem(i, 0, str[0])
                self.lstGogek.SetItem(i, 1, str[1])
                self.lstGogek.SetItem(i, 2, str[2])
                
            self.staCountLabel.SetLabelText('인원수 : ' , str(len(datas)))
            
        except Exception as err:
            print(err)
            
        finally:
            cursor.close()
            conn.close()


if __name__ == '__main__':
    app = wx.App()
    MyFrame1(None).Show()
    app.MainLoop()         
