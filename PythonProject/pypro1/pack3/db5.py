import wx
import wx.xrc
import MySQLdb
import ast

rec_r = 0
gogekDatas = []
jikData = ()

with open('mydict.txt', mode='r') as ff:
    aa = ff.read()
    config = ast.literal_eval(aa)


class MyFrame2 (wx.Frame):
    
    def __init__(self, parent):
        wx.Frame.__init__ (self, parent, id=wx.ID_ANY, title=u"고객자료", pos=wx.DefaultPosition, size=wx.Size(751, 190), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)
        
#         self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        self.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_MENU))
        
        bSizer6 = wx.BoxSizer(wx.VERTICAL)
        
        self.m_panel5 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer7 = wx.BoxSizer(wx.HORIZONTAL)
        
        self.NoLabel = wx.StaticText(self.m_panel5, wx.ID_ANY, u"번호 : ", wx.DefaultPosition, wx.DefaultSize, 0)
        self.NoLabel.Wrap(-1)
        bSizer7.Add(self.NoLabel, 0, wx.ALL, 5)
        
        self.txtGogekNo = wx.TextCtrl(self.m_panel5, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer7.Add(self.txtGogekNo, 0, wx.ALL, 5)
        
        self.GnameLabel = wx.StaticText(self.m_panel5, wx.ID_ANY, u"고객명 : ", wx.DefaultPosition, wx.DefaultSize, 0)
        self.GnameLabel.Wrap(-1)
        bSizer7.Add(self.GnameLabel, 0, wx.ALL, 5)
        
        self.txtGogekName = wx.TextCtrl(self.m_panel5, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer7.Add(self.txtGogekName, 0, wx.ALL, 5)
        
        self.GenLabel = wx.StaticText(self.m_panel5, wx.ID_ANY, u"성별 : ", wx.DefaultPosition, wx.DefaultSize, 0)
        self.GenLabel.Wrap(-1)
        bSizer7.Add(self.GenLabel, 0, wx.ALL, 5)
        
        self.txtGogekGen = wx.TextCtrl(self.m_panel5, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer7.Add(self.txtGogekGen, 0, wx.ALL, 5)
        
        self.m_panel5.SetSizer(bSizer7)
        self.m_panel5.Layout()
        bSizer7.Fit(self.m_panel5)
        bSizer6.Add(self.m_panel5, 0, wx.EXPAND | wx.ALL, 5)
        
        self.m_panel6 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer8 = wx.BoxSizer(wx.HORIZONTAL)
        
        self.btnFirst = wx.Button(self.m_panel6, wx.ID_ANY, u"처음", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer8.Add(self.btnFirst, 0, wx.ALL, 5)
        
        self.btnPre = wx.Button(self.m_panel6, wx.ID_ANY, u"이전", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer8.Add(self.btnPre, 0, wx.ALL, 5)
        
        self.btnNext = wx.Button(self.m_panel6, wx.ID_ANY, u"다음", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer8.Add(self.btnNext, 0, wx.ALL, 5)
        
        self.btnLast = wx.Button(self.m_panel6, wx.ID_ANY, u"마지막", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer8.Add(self.btnLast, 0, wx.ALL, 5)
        
        self.m_panel6.SetSizer(bSizer8)
        self.m_panel6.Layout()
        bSizer8.Fit(self.m_panel6)
        bSizer6.Add(self.m_panel6, 0, wx.EXPAND | wx.ALL, 5)
        
        self.m_panel7 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer9 = wx.BoxSizer(wx.HORIZONTAL)
        
        self.JikNameLabel = wx.StaticText(self.m_panel7, wx.ID_ANY, u"직원명 :", wx.DefaultPosition, wx.DefaultSize, 0)
        self.JikNameLabel.Wrap(-1)
        bSizer9.Add(self.JikNameLabel, 0, wx.ALL, 5)
        
        self.txtJikName = wx.TextCtrl(self.m_panel7, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(70, -1), 0)
        bSizer9.Add(self.txtJikName, 0, wx.ALL, 5)
        
        self.BusNameLabel = wx.StaticText(self.m_panel7, wx.ID_ANY, u"부서명 : ", wx.DefaultPosition, wx.DefaultSize, 0)
        self.BusNameLabel.Wrap(-1)
        bSizer9.Add(self.BusNameLabel, 0, wx.ALL, 5)
        
        self.txtBusName = wx.TextCtrl(self.m_panel7, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(85, -1), 0)
        bSizer9.Add(self.txtBusName, 0, wx.ALL, 5)
        
        self.busTelLabel = wx.StaticText(self.m_panel7, wx.ID_ANY, u"전화 : ", wx.DefaultPosition, wx.DefaultSize, 0)
        self.busTelLabel.Wrap(-1)
        bSizer9.Add(self.busTelLabel, 0, wx.ALL, 5)
        
        self.txtBusTel = wx.TextCtrl(self.m_panel7, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer9.Add(self.txtBusTel, 0, wx.ALL, 5)
        
        self.JikJikLabel = wx.StaticText(self.m_panel7, wx.ID_ANY, u"직급 : ", wx.DefaultPosition, wx.DefaultSize, 0)
        self.JikJikLabel.Wrap(-1)
        bSizer9.Add(self.JikJikLabel, 0, wx.ALL, 5)
        
        self.txtJikJik = wx.TextCtrl(self.m_panel7, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(70, -1), 0)
        bSizer9.Add(self.txtJikJik, 0, wx.ALL, 5)
        
        self.m_panel7.SetSizer(bSizer9)
        self.m_panel7.Layout()
        bSizer9.Fit(self.m_panel7)
        bSizer6.Add(self.m_panel7, 1, wx.EXPAND | wx.ALL, 5)
        
        self.SetSizer(bSizer6)
        self.Layout()
        
        self.Centre(wx.BOTH)
        
        # Connect Events
        self.btnFirst.Bind(wx.EVT_BUTTON, self.OnClick)
        self.btnPre.Bind(wx.EVT_BUTTON, self.OnClick)
        self.btnNext.Bind(wx.EVT_BUTTON, self.OnClick)
        self.btnLast.Bind(wx.EVT_BUTTON, self.OnClick)
        
        self.btnFirst.id = 1;
        self.btnPre.id = 2;
        self.btnNext.id = 3;
        self.btnLast.id = 4;
        
        self.DbLoad()
    
    # Virtual event handlers, overide them in your derived class
    # ===== OnClick : 버튼 클릭 이벤트 ===== 
    def OnClick(self, event):
        id = event.GetEventObject().id
        # print(id)
    
        global rec_r
        
        # 처음 가기
        if id == 1: 
            rec_r = 0
        # 이전
        elif id == 2:
            rec_r = rec_r - 1
            if rec_r < 0: rec_r = 0
        # 다음
        elif id == 3:
            rec_r = rec_r + 1
            if rec_r > (len(gogekDatas) - 1): rec_r = (len(gogekDatas) - 1)
        elif id == 4:
            rec_r = len(gogekDatas) - 1
        
        self.JikSearch(rec_r)
        self.ShowData(rec_r)
    
    # ===== DbLoad : 첫 DB Load , 고객데이터 gogekDatas에 저장 =====
    def DbLoad(self):
        try:
            conn = MySQLdb.connect(**config)
            cursor = conn.cursor()
            sql = "select gogek_no, gogek_name, gogek_jumin, gogek_damsano from gogek"
            cursor.execute(sql)
            
            # 고객 데이터 저장
            global gogekDatas
            gogekDatas = cursor.fetchall()
            
            self.JikSearch(rec_r)
            self.ShowData(rec_r)
            
        except Exception as err:
            print('DbLoad Err : ' + str(err))
        finally:
            cursor.close()
            conn.close()
    
    # ===== ShowData : 출력 메소드  =====
    def ShowData(self, r):
        self.txtGogekNo.SetLabelText(str(gogekDatas[r][0]))
        self.txtGogekName.SetLabelText(str(gogekDatas[r][1]))
        if str(gogekDatas[r][2])[7] == "1":
            gogekGen = "남"
        else: 
            gogekGen = "여"
            
        self.txtGogekGen.SetLabelText(gogekGen)
        self.txtJikName.SetLabelText(str(jikData[0]))
        self.txtBusName.SetLabelText(str(jikData[1]))
        self.txtBusTel.SetLabelText(str(jikData[2]))
        self.txtJikJik.SetLabelText(str(jikData[3]))
    
    # ===== JikSearch : 고객 데이터를 받고 직원 데이터를 찾아 jikData에 저장 ===== 
    def JikSearch(self, rec_r):
        try:
            conn = MySQLdb.connect(**config)
            cursor = conn.cursor()
            
            # 직원 데이터 저장
            damsano = str(gogekDatas[rec_r][3])
            sql = '''
            select jikwon_name, buser_name, buser_tel, jikwon_jik 
            from jikwon 
            left join buser on buser_num = buser_no 
            where jikwon_no = %s
            '''
            cursor.execute(sql, (damsano,))
            
            global jikData
            jikData = cursor.fetchone()
        
        except Exception as err:
            print('jik Err : ' + str(err))
        finally:
            cursor.close()
            conn.close()

            
if __name__ == '__main__':
    app = wx.App()
    MyFrame2(None).Show()
    app.MainLoop()      
