from tkinter import *

turn = 1

board = [
    '','','',
    '','','',
    '','',''
]

winPattern = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]

def chance(b,i):
    global turn
    turn += 1
    # print(b['text'])
    a = ''
    if turn % 2 == 0:
        if b["text"] == ' ':
            b["text"],a = 'O','O'
            board[i] = 'O'
    else:
        if b["text"] == ' ':
            b["text"],a = 'X','X'
            board[i] = 'X'

    for i in winPattern:
        # i = [0,1,2]
        if board[i[0]] == a and a == board[i[1]] and a == board[i[2]]:
            print('Wins')
            Label(root,text=f'{a} wins').grid(row=3,columnspan=3)
            break

root = Tk()
root.geometry('400x400')
root.resizable(0,0)

b1 = Button(root,text=' ',command= lambda : chance(b1,0),pady=5,padx=5,font='Arial 14 bold')
b1.grid(row=0,column=0)

b2 = Button(root,text=' ',command= lambda : chance(b2,1),pady=5,padx=5,font='Arial 14 bold')
b2.grid(row=0,column=1)

b3 = Button(root,text=' ',command= lambda : chance(b3,2),pady=5,padx=5,font='Arial 14 bold')
b3.grid(row=0,column=2)

b4 = Button(root,text=' ',command= lambda : chance(b4,3),pady=5,padx=5,font='Arial 14 bold')
b4.grid(row=1,column=0)

b5 = Button(root,text=' ',command= lambda : chance(b5,4),pady=5,padx=5,font='Arial 14 bold')
b5.grid(row=1,column=1)

b6 = Button(root,text=' ',command= lambda : chance(b6,5),pady=5,padx=5,font='Arial 14 bold')
b6.grid(row=1,column=2)

b7 = Button(root,text=' ',command= lambda : chance(b7,6),pady=5,padx=5,font='Arial 14 bold')
b7.grid(row=2,column=0)

b8 = Button(root,text=' ',command= lambda : chance(b8,7),pady=5,padx=5,font='Arial 14 bold')
b8.grid(row=2,column=1)

b9 = Button(root,text=' ',command= lambda : chance(b9,8),pady=5,padx=5,font='Arial 14 bold')
b9.grid(row=2,column=2)

root.mainloop()