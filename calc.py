from tkinter import *

expression = ''

def getInput(a):
    global expression
    if a not in ['C','=']:
        expression += a
        t.set(expression)
    elif a == '=':
        t.set(eval(expression))
        expression = str(eval(expression))
    else:
        t.set('')
        expression = ''

root = Tk()

t = StringVar()

root.title('Calculator')
root.configure(bg='black')
root.geometry('425x330')
root.resizable(0,0)

E1 = Entry(root,font='Arial 15 bold',justify='right',textvariable=t)
E1.place(x=0,y=0,width=425,height=50)

b1 = Button(root,text='7',font='Arial 12 bold',bg='grey',activeforeground='red')
b1.place(x=5,y=55,width=100,height=50)
b1.configure(command = lambda : getInput('7'))

b2 = Button(root,text='8',font='Arial 12 bold',bg='grey',activeforeground='red')
b2.place(x=110,y=55,width=100,height=50)
b2.configure(command = lambda : getInput('8'))

b3 = Button(root,text='9',font='Arial 12 bold',bg='grey',activeforeground='red')
b3.place(x=215,y=55,width=100,height=50)
b3.configure(command = lambda : getInput('9'))

b4 = Button(root,text='+',font='Arial 12 bold',bg='grey',activeforeground='red')
b4.place(x=320,y=55,width=100,height=50)
b4.configure(command = lambda : getInput('+'))

b5 = Button(root,text='4',font='Arial 12 bold',bg='grey',activeforeground='red')
b5.place(x=5,y=110,width=100,height=50)
b5.configure(command = lambda : getInput('4'))

b6 = Button(root,text='5',font='Arial 12 bold',bg='grey',activeforeground='red')
b6.place(x=110,y=110,width=100,height=50)
b6.configure(command = lambda : getInput('5'))

b7 = Button(root,text='6',font='Arial 12 bold',bg='grey',activeforeground='red')
b7.place(x=215,y=110,width=100,height=50)
b7.configure(command = lambda : getInput('6'))

b8 = Button(root,text='-',font='Arial 12 bold',bg='grey',activeforeground='red')
b8.place(x=320,y=110,width=100,height=50)
b8.configure(command = lambda : getInput('-'))

b9 = Button(root,text='1',font='Arial 12 bold',bg='grey',activeforeground='red')
b9.place(x=5,y=165,width=100,height=50)
b9.configure(command = lambda : getInput('1'))

b10 = Button(root,text='2',font='Arial 12 bold',bg='grey',activeforeground='red')
b10.place(x=110,y=165,width=100,height=50)
b10.configure(command = lambda : getInput('2'))

b11 = Button(root,text='3',font='Arial 12 bold',bg='grey',activeforeground='red')
b11.place(x=215,y=165,width=100,height=50)
b11.configure(command = lambda : getInput('3'))

b12 = Button(root,text='/',font='Arial 12 bold',bg='grey',activeforeground='red')
b12.place(x=320,y=165,width=100,height=50)
b12.configure(command = lambda : getInput('/'))

b13 = Button(root,text='.',font='Arial 12 bold',bg='grey',activeforeground='red')
b13.place(x=5,y=220,width=100,height=50)
b13.configure(command = lambda : getInput('.'))

b14 = Button(root,text='0',font='Arial 12 bold',bg='grey',activeforeground='red')
b14.place(x=110,y=220,width=100,height=50)
b14.configure(command = lambda : getInput('0'))

b15 = Button(root,text='C',font='Arial 12 bold',bg='grey',activeforeground='red')
b15.place(x=215,y=220,width=100,height=50)
b15.configure(command = lambda : getInput('C'))

b16 = Button(root,text='X',font='Arial 12 bold',bg='grey',activeforeground='red')
b16.place(x=320,y=220,width=100,height=50)
b16.configure(command = lambda : getInput('X'))

b17 = Button(root,text='=',font='Arial 12 bold',bg='grey',activeforeground='red')
b17.place(x=5,y=275,width=415,height=50)
b17.configure(command = lambda : getInput('='))

root.mainloop()