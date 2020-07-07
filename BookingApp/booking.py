from tkinter import *

def submit():
    Label(col,text=name.get(),bg='white').grid(columnspan=2)
    Label(col,text=age.get(),bg='white').grid(columnspan=2)
    Label(col,text=gender.get(),bg='white').grid(columnspan=2)
    Label(col,text=payment.get(),bg='white').grid(columnspan=2)

root = Tk()

root.geometry('250x300')
root.title('Booking App')

body = Frame(root,bg='white')

name = StringVar()
age = IntVar()
gender = StringVar()
payment = StringVar()

row = Frame(body,pady=5,bg='white')
col = Frame(row,bg='white')

Label(col,text='Name :',bg='white').grid(pady=5)
Entry(col,borderwidth=1,relief=SOLID,textvariable=name).grid(row=0,column=1,pady=5)

Label(col,text='Age :',bg='white').grid(row=1,column=0,pady=5)
Entry(col,borderwidth=1,relief=SOLID,textvariable=age).grid(row=1,column=1,pady=5)

Label(col,text='Gender :',bg='white').grid(row=2,column=0,pady=5)
Entry(col,borderwidth=1,relief=SOLID,textvariable=gender).grid(row=2,column=1,pady=5)

Label(col,text='Payment :',bg='white').grid(row=3,column=0,pady=5)
Entry(col,borderwidth=1,relief=SOLID,textvariable=payment).grid(row=3,column=1,pady=5)

Button(col,text='Submit',borderwidth=1,relief=SOLID,command=submit).grid(row=4,columnspan=2,pady=5)

col.columnconfigure(0,weight=1)
col.columnconfigure(1,weight=1)
col.pack(fill=X)
row.pack(fill=X)

body.pack(fill=BOTH,expand=True)

root.mainloop()