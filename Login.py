from tkinter import *
import Register
import tkinter.messagebox
import os
import pickle
import Welcome


class Login_Form:
    def __init__(self, window):
        self.window = window
        self.window.title("User login")
        self.window.geometry("600x350")
        self.window.configure(bg="yellow", bd=5)
        self.window.resizable(0, 0)

        self.loaddict = {}

        # ===================label heading===================
        self.lb_heading = Label(self.window, text="LOGIN SYSTEM", bg='red', fg='white',
                                font=("times new roman", 30, "bold"))
        self.lb_heading.place(x=0, y=0, relwidth=1)

        # ==========================Frame====================
        self.frame1 = Frame(self.window, bg="yellow")
        self.frame1.place(x=35, y=100)

        self.lb_username = Label(self.frame1, text="USERNAME:",
                                 font=("arial", 20, 'bold'), bg="yellow", fg="black")
        self.lb_username.grid(row=0, column=0, padx=10, pady=10)

        # ================Entry
        self.ent_username = Entry(self.frame1, bd=5, relief=RIDGE, font=("arial", 20, 'bold'))
        self.ent_username.grid(row=0, column=1, padx=10, pady=10)

        self.lb_password = Label(self.frame1, text="PASSWORD:",
                                 font=("arial", 20, 'bold'), bg="yellow", fg="black")
        self.lb_password.grid(row=1, column=0, padx=10, pady=10)

        # ================Entry
        self.ent_password = Entry(self.frame1, bd=5, relief=RIDGE, font=("arial", 20, 'bold'), show="*")
        self.ent_password.grid(row=1, column=1, padx=10, pady=10)

        # ==================button login
        self.btn_register = Button(self.frame1, text='REGISTER', fg="white", bg="green", bd="5",
                                   font=("arial", 10, "bold"),
                                   command=self.btn_register_click)
        self.btn_register.place(x=300, y=128)

        self.btn_login = Button(self.frame1, text="LOGIN", fg="white", bg="green", bd="5",
                                font=("arial", 10, "bold"), command=self.btn_login_click)
        self.btn_login.grid(columnspan=2)

        self.btn_clear = Button(self.frame1, text="CLEAR FORM", fg="white", bg="green", bd="5",
                                font=("arial", 10, "bold"), command=self.btn_reset_click)
        self.btn_clear.place(x=395, y=128)

    def current_user(self):
        self.ent_username.get()

    def btn_exit_click(self):
        self.window.destroy()

    def btn_register_click(self):
        wn = Tk()
        Register.User_register(wn)
        # self.window.withdraw()
        # user_window = Toplevel(self.window)
        # register_page.User_register(user_window)

    def btn_login_click(self):
        self.load()

    def btn_reset_click(self):
        self.ent_username.delete(0, "end")
        self.ent_password.delete(0, "end")

    def btn_login_success(self):
        self.window.withdraw()
        wn = Toplevel(self.window)
        Welcome.welcomelog(wn)
        wn.mainloop()

    def load(self):
        len = os.path.getsize(
            "D:\\Softwarica study material\\Semester 2\\Introduction to "
            "Algorithm\\Coding_and_Algorithms\\Manib_Assignment\\user_log.txt")

        if len > 0:
            f = open("user_log.txt", "rb")
            self.dictcred = pickle.load(f)
            # print(self.dictcred)
            for k, p in self.dictcred.items():
                if k == self.ent_username.get() and k != "":
                    # print(k, p)
                    for lis in p:

                        if lis == self.ent_password.get() and lis != "":
                            tkinter.messagebox.showinfo("Login Success",
                                                        f"Congratulations! {k}\n You have been logged in successfully!\n")
                            self.btn_login_success()
                            self.btn_exit_click()
                            return

                elif self.ent_password.get() == "" or self.ent_username.get() == "":
                    tkinter.messagebox.showinfo("empty", "Username or Password can not be empty ")
                    return
            else:
                tkinter.messagebox.showerror("login failed", "Username or password invalid")


def win():
    window = Tk()
    Login_Form(window)
    window.mainloop()


if __name__ == '__main__':
    win()
