from tkinter import *

root = Tk()
root.geometry('500x500')

Entry(root).pack()
# b = Button(root,text='Click me!')
b = [Button()]*16
# print(b)

data = ['7','8','9','+','4','5','6','-','1','2','3','/','.','0','C','*']

k = 0
x,y = 5,55
for i in range(4):
    for j in range(4):
        b[k] = Button(text=data[k],font='Arial 12 bold')
        b[k].place(x=x,y=y,width=100,height=50)
        x += 105
        k += 1
    y += 55
    x = 5

root.mainloop()