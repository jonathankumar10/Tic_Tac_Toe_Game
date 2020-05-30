from tkinter import *


root = Tk()

canvas = Canvas(root)
canvas.pack()

frame = Frame(canvas, relief = RIDGE)
frame.grid(row=1, column = 0)

frameTop = Frame(canvas, relief = RIDGE)
frameTop.grid(row =0, column = 0)

root.title("Tic Tac Toe")

title = Label(frameTop, text="Tic Tac Toe", justify=CENTER, font="times 25", bd = 20, fg='Blue', bg='white')
title.grid(row=0,column=0)

text1 = Entry(frame)
title.grid(row=0,column=2)

text2 = Entry(frame)
title.grid(row=1,column=2)

name1 = Label(frame, text="Player 1 : X", font="times 20")
name1.grid(row=1,column=1)


name2 = Label(frame, text="Player 2 : 0", font="times 20")
name2.grid(row=2,column=1)

space1 = Label(frame, text="      ", font="times 20")
space1.grid(row=1,column=2)

space2 = Label(frame, text="      ", font="times 20")
space2.grid(row=2,column=2)

newGame = Button(frame, text="New Game", font="times 20")
newGame.grid(row=1,column=3)

resetGame = Button(frame, text="Reset game", font="times 20")
resetGame.grid(row=2,column=3)

buttons = StringVar()
click = True

playerX = IntVar()
playerO = IntVar()

playerX.set(0)
playerO.set(0)

def checker(buttons):
    global click
    if buttons["text"] == " " and click == True:
        buttons["text"] = "X"
        click = False

    elif buttons["text"] == " " and click == False:
        buttons["text"] = "O"
        click = True

b1 = Button(frame, width = 20, text=" " ,height = 10, command = lambda: checker(b1))
b1.grid(row=3,column=1)

b2 = Button(frame, width = 20, text=" " , height = 10, command = lambda: checker(b2))
b2.grid(row=3,column=2)

b3 = Button(frame, width = 20, text=" " , height = 10, command = lambda: checker(b3))
b3.grid(row=3,column=3)

b4 = Button(frame, width = 20, text=" " , height = 10, command = lambda: checker(b4))
b4.grid(row=4,column=1)

b5 = Button(frame, width = 20, text=" " , height = 10, command = lambda: checker(b5))
b5.grid(row=4,column=2)

b6 = Button(frame, width = 20, text=" " , height = 10, command = lambda: checker(b6))
b6.grid(row=4,column=3)

b7 = Button(frame, width = 20, text=" " , height = 10, command = lambda: checker(b7))
b7.grid(row=5,column=1)

b8 = Button(frame, width = 20, text=" " , height = 10, command = lambda: checker(b8))
b8.grid(row=5,column=2)

b9 = Button(frame, width = 20, text=" " , height = 10, command = lambda: checker(b9))
b9.grid(row=5,column=3)

root.mainloop()