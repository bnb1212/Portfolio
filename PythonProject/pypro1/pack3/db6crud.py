import wx
import wx.xrc
import ast
import MySQLdb
from IPython.utils._sysinfo import commit

with open('mydict.txt', mode='r') as f:
    config = ast.literal_eval(f.read())
    
    
class MyFrame2 (wx.Frame):
    
    def __init__(self, parent):
        wx.Frame.__init__ (self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition, size=wx.Size(355, 483), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)
        
        # self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        self.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_MENU))
        
        bSizer5 = wx.BoxSizer(wx.VERTICAL)
        
        self.m_panel4 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer6 = wx.BoxSizer(wx.HORIZONTAL)
        
        self.m_staticText8 = wx.StaticText(self.m_panel4, wx.ID_ANY, u"번호 : ", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText8.Wrap(-1)
        bSizer6.Add(self.m_staticText8, 0, wx.ALL, 5)
        
        self.txtNo = wx.TextCtrl(self.m_panel4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(-1, -1), 0)
        bSizer6.Add(self.txtNo, 1, wx.ALL, 5)
        
        self.btnInsert = wx.Button(self.m_panel4, wx.ID_ANY, u"등록", wx.DefaultPosition, wx.Size(110, -1), 0)
        bSizer6.Add(self.btnInsert, 0, wx.ALL, 5)
        
        self.m_panel4.SetSizer(bSizer6)
        self.m_panel4.Layout()
        bSizer6.Fit(self.m_panel4)
        bSizer5.Add(self.m_panel4, 0, wx.EXPAND | wx.ALL, 5)
        
        self.m_panel5 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer7 = wx.BoxSizer(wx.HORIZONTAL)
        
        self.m_staticText9 = wx.StaticText(self.m_panel5, wx.ID_ANY, u"이름 : ", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText9.Wrap(-1)
        bSizer7.Add(self.m_staticText9, 0, wx.ALL, 5)
        
        self.txtName = wx.TextCtrl(self.m_panel5, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer7.Add(self.txtName, 1, wx.ALL, 5)
        
        self.btnUpdate = wx.Button(self.m_panel5, wx.ID_ANY, u"수정", wx.DefaultPosition, wx.Size(50, -1), 0)
        bSizer7.Add(self.btnUpdate, 0, wx.ALL, 5)
        
        self.btnConfirm = wx.Button(self.m_panel5, wx.ID_ANY, u"확인", wx.DefaultPosition, wx.Size(50, -1), 0)
        bSizer7.Add(self.btnConfirm, 0, wx.ALL, 5)
        
        self.m_panel5.SetSizer(bSizer7)
        self.m_panel5.Layout()
        bSizer7.Fit(self.m_panel5)
        bSizer5.Add(self.m_panel5, 0, wx.EXPAND | wx.ALL, 5)
        
        self.m_panel6 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer8 = wx.BoxSizer(wx.HORIZONTAL)
        
        self.m_staticText10 = wx.StaticText(self.m_panel6, wx.ID_ANY, u"전화 : ", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText10.Wrap(-1)
        bSizer8.Add(self.m_staticText10, 0, wx.ALL, 5)
        
        self.txtTel = wx.TextCtrl(self.m_panel6, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer8.Add(self.txtTel, 1, wx.ALL, 5)
        
        self.btnDel = wx.Button(self.m_panel6, wx.ID_ANY, u"삭제", wx.DefaultPosition, wx.Size(110, -1), 0)
        bSizer8.Add(self.btnDel, 0, wx.ALL, 5)
        
        self.m_panel6.SetSizer(bSizer8)
        self.m_panel6.Layout()
        bSizer8.Fit(self.m_panel6)
        bSizer5.Add(self.m_panel6, 0, wx.EXPAND | wx.ALL, 5)
        
        self.m_panel7 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer9 = wx.BoxSizer(wx.VERTICAL)
        
        self.lstMem = wx.ListCtrl(self.m_panel7, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_REPORT)
        bSizer9.Add(self.lstMem, 1, wx.ALL | wx.EXPAND, 5)
        
        self.m_panel7.SetSizer(bSizer9)
        self.m_panel7.Layout()
        bSizer9.Fit(self.m_panel7)
        bSizer5.Add(self.m_panel7, 1, wx.EXPAND | wx.ALL, 5)
        
        self.m_panel8 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer10 = wx.BoxSizer(wx.HORIZONTAL)
        
        self.m_staticText11 = wx.StaticText(self.m_panel8, wx.ID_ANY, u"인원수 : ", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText11.Wrap(-1)
        bSizer10.Add(self.m_staticText11, 0, wx.ALL, 5)
        
        self.staCount = wx.StaticText(self.m_panel8, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0)
        self.staCount.Wrap(-1)
        bSizer10.Add(self.staCount, 0, wx.ALL, 5)
        
        self.m_panel8.SetSizer(bSizer10)
        self.m_panel8.Layout()
        bSizer10.Fit(self.m_panel8)
        bSizer5.Add(self.m_panel8, 0, wx.ALL, 5)
        
        self.SetSizer(bSizer5)
        self.Layout()
        
        self.Centre(wx.BOTH)
        
        # Connect Events
        self.btnInsert.Bind(wx.EVT_BUTTON, self.OnBtnClick)
        self.btnUpdate.Bind(wx.EVT_BUTTON, self.OnBtnClick)
        self.btnConfirm.Bind(wx.EVT_BUTTON, self.OnBtnClick)
        self.btnDel.Bind(wx.EVT_BUTTON, self.OnBtnClick)
        
        self.btnInsert.id = 1
        self.btnUpdate.id = 2
        self.btnConfirm.id = 3
        self.btnDel.id = 4
    
        self.lstMem.InsertColumn(0, '번호', width=50)
        self.lstMem.InsertColumn(1, '이름', width=100)
        self.lstMem.InsertColumn(2, '전화', width=150)
        
        self.btnConfirm.Enable(enable=False)
        
        self.ViewListData()
        
    def __del__(self):
        pass
    
    def ViewListData(self):
        try:
            conn = MySQLdb.connect(**config)
            cursor = conn.cursor()
            
            sql = "select * from pymem"
            cursor.execute(sql)
            
            self.lstMem.DeleteAllItems()
            count = 0
            
            print(cursor)
            for data in cursor:
                i = self.lstMem.InsertItem(5000, 0)  # 65535개의 행까지 줄 수 있음
                self.lstMem.SetItem(i, 0, str(data[0]))
                self.lstMem.SetItem(i, 1, data[1])
                self.lstMem.SetItem(i, 2, data[2])
                count += 1
            self.staCount.SetLabelText(str(count))
            
        except Exception as e:
            wx.MessageBox("ViewListData err : " + str(e))
    
        finally:
            cursor.close()
            conn.close()
            
    # Virtual event handlers, overide them in your derived class
    def OnBtnClick(self, event):
        id = event.GetEventObject().id
        
        if id == 1:
            self.MemInsert()  # 등록 메소드
        elif id == 2:
            self.MemUpdate()  # 수정 준비
        elif id == 3:
            self.MemUpdateOk()  # 수정 처리
        elif id == 4: 
            self.MemDelete()  # 삭제 처리
        elif id == 5:
            self.MemUpdateCancel()  # 수정 취소
    
    # Insert Member ==================================================
    def MemInsert(self):
        no = self.txtNo.GetValue()
        name = self.txtName.GetValue()
        tel = self.txtTel.GetValue()
        
        if no == '' or name == '' or tel == '':
            wx.MessageBox('자료를 입력하시오', '입력', wx.OK)
            return
            
        try:
            conn = MySQLdb.connect(**config)
            cursor = conn.cursor()
            data = self.SelectData(no)  # 추가용 번호의 등록 가능 여부 판단
            if data != None:  # 존재한다면 중복이 될수 있음
                wx.MessageBox('이미 사용중인 번호입니다.', '알림', wx.OK)
                self.txtNo.SetFocus()
                return
            
            # 추가 계속
            sql = "insert into pymem values(%s, %s, %s)"
            cursor.execute(sql, (no, name, tel))
            '''
            if result != 1:
                conn.rollback()
                # ...
                return 
            '''
            conn.commit()
            
            self.ViewListData()  # 추가후 자료 보기
            self.txtNo.SetValue("")
            self.txtName.SetValue("")
            self.txtTel.SetValue("")
            
        except Exception as e:
            wx.MessageBox('MemInsert err : ' + str(e))
            conn.rollback()
        
        finally:
            cursor.close()
            conn.close()
            
    # Update Member ==================================================
    def MemUpdate(self):
        dlg = wx.TextEntryDialog(None, '수정할 번호 입력', '수정')
        if dlg.ShowModal() == wx.ID_OK:
            if dlg.GetValue == '':
                return 
            
            upno = dlg.GetValue()
            print(upno)
            data = self.SelectData(upno)
            if data == None:
                wx.MessageBox(upno + '번은 등록된 자료가 아닙니다.', '알림', wx.OK)
                return
            
            # 수정 준비 계속
            self.txtNo.SetValue(str(data[0]))
            self.txtName.SetValue(data[1])
            self.txtTel.SetValue(data[2])
                                
            self.txtNo.SetEditable(False)
            self.btnConfirm.Enable(True)
            self.btnUpdate.SetLabel("취소")
            self.btnUpdate.id = 5
        else:
            return
        
        dlg.Destroy()
    
    # MemberUpdateOk : 실제로 자료 업데이트 하는 부분 ========================
    def MemUpdateOk(self):
        no = self.txtNo.GetValue()
        name = self.txtName.GetValue()
        tel = self.txtTel.GetValue()
        
        if no == '' or name == '' or tel == '':
            wx.MessageBox('자료를 입력하시오', '입력', wx.OK)
            return
            
        try:
            conn = MySQLdb.connect(**config)
            cursor = conn.cursor()
            
            sql = "update pymem set irum=%s, junhwa=%s where bun=%s"
            cursor.execute(sql, (name, tel, no))
            conn.commit()
            
            self.ViewListData()  # 수정후 자료 보기
            self.txtNo.SetValue('')
            self.txtName.SetValue('')
            self.txtTel.SetValue('')
            self.txtNo.SetEditable(True)
            self.btnUpdate.SetLabel("수정")
            self.btnUpdate.id = 2
            self.btnConfirm.Enable(False)
            
        except Exception as e:
            wx.MessageBox('MemUpdateOk err : ' + str(e))
            conn.rollback()
        
        finally:
            cursor.close()
            conn.close()

    # MemUpdateCancel : 수정 취소 ======================================
    def MemUpdateCancel(self):
        self.ViewListData()  # 수정후 자료 보기
        self.txtNo.SetValue('')
        self.txtName.SetValue('')
        self.txtTel.SetValue('')
        self.txtNo.SetEditable(True)
        self.btnUpdate.SetLabel("수정")
        self.btnUpdate.id = 2
        self.btnConfirm.Enable(False)
    
    def MemDelete(self):
        dlg = wx.TextEntryDialog(None, '삭제할 번호 입력', '수정')
        if dlg.ShowModal() == wx.ID_OK:
            if dlg.GetValue == '':
                return 
            
            delno = dlg.GetValue()
            data = self.SelectData(delno)
            if data == None:
                wx.MessageBox(delno + '번은 등록된 자료가 아닙니다.', '알림', wx.OK)
                return
            
            # 삭제 준비 계속
        try:
            conn = MySQLdb.connect(**config)
            cursor = conn.cursor()
            sql = "delete from pymem where bun=%s"
            cursor.execute(sql, (delno,))
            conn.commit()
            
            self.ViewListData() # 삭제후 자료 보기
            
        except Exception as e:
            wx.MessageBox('MemDelete err : ' + str(e))
        
        finally:
            cursor.close()
            conn.close()
 
    def SelectData(self, no):  # 해당 번호 자료 읽기 ( i, u, d에서 사용 )
        try:
            conn = MySQLdb.connect(**config)
            cursor = conn.cursor()
            sql = "select * from pymem where bun = %s"
            sqldata = (no,)
            
            cursor.execute(sql, sqldata)
            data = cursor.fetchone()
            
            return data
            
        except Exception as e:
            wx.MessageBox('SelectData err : ' + str(e))
        
        finally:
            cursor.close()
            conn.close()

     
if __name__ == '__main__':
    app = wx.App()
    MyFrame2(None).Show()
    app.MainLoop()      

