from NewsApp.NewsModule import News
from tkinter import *
from PIL import ImageTk,Image
from NewsApp.AssistantModule import Say

newsType = (
    'bitcoin',
    'business headlines',
    'tech headlines',
    'wall street journal',
    'apple headlines',
)

window = Tk()
window.title('News Today')
window.state('zoomed') # full screen
window.minsize(800, 500)

body = Frame(window,bg='white')

speakerIcon = ImageTk.PhotoImage(Image.open('speaker.jpg'))

menu = Frame(body, bg='white', padx=10, pady=10, relief=SOLID, borderwidth=1)
menuCol = Frame(body,bg='white')
c = 0

for type in newsType:
    Button(menuCol,text=type,borderwidth=1,relief=SOLID).grid(row=0,column=c,pady=4)
    c += 1

menuCol.pack(fill=BOTH)
menu.pack(fill=X, side=TOP, pady=5, padx=10)

for news in News(type=newsType[2]).response:
    row = Frame(body,bg='white',padx=10,pady=10,relief=SOLID,borderwidth=1)
    col = Frame(row,bg='white')

    Label(col,text=news['title'], bg='white', font='Arial 16 bold',padx=10).grid(row=0,columnspan=2)

    Label(col,text=news['description'], bg='white', fg='black', font='Arial 12',wraplength=900).grid(stick='w')

    Label(col, text=f"--by {news['author']}", bg='white', fg='black', font='Arial 10 italic').grid(sticky='w')

    Label(col,text="news['urlToImage']").grid(row=0,column=1,rowspan=3)

    Button(col,image=speakerIcon,borderwidth=1,relief=SOLID,command=lambda : Say(news['description'])).grid(sticky='w',pady=5)

    col.grid_columnconfigure(0,weight=1)
    col.grid_columnconfigure(1,weight=1)
    col.pack(fill=BOTH)
    row.pack(fill=X,pady=5,padx=10)

body.pack(fill=BOTH,expand=True)

window.mainloop()