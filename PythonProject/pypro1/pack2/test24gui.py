# Graphic User Interface. 윈도우 프로그래밍 ( wxPython ) 라이브러리를 사용
 
import wx
# app = wx.App(False)  
# frame = wx.Frame(None, wx.ID_ANY, "Hello World")
# frame.Show(True)  
# app.MainLoop() # 창을 무한 루프에 빠트림


class Ex(wx.Frame):

    def __init__(self, parent, title):
        super(Ex, self).__init__(parent, title=title, size=(400, 300))
        
        # textBox 추가
        # self.txtA = wx.TextCtrl(self) # Single Line
        # self.txtA = wx.TextCtrl(self, style=wx.TE_MULTILINE) # text Area
    
        self.CreateStatusBar()  # 상태 표시줄
        
        # 메뉴(Menu) 추가
        menuBar = wx.MenuBar()
        mnuFile = wx.Menu()  # 메뉴 속성
        
        # 메뉴 항목 추가
        mnuNew = mnuFile.Append(wx.ID_NEW, 'New', '새글')
        mnuNew = mnuFile.Append(wx.ID_NEW, 'Open', '열기')
        mnuFile.AppendSeparator()  # 구분선
        mnuExit = mnuFile.Append(wx.ID_EXIT, 'Exit', '닫기')
        
        menuBar.Append(mnuFile, 'File')
        
        # 창에 붙이기
        self.SetMenuBar(menuBar)
         
        # 메뉴에 이벤트 장착
        self.Bind(wx.EVT_MENU, self.OnEvent1, mnuNew)
        self.Bind(wx.EVT_MENU, self.OnEvent2, mnuExit)
        
        # 라벨과 텍스트 Box 
        panel = wx.Panel(self)
        wx.StaticText(panel, label='i d : ', pos=(5, 5))  # 자바에서는 label.
        wx.StaticText(panel, label='pwd : ', pos=(5, 40))  
        self.txtA = wx.TextCtrl(panel, pos=(50, 5))
        self.txtB = wx.TextCtrl(panel, pos=(50, 40), size=(200, -1))
        
        # 버튼
        btn1 = wx.Button(panel, label='일반 버튼', pos=(5, 100))
        btn2 = wx.ToggleButton(panel, label='토글 버튼', pos=(100, 100))
        btn3 = wx.Button(panel, label=' 종료', pos=(200, 100), size=(50, -1))
        
        # 이벤트 함수 (처리방법 1)
#        btn1.Bind(wx.EVT_BUTTON, self.OnClick1)
#        btn2.Bind(wx.EVT_TOGGLEBUTTON, self.OnClick2)
#        btn3.Bind(wx.EVT_BUTTON, self.OnClick3)
#         
#       # 이벤트 처리 방법 2 - id 사용
        btn1.id = 1
        btn2.id = 2
        btn3.id = 3
        btn1.Bind(wx.EVT_BUTTON, self.OnClickAbc)
        btn2.Bind(wx.EVT_TOGGLEBUTTON, self.OnClickAbc)
        btn3.Bind(wx.EVT_BUTTON, self.OnClickAbc)
       
        self.Center()
        self.Show()
    
    # 이벤트 함수 (처리방법 1)
    def OnEvent1(self, event):
        self.txtA.SetLabelText('새글 메뉴 누름',)
    
    def OnEvent2(self, event):
        self.Close(True)
        
    def OnClick1(self, event):
        # 대화상자 호출
        msgDial = wx.MessageDialog(self, '메세지', '제목', wx.OK)
        msgDial.ShowModal()
        msgDial.Destroy()
    
        self.SetTitle("버튼1 클릭")

    def OnClick2(self, event):
#         print(event.GetEventObject().GetValue())
        if event.GetEventObject().GetValue():
            self.txtA.SetLabelText('토글 버튼 실행 1')
            self.txtB.SetLabelText('true')
            
        else:  # false일 떄 실행
            self.txtA.SetLabelText('토글 버튼 실행2')
            self.txtB.SetLabelText('false')
            
    def OnClick3(self, event):
        self.Close()
    
    # 1개의 이벤트 핸들러로 여러개 이벤트 관리
    def OnClickAbc(self, event):
        # print(event.GetEventObject(),id)
        bid = event.GetEventObject().id
        if bid == 1:
            self.SetTitle('버튼1')
        elif bid == 2:
            self.SetTitle('버튼2')
        else:
            self.Close()
            
            
if __name__ == '__main__':
    app = wx.App()
    Ex(None, title='연습')
    app.MainLoop()
