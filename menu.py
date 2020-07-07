from tkinter import *
import tkinter.messagebox as TMsg

def show():
    ans = TMsg.askquestion('title','Are you happy?')
    if ans == 'yes':
        msg = 'Ok you are happy'
    else:
        msg = 'Why you are not happy?'
    TMsg.showinfo('title',msg)
    TMsg.askretrycancel('title','Content here')
    # print('Testing')

root = Tk()

root.geometry('400x400')
menuBar = Menu(root)

m1 = Menu(menuBar)
m1.add_command(label='New',command = show)
m1.add_command(label='Save',command = show)
m1.add_command(label='Close',command = show)

subMenu = Menu(m1)
subMenu.add_command(label='File', command = show)
subMenu.add_command(label='Folder', command = show)
m1.add_cascade(label='Options',menu=subMenu)

# m1.add_separator()

# m1.add_command(label='New1',command = show)
# m1.add_command(label='Add1',command = show)
# m1.add_command(label='Close1',command = show)

m2 = Menu(menuBar)
m2.add_command(label='Cut',command = show)
m2.add_command(label='Copy',command = show)
m2.add_command(label='Paste',command = show)

root.config(menu=menuBar)
menuBar.add_cascade(label='File',menu=m1)
menuBar.add_cascade(label='Edit',menu=m2)

root.mainloop()

# intro
# if statement -> intro, syntax with program
# Loops -> intro, types, syntax with program