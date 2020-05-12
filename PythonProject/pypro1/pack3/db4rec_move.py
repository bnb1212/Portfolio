import wx
import wx.xrc
import ast
import MySQLdb

rec_r = 0
datas = []

with open('mydict.txt', mode='r') as ff:
    aa = ff.read()
    config = ast.literal_eval(aa)

class MyFrame2 (wx.Frame):
    
    def __init__(self, parent):
        wx.Frame.__init__ (self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition, size=wx.Size(500, 300), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)
        
        # self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        self.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_MENU))
        
        bSizer6 = wx.BoxSizer(wx.VERTICAL)
        
        self.m_panel5 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer7 = wx.BoxSizer(wx.HORIZONTAL)
        
        self.m_staticText6 = wx.StaticText(self.m_panel5, wx.ID_ANY, u"코드 : ", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText6.Wrap(-1)
        bSizer7.Add(self.m_staticText6, 0, wx.ALL, 5)
        
        self.txtNo = wx.TextCtrl(self.m_panel5, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer7.Add(self.txtNo, 0, wx.ALL, 5)
        
        self.staName = wx.StaticText(self.m_panel5, wx.ID_ANY, u"품명 : ", wx.DefaultPosition, wx.DefaultSize, 0)
        self.staName.Wrap(-1)
        bSizer7.Add(self.staName, 0, wx.ALL, 5)
        
        self.txtSang = wx.TextCtrl(self.m_panel5, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer7.Add(self.txtSang, 0, wx.ALL, 5)
        
        self.m_panel5.SetSizer(bSizer7)
        self.m_panel5.Layout()
        bSizer7.Fit(self.m_panel5)
        bSizer6.Add(self.m_panel5, 0, wx.EXPAND | wx.ALL, 5)
        
        self.m_panel6 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer3 = wx.BoxSizer(wx.HORIZONTAL)
        
        self.m_staticText61 = wx.StaticText(self.m_panel6, wx.ID_ANY, u"수량 : ", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText61.Wrap(-1)
        bSizer3.Add(self.m_staticText61, 0, wx.ALL, 5)
        
        self.txtSu = wx.TextCtrl(self.m_panel6, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer3.Add(self.txtSu, 0, wx.ALL, 5)
        
        self.staName1 = wx.StaticText(self.m_panel6, wx.ID_ANY, u"단가 : ", wx.DefaultPosition, wx.DefaultSize, 0)
        self.staName1.Wrap(-1)
        bSizer3.Add(self.staName1, 0, wx.ALL, 5)
        
        self.txtDan = wx.TextCtrl(self.m_panel6, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer3.Add(self.txtDan, 0, wx.ALL, 5)
        
        self.m_panel6.SetSizer(bSizer3)
        self.m_panel6.Layout()
        bSizer3.Fit(self.m_panel6)
        bSizer6.Add(self.m_panel6, 0, wx.EXPAND | wx.ALL, 5)
        
        self.m_panel7 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer4 = wx.BoxSizer(wx.VERTICAL)
        
        self.staKeum = wx.StaticText(self.m_panel7, wx.ID_ANY, u"금액 : 0", wx.DefaultPosition, wx.DefaultSize, 0)
        self.staKeum.Wrap(-1)
        bSizer4.Add(self.staKeum, 0, wx.ALL, 5)
        
        self.m_panel7.SetSizer(bSizer4)
        self.m_panel7.Layout()
        bSizer4.Fit(self.m_panel7)
        bSizer6.Add(self.m_panel7, 0, wx.EXPAND | wx.ALL, 5)
        
        self.m_panel8 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer5 = wx.BoxSizer(wx.HORIZONTAL)
        
        self.m_button1 = wx.Button(self.m_panel8, wx.ID_ANY, u"||<<", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer5.Add(self.m_button1, 0, wx.ALL, 5)
        
        self.m_button2 = wx.Button(self.m_panel8, wx.ID_ANY, u"<<", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer5.Add(self.m_button2, 0, wx.ALL, 5)
        
        self.m_button3 = wx.Button(self.m_panel8, wx.ID_ANY, u">>", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer5.Add(self.m_button3, 0, wx.ALL, 5)
        
        self.m_button4 = wx.Button(self.m_panel8, wx.ID_ANY, u">>||", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer5.Add(self.m_button4, 0, wx.ALL, 5)
        
        self.m_panel8.SetSizer(bSizer5)
        self.m_panel8.Layout()
        bSizer5.Fit(self.m_panel8)
        bSizer6.Add(self.m_panel8, 1, wx.EXPAND | wx.ALL, 5)
        
        self.SetSizer(bSizer6)
        self.Layout()
        
        self.Centre(wx.BOTH)
        
        # Connect Events
        self.m_button1.id = 1;
        self.m_button2.id = 2;
        self.m_button3.id = 3;
        self.m_button4.id = 4;
        
        self.m_button1.Bind(wx.EVT_BUTTON, self.OnClick)
        self.m_button2.Bind(wx.EVT_BUTTON, self.OnClick)
        self.m_button3.Bind(wx.EVT_BUTTON, self.OnClick)
        self.m_button4.Bind(wx.EVT_BUTTON, self.OnClick)
        
        self.DbLoad()
    
    # Virtual event handlers, overide them in your derived class
    def OnClick(self, event):
        id = event.GetEventObject().id
        #print(id)
    
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
            if rec_r > (len(datas) - 1): rec_r = (len(datas) - 1)
        elif id == 4:
            rec_r = len(datas) - 1
        
        self.ShowData(rec_r)
    
    def DbLoad(self):
        try:
            conn = MySQLdb.connect(**config)
            cursor = conn.cursor()
            sql = "select * from sangdata"
            cursor.execute(sql)
            
            global datas
            datas = cursor.fetchall()
            #print(datas[0][0])
            
            self.ShowData(rec_r)
            
            
        except Exception as err:
            print('DbLoad Err : ' + str(err))
        finally:
            cursor.close()
            conn.close()
            
    
    def ShowData(self, r):
        self.txtNo.SetLabelText(str(datas[r][0]))
        self.txtSang.SetLabelText(str(datas[r][1]))
        self.txtSu.SetLabelText(str(datas[r][2]))
        self.txtDan.SetLabelText(str(datas[r][3]))
        self.staKeum.SetLabelText("금액 : " + str(datas[r][2] * datas[r][3]))
        
if __name__ == '__main__':
    app = wx.App()
    MyFrame2(None).Show()
    app.MainLoop()      

