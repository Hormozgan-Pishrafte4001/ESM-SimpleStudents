import View
import model


def callback1(user_name, u_pass):
    x = model.login(user_name, u_pass)
    if x is True:
        root.destroy()
        # open user panel
    else:
        pass  # show message user password
root = View.LoginView(callback1)
root.mainloop()

