from tkinter import *

window = Tk()
window.geometry('800x500')

# bg = background
# fg = foreground
# relief = style of border (RIDGE, SUNKEN, GROOVE, RAISED, SOLID, FLAT)
# padx = padding x
# pady = padding y

# method of pack (Side, Fill, padx, pady, anchor)
# side = LEFT, RIGHT, TOP, BOTTOM
# fill = X, Y (full width)
# anchor = ne, nw, n, e (directions NorthWest, NortEast etc)

Label(window,text='Lorem Ipsum is simply dummy text of the printing and\n typesetting industry. Lorem Ipsum has been the industry\'s standard\n dummy text ever since the 1500s, when an unknown printer took a galley\n of type and scrambled it to make a type specimen book. It has\n survived not only five centuries, but also the leap into\n electronic typesetting, remaining essentially unchanged. It was \npopularised in the 1960s with the release of Letraset sheets\n containing Lorem Ipsum passages, and more recently with desktop \npublishing software like Aldus PageMaker including versions of Lorem\n Ipsum.',bg='grey',fg='white',font='arial 16 italic',pady='30',borderwidth=13,relief=RAISED).pack(padx=200)

window.mainloop()