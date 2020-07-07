from tkinter import *
root = Tk()
root.geometry('600x400') # Initialize size
root.minsize(100,100) # width, height
root.maxsize(700,300) # width, height
root.title('Window title') # window title

Label(root,text='Python GUI').pack()

root.mainloop() # shows window until we exit
print('My name is dishant') # will run after mainloop