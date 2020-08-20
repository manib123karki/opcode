from tkinter import *
import tkinter.messagebox
import pickle
import os
import Login


class User_register:
    def __init__(self, window):
        self.window = window
        self.window.title("REGISTER USER")
        self.window.geometry("600x500")
        self.window.configure(bg="yellow", bd=5)
        self.window.resizable(0,0)

        self.dictcred = {}
        # ============Label

        self.lb_heading = Label(self.window, text="USER REGISTRATION FORM", bg="red",
                                font=("arial", 25, "bold"))
        self.lb_heading.place(x=0, y=0, relwidth=1)

        self.fname_value = StringVar()
        self.lname_value = StringVar()
        self.choose_username_value = StringVar()
        self.rpassword_value = StringVar()
        self.cpassword_value = StringVar()
        self.address_value = StringVar()

        # ===================Frame=========
        self.frame1 = Frame(self.window, bg="yellow")
        self.frame1.place(x=50, y=100)

        self.lb_fname = Label(self.frame1, text="FIRST NAME:",
                              font=("arial", 15, 'bold'), bg="yellow")
        self.lb_fname.grid(row=0, column=0, padx=10, pady=10)

        self.lb_lname = Label(self.frame1, text="LAST NAME:",
                              font=("arial", 15, 'bold'), bg="yellow")
        self.lb_lname.grid(row=1, column=0, padx=10, pady=10)

        self.lb_choose_username = Label(self.frame1, text="CHOOSE USERNAME:",
                                        font=("arial", 15, 'bold'), bg="yellow")
        self.lb_choose_username.grid(row=2, column=0, padx=10, pady=10)

        self.lb_rpassword = Label(self.frame1, text="PASSWORD:",
                                  font=("arial", 15, 'bold'), bg="yellow")
        self.lb_rpassword.grid(row=3, column=0, padx=10, pady=10)

        self.lb_cpassword = Label(self.frame1, text=" CONFIRM PASSWORD:",
                                  font=("arial", 15, 'bold'), bg="yellow")
        self.lb_cpassword.grid(row=4, column=0, padx=10, pady=10)

        self.lb_address = Label(self.frame1, text=" ADDRESS:",
                                font=("arial", 15, 'bold'), bg="yellow")
        self.lb_address.grid(row=5, column=0, padx=10, pady=10)

        # ================Entry
        self.ent_fname = Entry(self.frame1, font=("arial", 15, 'bold'), textvariable=self.fname_value)
        self.ent_fname.grid(row=0, column=1, padx=10, pady=10)

        self.ent_lname = Entry(self.frame1, font=("arial", 15, 'bold'), textvariable=self.lname_value)
        self.ent_lname.grid(row=1, column=1, padx=10, pady=10)

        self.ent_choose_username = Entry(self.frame1, font=("arial", 15, 'bold'),
                                         textvariable=self.choose_username_value)
        self.ent_choose_username.grid(row=2, column=1, padx=10, pady=10)

        self.ent_password = Entry(self.frame1, font=("arial", 15, 'bold'), textvariable=self.rpassword_value)
        self.ent_password.grid(row=3, column=1, padx=10, pady=10)

        self.ent_cpassword = Entry(self.frame1, font=("arial", 15, 'bold'), textvariable=self.cpassword_value, show="*")
        self.ent_cpassword.grid(row=4, column=1, padx=10, pady=10)

        self.ent_address = Entry(self.frame1, font=("arial", 15, 'bold'), textvariable=self.address_value)
        self.ent_address.grid(row=5, column=1, padx=10, pady=10)

        self.btn_submit = Button(self.frame1, text="SUBMIT", bg="green", bd=5, command=self.btn_submit_click)
        self.btn_submit.grid(columnspan=2)

        self.btn_clear = Button(self.frame1, text="CLEAR FORM", bg="green", bd=5, command=self.btn_reset_click)
        self.btn_clear.place(x=290, y=300)

        self.btn_backtolog = Button(self.frame1, text="LOGIN PAGE", bg="green", bd=5, command=self.btn_exit_click)
        self.btn_backtolog.place(x=390, y=300)

    def btn_exit_click(self):
        self.window.withdraw()
        user_window = Toplevel(self.window)
        Login.Login_Form(user_window)

    def btn_submit_click(self):
        self.data_insert()

    def btn_reset_click(self):
        self.ent_fname.delete(0, "end")
        self.ent_lname.delete(0, "end")
        self.ent_address.delete(0, "end")
        self.ent_cpassword.delete(0, "end")
        self.ent_choose_username.delete(0, "end")
        self.ent_password.delete(0, "end")

    def data_insert(self):
        le = os.path.getsize(
            "D:\\Softwarica study material\\Semester 2\\Introduction to "
            "Algorithm\\Coding_and_Algorithms\\Manib_Assignment\\user_log.txt")
        fname = self.ent_fname.get()
        lname = self.ent_lname.get()
        cusername = self.ent_choose_username.get()
        rpassword = self.ent_password.get()
        cpassword = self.ent_cpassword.get()
        address = self.ent_address.get()

        if fname == "" or lname == "" or cusername == "" or rpassword == "" or cpassword == "" or address == "":
            tkinter.messagebox.showinfo("Empty", "Please fill up all details")

        else:
            self.listcred = [cpassword]
            self.listcred1 = [rpassword, fname, lname, address]
            di = {cusername: self.listcred}

            len = os.path.getsize(
                "D:\\Softwarica study material\\Semester 2\\Introduction to "
                "Algorithm\\Coding_and_Algorithms\\Manib_Assignment\\user_log.txt")

            if len > 0:
                f = open("user_log.txt", "rb")
                self.dictcred = pickle.load(f)
                print(self.dictcred)
                for k, p in self.dictcred.items():
                    if k == self.ent_choose_username.get() and k != "":
                        tkinter.messagebox.showinfo("Already exists",
                                                    f"Sorry! Username {k}\n already exists!\n")
                    else:
                        if le > 0:
                            f = open("user_log.txt", "rb+")
                            self.dictcred = pickle.load(f)
                            self.dictcred.update(di)
                            f.seek(0)
                            pickle.dump(self.dictcred, f)
                            tkinter.messagebox.showinfo("Success!", "Your data have been saved successfully")
                            self.window.withdraw()
                            f.close()

            else:
                f = open("user_log.txt", "wb")
                self.dictcred.update(di)
                pickle.dump(self.dictcred, f)
                tkinter.messagebox.showinfo("Success!", "Your data have been saved successfully")
                self.btn_exit_click()
                f.close()
