from tkinter import *
import random

def next_turn(row,column):
    
    global player
    
    if player == players[0] and check_winner() is False:
            
        buttons[row][column]["text"] = player
                
        if check_winner() is False:
            
            player = players[1]
            turn_label.config(text=player + " turn")
        
        elif check_winner() is True:
            
            turn_label.config(text=players[0] + " wins")
        
        elif check_winner() == "Ties":
            
            turn_label.config(text="Tie")
    else:
        
        buttons[row][column]["text"] = player
                
        if check_winner() is False:
            
            player = players[0]
            turn_label.config(text=player + " turn")
        
        elif check_winner() is True:
            
            turn_label.config(text=players[1] + " wins")
        
        elif check_winner() == "Ties":
            
            turn_label.config(text="Tie!")
        
def check_winner():
    
    for row in range(3):
        
        if buttons[row][0]["text"] == buttons[row][1]["text"] == buttons[row][2]["text"] != "":
            buttons[row][0].config(bg="lightgreen")
            buttons[row][1].config(bg="lightgreen")
            buttons[row][2].config(bg="lightgreen")
            return True
    
    for column in range(3):
        
        if buttons[0][column]["text"] == buttons[1][column]["text"] == buttons[2][column]["text"] != "":
            buttons[0][column].config(bg="lightgreen")
            buttons[1][column].config(bg="lightgreen")
            buttons[2][column].config(bg="lightgreen")
            return True 
    
    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != "":
        buttons[0][0].config(bg="lightgreen")
        buttons[1][1].config(bg="lightgreen")
        buttons[2][2].config(bg="lightgreen")
        return True
    
    elif buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != "":
        buttons[0][2].config(bg="lightgreen")
        buttons[1][1].config(bg="lightgreen")
        buttons[2][0].config(bg="lightgreen")
        return True
    
    elif empty_space() is False:
        
        for row in range(3):
            for column in range(3):
                
                buttons[row][column].config(bg="yellow")
                
        return "Ties"
    
    else:
        
        return False
        
def empty_space():
    
    spaces = 9
    
    for row in range(3):
        for column in range(3):
            if buttons[row][column]["text"] != "":
                spaces-=1

    if spaces == 0:
        return False

    else:
        return True

def new_game():
    
    global player
    
    player = random.choice(players)
    turn_label.config(text=player + " turn")
    
    for row in range(3):
        for column in range(3):
            
            buttons[row][column].config(text="",bg="cyan")
            
            

window = Tk()
window.title("Tic,Tac,Toe")

players = ["x","o"]
player = random.choice(players)

buttons = [[0,0,0],
           [0,0,0],
           [0,0,0]]

turn_label = Label(window,text=player+" turn",font=("consolas",40))
turn_label.pack(side="top")

reset_btn = Button(window,text="Restart",command=new_game,font=("consolas",20))
reset_btn.pack(side="top")

frame = Frame(window)
frame.pack()

# bg_colors = "pink","lightblue","cyan","lightyellow","purple","orange"

for row in range(3):
    for column in range(3):
        
        # bg_color = random.choice(bg_colors)
        
        buttons[row][column] = Button(frame,text="",font=("consolas",40),width=5,height=2,
                                      bg = "cyan",
                                      command = lambda row=row,column=column : next_turn(row,column))
        
        buttons[row][column].grid(row=row,column=column)

window.mainloop()