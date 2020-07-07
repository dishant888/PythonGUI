from tkinter import *

expression = ''

def getInput(i):
    global expression
    if i not in ['=','C']:
        if i in ['+','-','*','/','.']:
            if not expression.endswith(('*','+','-','/','.')):
                expression += i
                textBox.set(expression)
        else:
            expression += i
            textBox.set(expression)
    elif i == '=':
        try:
            textBox.set(eval(expression))
            expression = str(eval(expression))
        except Exception:
            textBox.set('Error')
            expression = ''
    else:
        textBox.set('')
        expression = ''

root = Tk()
root.geometry('350x355')
root.title('Calculator')
root.resizable(0,0)

textBox = StringVar()

body = Frame(root,bg='white',pady=5,padx=5)

TopFrame = Frame(body,bg='white',borderwidth=1,relief=SUNKEN)

Entry(TopFrame,font='Arial 26',borderwidth=0,textvariable=textBox).pack(pady=(10,5),padx=5)

TopFrame.pack(fill=X)

BottomFrame = Frame(body,bg='white')

# First row
Button(BottomFrame,text='C',pady=10,padx=70,bg='white',relief=SUNKEN,font='Arial 14 bold',command=lambda: getInput('C')).grid(row=0,columnspan=2)
Button(BottomFrame,text='.',pady=10,padx=40,bg='white',relief=SUNKEN,font='Arial 14 bold',command=lambda: getInput('.')).grid(row=0,column=2)
Button(BottomFrame,text='+',pady=10,padx=40,bg='white',relief=SUNKEN,font='Arial 14 bold',command=lambda: getInput('+')).grid(row=0,column=3)

# Second row
Button(BottomFrame,text='7',pady=10,padx=40,bg='white',relief=SUNKEN,font='Arial 14 bold',command=lambda: getInput('7')).grid(row=1,column=0)
Button(BottomFrame,text='8',pady=10,padx=40,bg='white',relief=SUNKEN,font='Arial 14 bold',command=lambda: getInput('8')).grid(row=1,column=1)
Button(BottomFrame,text='9',pady=10,padx=40,bg='white',relief=SUNKEN,font='Arial 14 bold',command=lambda: getInput('9')).grid(row=1,column=2)
Button(BottomFrame,text='/',pady=10,padx=40,bg='white',relief=SUNKEN,font='Arial 14 bold',command=lambda: getInput('/')).grid(row=1,column=3)

# Third row
Button(BottomFrame,text='4',pady=10,padx=40,bg='white',relief=SUNKEN,font='Arial 14 bold',command=lambda: getInput('4')).grid(row=2,column=0)
Button(BottomFrame,text='5',pady=10,padx=40,bg='white',relief=SUNKEN,font='Arial 14 bold',command=lambda: getInput('5')).grid(row=2,column=1)
Button(BottomFrame,text='6',pady=10,padx=40,bg='white',relief=SUNKEN,font='Arial 14 bold',command=lambda: getInput('6')).grid(row=2,column=2)
Button(BottomFrame,text='X',pady=10,padx=40,bg='white',relief=SUNKEN,font='Arial 14 bold',command=lambda: getInput('*')).grid(row=2,column=3)

# Forth row
Button(BottomFrame,text='1',pady=10,padx=40,bg='white',relief=SUNKEN,font='Arial 14 bold',command=lambda: getInput('1')).grid(row=3,column=0)
Button(BottomFrame,text='2',pady=10,padx=40,bg='white',relief=SUNKEN,font='Arial 14 bold',command=lambda: getInput('2')).grid(row=3,column=1)
Button(BottomFrame,text='3',pady=10,padx=40,bg='white',relief=SUNKEN,font='Arial 14 bold',command=lambda: getInput('3')).grid(row=3,column=2)
Button(BottomFrame,text='-',pady=10,padx=40,bg='white',relief=SUNKEN,font='Arial 14 bold',command=lambda: getInput('-')).grid(row=3,column=3)

# Fifth row
Button(BottomFrame,text='0',pady=10,padx=120,bg='white',relief=SUNKEN,font='Arial 14 bold',command=lambda: getInput('0')).grid(row=4,columnspan=3)
Button(BottomFrame,text='=',pady=10,padx=40,bg='white',relief=SUNKEN,font='Arial 14 bold',command=lambda: getInput('=')).grid(row=4,column=3)

BottomFrame.columnconfigure(0,weight=1)
BottomFrame.columnconfigure(1,weight=1)
BottomFrame.columnconfigure(2,weight=1)
BottomFrame.columnconfigure(3,weight=1)
BottomFrame.columnconfigure(4,weight=1)
BottomFrame.pack(fill=BOTH,expan=TRUE)

body.pack(fill=BOTH,expand=True)

# key Bindings
root.bind('<Key-1>',lambda a: getInput('1'))
root.bind('<Key-2>',lambda a: getInput('2'))
root.bind('<Key-3>',lambda a: getInput('3'))
root.bind('<Key-4>',lambda a: getInput('4'))
root.bind('<Key-5>',lambda a: getInput('5'))
root.bind('<Key-6>',lambda a: getInput('6'))
root.bind('<Key-7>',lambda a: getInput('7'))
root.bind('<Key-8>',lambda a: getInput('8'))
root.bind('<Key-9>',lambda a: getInput('9'))
root.bind('<Key-0>',lambda a: getInput('0'))
root.bind('<Key-0>',lambda a: getInput('0'))
root.bind('<BackSpace>',lambda a: getInput('C'))

root.mainloop()