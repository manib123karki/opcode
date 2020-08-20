from tkinter import *
import Login
from PIL import ImageTk, Image
import PIL


class welcomelog:
    def __init__(self, window):
        self.window = window
        self.window.configure(bg="white", bd=10)
        self.window.title("Welcome page!")
        self.window.geometry("600x600+0+0")

        # ===============label=================
        self.lb_welhead = Label(self.window, text="YOU ARE WELCOME", bd=5,
                                relief=GROOVE,
                                font=("times new roman", 40, "bold"), bg="red", fg="white")
        self.lb_welhead.place(x=0, y=0, relwidth=1)

        # ==============frame==================
        self.framewel = Frame(self.window, bg="yellow", bd=5, relief=GROOVE)
        self.framewel.place(x=10, y=85, width=560, height=490)

        self.btn_exit = Button(self.framewel, text="EXIT", bd=5, fg="red", bg="light grey",
                               font=("arial", 10, "bold"), command=self.btn_exit_click)
        self.btn_exit.place(x=240, y=310, width=80, height=40)

        self.image = ImageTk.PhotoImage(Image.open(
            "D:\\Softwarica study material\\Semester 2\\Introduction to "
            "Algorithm\\Coding_and_Algorithms\\Manib_Assignment\\businessman.png"))
        self.image_panel = Label(self.framewel, image=self.image, bg="yellow")
        self.image_panel.place(x=150, y=20)

    def btn_exit_click(self):
        self.window.destroy()
