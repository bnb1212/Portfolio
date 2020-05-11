# 레이아웃 매니저 중에서 BoxSizer()

import wx


class MyFrame(wx.Frame):

        def __init__(self, parent, title):
            super(MyFrame, self).__init__(parent, title=title, size=(400, 300))
        
            panel1 = wx.Panel(self, -1, style=wx.SUNKEN_BORDER)
            panel2 = wx.Panel(self, -1, style=wx.SUNKEN_BORDER)
            
            panel1.SetBackgroundColour('BLUE')
            panel2.SetBackgroundColour('RED')
            
            box = wx.BoxSizer(wx.HORIZONTAL)
            box.Add(panel1, 1, wx.EXPAND)
            box.Add(panel2, 2, wx.EXPAND)

            self.SetSizer(box)
            self.Center()
            self.Show()
            
    
if __name__ == '__main__':
    app = wx.App()
    MyFrame(None, title='BoxSizer() 연습')
    app.MainLoop()           
