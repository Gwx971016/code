# 初始化
import tkinter as tk
import tkinter.messagebox
import pickle

window = tk.Tk()

# 登陆界面
window.title('登录界面~')
window.geometry('400x300')
tk.Label(window, text='用户名~：').place(x=100, y=100)
tk.Label(window, text='密码~：').place(x=100, y=140)

var_usr_name = tk.StringVar()
enter_usr_name = tk.Entry(window, textvariable=var_usr_name)
enter_usr_name.place(x=160, y=100)

var_usr_pwd = tk.StringVar()
enter_usr_pwd = tk.Entry(window, textvariable=var_usr_pwd, show='*')
enter_usr_pwd.place(x=160, y=140)


# 登录
def usr_log_in():
    # 输入框内容
    usr_name = var_usr_name.get()
    usr_pwd = var_usr_pwd.get()
    try:
        with open('usr_info.pickle', 'rb') as usr_file:
            usrs_info = pickle.load(usr_file)
    except:
        with open('usr_info.pickle', 'wb') as usr_file:
            usrs_info = {'admin': 'admin'}
            pickle.dump(usrs_info, usr_file)

    # 判断用户输入
    if usr_name in usrs_info:
        if usr_pwd == usrs_info[usr_name]:
            tk.messagebox.showinfo(title='Welcome！', message='Hi~ o(*￣▽￣*)ブ，登录成功啦~')
        else:
            tk.messagebox.showerror(message='emmm...账号不存在，请检查输入~ 未注册请先注册哦~')

    # 用户名 & 密码不能为空
    elif usr_name == '' or usr_pwd == '':
        tk.messagebox.showerror(message='用户名和密码不能为空哦~')


def usr_sign_quit():
    window.destroy()


def usr_sign_up():
    def signtowcg():
        NewName = new_name.get()
        NewPwd = new_pwd.get()
        ConfirPwd = pwd_comfirm.get()
        try:
            with open('usr_info.pickle', 'rb') as usr_file:
                exist_usr_info = pickle.load(usr_file)
        except FileNotFoundError:
            exist_usr_info = {}
        if NewName in exist_usr_info:
            tk.messagebox.showerror(message='用户名被别人占用啦！')
        elif NewName == '' and NewPwd == '':
            tk.messagebox.showerror(message='用户名和密码不能为空哦~')
        elif NewPwd != ConfirPwd:
            tk.messagebox.showerror(message='emmm...密码前后不一致...')
        else:
            exist_usr_info[NewName] = NewPwd
            with open('usr_info.pickle', 'wb') as usr_file:
                pickle.dump(exist_usr_info, usr_file)
                tk.messagebox.showinfo(message='注册成功啦！o(*￣▽￣*)ブ')
                window_sign_up.destroy()

    # 新建注册窗口
    window_sign_up = tk.Toplevel(window)
    window_sign_up.geometry('400x300')
    window_sign_up.title('注册界面~')

    # 注册编辑框
    new_name = tk.StringVar()
    new_pwd = tk.StringVar()
    pwd_comfirm = tk.StringVar()

    tk.Label(window_sign_up, text='用户名~：').place(x=90, y=50)
    tk.Entry(window_sign_up, textvariable=new_name).place(x=160, y=50)

    tk.Label(window_sign_up, text='密码~：').place(x=90, y=100)
    tk.Entry(window_sign_up, textvariable=new_pwd, show='*').place(x=160, y=100)

    tk.Label(window_sign_up, text='确认密码~：').place(x=90, y=150)
    tk.Entry(window_sign_up, textvariable=pwd_comfirm, show='*').place(x=160, y=150)

    # 确认注册
    bt_confirm = tk.Button(window_sign_up, text='确定~', command=signtowcg).place(x=180, y=220)


# 登录 注册按钮
bt_login = tk.Button(window, text='登录~', command=usr_log_in)
bt_login.place(x=120, y=230)

bt_signup = tk.Button(window, text='注册~', command=usr_sign_up)
bt_signup.place(x=190, y=230)

bt_logquit = tk.Button(window, text='退出~', command=usr_sign_quit)
bt_logquit.place(x=260, y=230)

window.mainloop()
