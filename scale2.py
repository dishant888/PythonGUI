from tkinter import *

def slide(a):
    amt.set(myScale.get()*76)
    result['text'] = f'INR = {myScale.get()*76}'
    result.pack()
    # Label(root,text=f'INR = {myScale.get() * 76}').pack()

root = Tk()

amt = IntVar()
amt.set(0)
root.geometry('400x250')

myScale = Scale(root,from_=0,to=100,orient=HORIZONTAL,tickinterval=10,width=20,length=300)
myScale.bind('<ButtonRelease>',slide)
myScale.pack(pady=20)

Label(root,text='Amount in INR').pack()
Entry(root,textvariable=amt).pack(pady=20)
result = Label(root)

root.mainloop()