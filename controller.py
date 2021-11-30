import View
from model import Core


def callback1(user_name, user_pass):
    core.add_user(user_name, user_pass)
    x = core.login(user_name, user_pass)
    if x is True:
        root.destroy()
        # open user panel
    else:
        root.show_message("your password is Wrong!")  # show message user & password is wrong


core = Core()
root = View.LoginView(callback1)
root.mainloop()
