from tkinter import *
from tkinter import messagebox
import datetime

def hello():
    # messagebox.showinfo("Information","Hello my name is dishant")
    # messagebox.showwarning("Information","Hello my name is dishant")
    # messagebox.showerror("Information","Hello my name is dishant")
    # messagebox.askquestion("Information","Hello my name is dishant")
    print(messagebox.askokcancel("Information","Hello my name is dishant"))

root = Tk()
root.geometry('500x400')

time = datetime.datetime.now().strftime('%H:%M:%S')
day = datetime.datetime.now().day

f1 = Frame(root,bg='red',borderwidth=2,relief=SOLID)
l1 = Label(f1,text='Label 1',padx=50,pady=50).pack(pady=20)
btn1 = Button(f1,bg='white',borderwidth=1,relief=SOLID,text='Click me!',command=hello).pack(pady=0)
f1.pack(side=LEFT,fill=Y)

f4 = Frame(root,bg='red',borderwidth=2,relief=SOLID)
l4 = Label(f4,text='Label 1',padx=10,pady=20).pack(pady=150)
f4.pack(side=RIGHT,fill=Y)

f2 = Frame(root,bg='green',borderwidth=2,relief=SOLID)
l2 = Label(f2,text=time,font='arial 18 bold').pack()
f2.pack(side=TOP,fill=X)

f3 = Frame(root,bg='green',borderwidth=2,relief=SOLID)
l3 = Label(f3,text=day,font='arial 18 bold').pack()
f3.pack(side=BOTTOM,fill=X)

root.mainloop()