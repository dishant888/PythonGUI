from tkinter import *

def fact():
    f = 1
    for i in range(1,num.get()+1):
        f *= i
    # Label(root,text=f'Result = {f}').pack()
    ans.set(f)

root = Tk()

root.geometry('400x400')
root.title('Factorial')

num = IntVar()
ans = IntVar()

Label(root,text='Enter Number: ').pack()
Entry(root,textvariable=num).pack()

Button(root,text='Calculate',command=fact).pack()

Entry(root,textvariable=ans).pack()

root.mainloop()