from tkinter import *
from pygame import mixer

def show1(a):
    # print(a)
    root.configure(bg='blue')

def show2(a):
    # print(a)
    root.configure(bg='red')

def show3(a):
    # print(a)
    root.configure(bg='green')

def play1(a):
    mixer.init()
    mixer.music.load('./music/song.mp3')
    mixer.music.play()

def pause1(a):
    mixer.music.pause()

root = Tk()
root.geometry('400x400')
root.resizable(0,0)

b1 = Button(root,text='Button')

# Clik events

# b1.config(command=show)
# b1.bind('<Double-1>',show)

# b1.bind('<Button-1>',lambda a: root.configure(bg='green'))
# b1.bind('<Button-2>',lambda a: root.configure(bg='red'))
# b1.bind('<Button-3>',lambda a: root.configure(bg='blue'))

# b1.bind('<Double-1>',lambda a: root.configure(bg='green'))
# b1.bind('<Double-2>',lambda a: root.configure(bg='red'))
# b1.bind('<Double-3>',lambda a: root.configure(bg='blue'))

# b1.bind('<Button-1>',show1)

# b1.bind('<Button-2>',show2)
# b1.bind('<Button-3>',show3)

# Enter and leave events

# b1.bind('<Enter>',lambda a: root.configure(bg='green'))
# b1.bind('<Leave>',lambda a: root.configure(bg='red'))

# Events with root

# root.bind('<F1>',lambda a: root.configure(bg='red'))
# root.bind('<F2>',lambda a: root.configure(bg='blue'))
# root.bind('<F3>',lambda a: root.configure(bg='green'))
# root.bind('<Delete>',lambda a: root.configure(bg='white'))
# root.bind('<Key-a>',lambda a: root.configure(bg='black'))
# root.bind('<Key-1>',lambda a: root.configure(bg='yellow'))
# root.bind('<Shift-Up>',lambda a: root.configure(bg='pink'))
# root.bind('<Up>',lambda a: root.configure(bg='grey'))

# b1.bind('<Button>',lambda a: root.configure(bg='brown'))
# b1.bind('<ButtonRelease>',lambda a: root.configure(bg='blue'))

# e1 = Entry(root)
# e1.bind('<FocusIn>',lambda a: root.configure(bg='black'))
# e1.bind('<FocusOut>',lambda a: root.configure(bg='white'))
# e1.pack()
# Entry(root).pack()

e1 = Entry(root)
e1.bind('<FocusIn>',play1)
e1.bind('<FocusOut>',pause1)
e1.pack()
Entry(root).pack()

# b1.pack()

root.mainloop()