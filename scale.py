from tkinter import *
from tkinter import messagebox

def click():
    # messagebox.showinfo(title='Title here',message=f'Value of scale = {myScale.get()}')
    Label(root,text=f'INR = {int(myScale.get())*76}').pack(pady=20)

root = Tk()
root.geometry('400x200')

myScale = Scale(root,from_=0,to=100,orient=HORIZONTAL,tickinterval=10,width=20,length=300)
myScale.pack()

Button(root,text='Click me!',command=click).pack(pady=20)

root.mainloop()