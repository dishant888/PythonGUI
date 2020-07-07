from tkinter import *

root = Tk()

# ch = int(input('Enter height: '))
# cw = int(input('Enter width: '))

# root.geometry(f'{cw}x{ch}')

root.geometry(f'800x900')
root.title('My canvas')

canvas = Canvas(root,width=900,height=800)
canvas.create_line(5,5,5,100,fill='red')
canvas.create_line(5,5,100,5,fill='red')
canvas.create_line(100,5,100,100,fill='red')
canvas.create_line(100,100,5,100,fill='red')

canvas.create_rectangle(0,150,300,200,fill='green')

canvas.create_oval(244,133,144,255,fill='blue')

canvas.create_text(195,190,text='Hello')

canvas.pack()

root.mainloop()