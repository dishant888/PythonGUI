from tkinter import *

def update(headingText,contentText):
    heading['text'] = headingText
    content['text'] = contentText

root = Tk()
root.state('zoomed')
root.title('Python Tutorial')

menuBar = Menu(root)

mainMenu = Menu(menuBar)
mainMenu.add_command(label='Introduction',command=lambda:update('Introduction to Python','Content here'))

ifMenu = Menu(menuBar)
ifMenu.add_command(label='Introduction',command=lambda:update('Introduction to Conditional statements','If content here'))
ifMenu.add_command(label='Syntax',command=lambda:update('Syntax for conditional statements','Syntax here'))
ifMenu.add_command(label='Programs',command=lambda :update('Programs for conditional statements','Programs here'))

loopMenu = Menu(menuBar)
loopMenu.add_command(label='Introduction',command=lambda:update('Introduction to loops','Loop content here'))
loopMenu.add_command(label='Types',command=lambda:update('Types of Loop','Types here'))
loopMenu.add_command(label='Syntax',command=lambda:update('Synatax for Loop','Syntax here'))
loopMenu.add_command(label='Programs',command=lambda:update('Programs of loop','Program here'))

mainMenu.add_cascade(label='Conditional Statements',menu=ifMenu)
mainMenu.add_cascade(label='Loop Statements',menu=loopMenu)

body = Frame(root,bg='white')

heading = Label(body,bg='white',font='Arial 16 bold')
heading['text'] = 'Python'
heading.pack(fill=X,pady=10)

content = Label(body,bg='white',font='Arial 12')
content['text'] = 'Welcome to python tutorial'
content.pack(fill=BOTH,expand=True)

body.pack(fill=BOTH,expand=True)

menuBar.add_cascade(label='Content',menu=mainMenu)
root.config(menu=menuBar)
root.mainloop()