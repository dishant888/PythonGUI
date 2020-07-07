from tkinter import *

def click():
    # print(a.get())
    # print(b.get())
    # sum = a.get() + b.get()
    # Label(root,text=f'Result = {sum}').grid(row=4,columnspan=2)
    c = a.get() + b.get()
    sum.set(c)
    Entry(root,textvariable=sum).grid(row=4,columnspan=2)

root = Tk()
root.geometry('500x500')

# IntVar, StringVar, BooleanVar, DoubleVar
a = IntVar()
b = IntVar()
sum = IntVar()

l = Label(root,text='Program for addition of two numbers',bg='white',font='Arial 14 bold').grid(columnspan=2)

l1 = Label(root,text='Enter first number : ').grid(row=1,column=0)
Entry(root,textvariable=a).grid(row=1,column=1)

l2 = Label(root,text='Enter second number : ').grid(row=2,column=0)
Entry(root,textvariable=b).grid(row=2,column=1)

Button(root,text='Click me',command=click).grid(row=3,columnspan=2)

root.mainloop()