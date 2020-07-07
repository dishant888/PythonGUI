from tkinter import *
from tkinter.ttk import Combobox
from urllib.parse import quote
from requests import get

apiKey = 'ee0e6d36ba66043a05cd'
optionsUrl = f'https://free.currconv.com/api/v7/currencies?apiKey={apiKey}'

# dropdownOptions = tuple(get(optionsUrl).json()['results'].keys())
# print(dropdownOptions)

def convert():
    query = quote(fromCurrency.get()) + '_' + quote(toCurrency.get())
    url = f'https://free.currconv.com/api/v7/convert?q={query}&compact=ultra&apiKey={apiKey}'
    # print(get(url).json())
    rate = get(url).json()[query.upper()]
    Label(col, text='Result :', bg='white').grid(row=4, column=0, pady=10)
    Label(col, text=rate*amount.get(), bg='white').grid(row=4, column=1, pady=10)

root = Tk()
root.geometry('350x200')
root.title('Converter')
root.resizable(0,0)

amount = DoubleVar()
fromCurrency = StringVar()
# fromCurrency.set(dropdownOptions[1])
toCurrency = StringVar()

body = Frame(root,bg='white')

row = Frame(body,pady=5,bg='white')
col = Frame(row,bg='white')

Label(col,text='Amount :',bg='white').grid(pady=5)
Entry(col,borderwidth=1,relief=SOLID,textvariable=amount).grid(row=0,column=1,pady=5)

Label(col,text='From(currency) :',bg='white').grid(row=1,column=0,pady=5)
Entry(col,borderwidth=1,relief=SOLID,textvariable=fromCurrency).grid(row=1,column=1,pady=5)
# optionMenu = Combobox(col,textvariable=fromCurrency)
# optionMenu['values'] = dropdownOptions
# optionMenu.grid(row=1,column=1,pady=5)

Label(col,text='To(currency) :',bg='white').grid(row=2,column=0,pady=5)
Entry(col,borderwidth=1,relief=SOLID,textvariable=toCurrency).grid(row=2,column=1,pady=5)

Button(col,text='Convert',borderwidth=1,relief=SOLID,command=convert).grid(row=3,columnspan=2,pady=10)

col.columnconfigure(0,weight=1)
col.columnconfigure(1,weight=1)
col.pack(fill=X)
row.pack(fill=X)

body.pack(fill=BOTH,expand=True)

root.mainloop()