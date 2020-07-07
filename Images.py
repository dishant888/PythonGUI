from tkinter import *
# install Pillow and Pillow-PIL
from PIL import Image, ImageTk
window = Tk()
window.geometry('360x180')
window.title('Images in GUI')

# png (portable network graphics) can be set directly other formats needs to be opened before setting

# png
# photo = PhotoImage(file='img.png')

# jpeg
photo = ImageTk.PhotoImage(Image.open('images/img.jpg'))

# set image in label
Label(image=photo).pack()

window.mainloop()