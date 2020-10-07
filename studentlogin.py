from tkinter import *
from playsound import playsound
import os


root = Tk()

root.configure(background="white")
def function1():
    playsound('sound.mp3')

def function6():
    root.destroy()

def attend():
    root.destroy()

root.title("ATTENDANCE MANAGEMENT USING FACE RECOGNITION")

Label(root, text="FACE RECOGNITION ATTENDANCE SYSTEM", font=("times new roman", 20), fg="white", bg="green",
      height=2).grid(row=0, rowspan=2, columnspan=2, sticky=E + W )

Button(root, text="Show your Profile", font=("times new roman", 20), bg="#0D47A1", fg='white', command=function1).grid(
    row=3, columnspan=2, sticky=W + E)

Button(root, text="Attendance Sheet", font=('times new roman', 20), bg="#0D47A1", fg="white", command=attend).grid(
    row=6, columnspan=2, sticky=W + E)

Button(root, text="Exit", font=('times new roman', 20), bg="green", fg="lightblue", command=function6).grid(row=9,
                                                                                                         columnspan=2,
                                                                                                         sticky=E + W)
root.mainloop()