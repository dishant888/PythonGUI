from tkinter import *

root = Tk()

root.geometry('500x400')

# pack, grid(rows and col), place
# StrigVar, IntVar, DoubleVar, BooleanVar

def clickEvent():
    print(f"value of username: {uservalue.get()}")
    print(f"value of password: {passwordvalue.get()}")
    # print(f"Sum: {int(passwordvalue.get())+int(uservalue.get())}")

uservalue = StringVar()
passwordvalue = StringVar()

username = Label(root,text='Username').grid() # default (row=0,column=0)
userinput = Entry(root,textvariable=uservalue).grid(row=0,column=1)
password = Label(root,text='Password').grid(row=1)
passwordinput = Entry(root,textvariable=passwordvalue).grid(row=1,column=1)
btn = Button(root,text='Click Me!',command=clickEvent).grid()

root.mainloop()

