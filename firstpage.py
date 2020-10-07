from tkinter import *
from tkinter.ttk import *
import os

root = Tk()
def function1():
    os.system("py teacherlogin.py")

def function2():
    os.system("py studentlogin.py")


Label(root, text='Teacher Login', font=(
    'Verdana', 15)).pack(side=TOP, pady=10)

photo = PhotoImage(file="teacher.png")
photo1 = PhotoImage(file="student.png")

Button(root, text='Click Me !', image=photo,command=function1).pack(side=TOP)

Button(root, text='Click Me !', image=photo1,command=function2).pack(side=TOP)

mainloop() 