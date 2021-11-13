from tkinter import Tk, Button, Entry, Label

class LoginView(Tk):
    def __init__(self, callback1):
        super(LoginView, self).__init__()
        self.callback1 = callback1
        self.geometry("300x300+550+150")
        b = Button(self, text="login" , command= self.login_callback)
        b.grid(row=3, column=2)
        self.user = user = Entry(self)
        user.grid(row=1, column=2)
        self.pass_ = pass_ = Entry(self)
        pass_.grid(row=2, column=2)
        lbl_user = Label(self, text="user")
        lbl_user.grid(row=1, column=1)
        lbl_pass = Label(self, text="pass")
        lbl_pass.grid(row=2, column=1)
        lbl_hm = Label(self, text="HIDDEN MESSAGE")
        lbl_hm.grid(column=2, row=4)
    def login_callback(self):
        u = self.user.get()
        p = self.pass_.get()
        self.callback1(u, p)


