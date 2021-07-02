# 开发者 haotian
# 开发时间: 2021/6/30 22:12
import tkinter # 导入TKinter模块

login = tkinter.Tk(screenName='登录')  # 初始化Tk()创建Mac窗口对象

left_menu=tkinter.Menubutton(login)
left_menu.add_command(label='打开乐斗')
left_menu.pack()

tkinter.Label(login,text='用户名').pack()

l1=tkinter.Entry()
l1.pack()
tkinter.Label(login,text='密码').pack()
l2=tkinter.Entry()
l2.pack()

def getusername():
    username=l1.get()
    print(username)

tkinter.Button(login,text='登录',command=getusername).pack()

login.mainloop()  # 进入主循环
