from tkinter import *

# *****grid for tic tac toe******
root=Tk()
root.geometry("500x500")  # dimension of the grid
root.title("Tic Tac Toe") # title of the grid

# Frame 1 for title
frame1=Frame(root)
frame1.pack()
titleLabel = Label(frame1, text="Tic Tac Toe",font=("Ariel",25),bg="orange")
titleLabel.pack()

# initial state of the board
board = {
         1:" ",2:" ",3:" ",
         4:" ",5:" ",6:" ",
         7:" ",8:" ",9:" "
         }


turn = "X" #initialie turn as X
game_end=False

# Global variables for the win and draw labels
winning_label = None
draw_label = None


def update_board():
    for key in board.keys():
        Buttons[key-1]["text"]=board[key]


# conditon for win

def checkforWin(player):
    # row
    if board[1]==board[2] and board[2]==board[3] and board[3]==player:
        return True
    elif board[4]==board[5] and board[5]==board[6] and board[6]==player:
        return True
    elif board[7]==board[8] and board[8]==board[9] and board[9]==player:
        return True
    # column
    elif board[1]==board[4] and board[4]==board[7] and board[7]==player:
        return True
    elif board[2]==board[5] and board[5]==board[8] and board[8]==player:
        return True
    elif board[3]==board[6] and board[6]==board[9] and board[9]==player:
        return True
    # diagonal
    elif board[1]==board[5] and board[5]==board[9] and board[9]==player:
        return True
    elif board[3]==board[5] and board[5]==board[7] and board[7]==player:
        return True
    else:
        return False
def  checkforDraw():
    for i in board.keys():
        if board[i] == " ":
            return False
    return True

def restart_game():
    global winning_label, draw_label,game_end
    game_end=False
    for button in Buttons:
        button["text"]=" "
    for i in board.keys():
        board[i]=" "
    if winning_label:
        winning_label.destroy()
        winning_label = None
    if draw_label:
        draw_label.destroy()
        draw_label = None
    
# Apply minimax algo to make computer play this game

def minimax(board, isMaximiing):
    if checkforWin("O"):
        return 1
    if checkforWin("X"):
        return -1
    if checkforDraw():
        return 0

    if isMaximiing:
         bestscore=-100

         for keys in board.keys():
            if board[keys] == " ":
                board[keys]="O"
                score=minimax(board,False) # using minimax algo for finding the optimal position
                board[keys]= " "
                if score > bestscore:
                    bestscore = score
         return bestscore
    else:
         bestscore=100

         for keys in board.keys():
            if board[keys] == " ":
                board[keys]="X"
                score=minimax(board,True) # using minimax algo for finding the optimal position
                board[keys]= " "
                if score < bestscore:
                    bestscore = score
         return bestscore

    
def play_computer():
    bestscore=-100
    bestmove=0

    for keys in board.keys():
        if board[keys] == " ":
            board[keys]="O"
            score=minimax(board,False) # using minimax algo for finding the optimal position
            board[keys]= " "
            if score > bestscore:
                bestscore = score
                bestmove=keys
    board[bestmove]="O"
    
# function to toggle between X and O on pressing the button
def play(event):
    global turn,winning_label,draw_label,game_end
    if game_end:
        return
    botton = event.widget
    button= str(botton)
    cliched_btn=button[-1]
    if cliched_btn=="n":
        cliched_btn=1
    else:
        cliched_btn=int(cliched_btn)

    if botton["text"]==" ":
         if turn == "X":
            board[cliched_btn]=turn
            if checkforWin(turn):
                winning_label =Label(frame2, text=f"{turn}, wins the game",bg="red",font="ariel,40")
                winning_label.grid(row=3,column=0,columnspan=3)
                game_end=True
            turn = "O"
            play_computer()
            if checkforWin(turn):
                winning_label =Label(frame2, text=f"{turn}, wins the game",bg="red",font="ariel,40")
                winning_label.grid(row=3,column=0,columnspan=3)
                game_end=True
            update_board()
            turn = "X"
    
         if checkforDraw():
             draw_label =Label(frame2, text=f"Game Draw!",bg="red",font="Ariel,40",width=20)
             draw_label.grid(row=3,column=0,columnspan=3)
             
   

 
# Frame 2 for board
frame2 = Frame(root)
frame2.pack()

# first row
button1 = Button(frame2, text=" ", width = 4 , height=2, font="Ariel, 30", bg = "yellow")
button1.grid(row = 0, column = 0)
button1.bind("<Button-1>",play)

button2 = Button(frame2, text=" ", width = 4 , height=2, font="Ariel, 30",bg = "yellow")
button2.grid(row = 0, column = 1)
button2.bind("<Button-1>",play)

button3 = Button(frame2, text=" ", width = 4 , height=2, font="Ariel, 30",bg = "yellow")
button3.grid(row = 0, column = 2)
button3.bind("<Button-1>",play)

# 2nd row
button4 = Button(frame2, text=" ",  width = 4 , height=2, font="Ariel, 30",bg = "yellow")
button4.grid(row = 1, column = 0)
button4.bind("<Button-1>",play)

button5 = Button(frame2, text=" ", width = 4 , height=2, font="Ariel, 30",bg = "yellow")
button5.grid(row = 1, column = 1)
button5.bind("<Button-1>",play)

button6 = Button(frame2, text=" ", width = 4 , height=2, font="Ariel, 30",bg = "yellow")
button6.grid(row = 1, column = 2)
button6.bind("<Button-1>",play)

# 3rd row
button7 = Button(frame2, text=" ",  width = 4 , height=2, font="Ariel, 30",bg = "yellow")
button7.grid(row = 2, column = 0)
button7.bind("<Button-1>",play)

button8 = Button(frame2, text=" ", width = 4 , height=2, font="Ariel, 30",bg = "yellow")
button8.grid(row = 2, column = 1)
button8.bind("<Button-1>",play)

button9 = Button(frame2, text=" ", width = 4 , height=2, font="Ariel, 30",bg = "yellow")
button9.grid(row = 2, column = 2)
button9.bind("<Button-1>",play)

restart_button= Button(frame2, text="Restart Game",width=12, height=1, font="Ariel, 20",bg="green",relief=RAISED,borderwidth=5,command=restart_game)
restart_button.grid(row=4,column=0,columnspan=3)


Buttons = [button1,button2,button3,button4,button5,button6,button7,button8,button9]

root.mainloop()