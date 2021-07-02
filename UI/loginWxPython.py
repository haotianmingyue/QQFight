# 开发者 haotian
# 开发时间: 2021/7/1 18:47
import wx
login=wx.App()
# 顶级窗口
login_window=wx.Frame(None,title='登录',size=(300,300))
# 导入面板
login_panel=wx.Panel(login_window)
# 显示
login_window.Show(True)
#运行
login.MainLoop()


