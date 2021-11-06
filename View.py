from tkinter import Tk, Button, Entry, Label


class LoginView(Tk):
    def __init__(self):
        super(LoginView, self).__init__()
        x = self.winfo_screenwidth()
        self.geometry(f"{x}x200")
        b = Button(self, text="login")
        b.grid(row=3, column=2)
        user = Entry(self)
        user.grid(row=1, column=2)
        pass_ = Entry(self)
        pass_.grid(row=2, column=2)
        lbl_user = Label(self, text="user")
        lbl_user.grid(row=1, column=1)
        lbl_pass = Label(self, text="pass")
        lbl_pass.grid(row=2, column=1)
        lbl_hm = Label(self, text="HIDDEN MASSAGE")
        lbl_hm.grid(column=4, row=4)


root = LoginView()
root2 = LoginView()
root.mainloop()
