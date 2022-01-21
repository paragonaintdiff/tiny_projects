from tkinter import *
import random

GAME_WDITH = 1000
GAME_HEIGHT = 700
SPEED = 100
SPACE_SIZE = 50
BODY_PARTS = 3
SNAKE_COLOR = "blue"
colors = "blue","red","cyan","lightgreen"
RAT_COLOR = random.choice(colors)
BG_COLOR = "black"

class Snake:
    
    def __init__(self):
        
        self.body_size = BODY_PARTS
        self.coordinates = []
        self.squares = []
        
        for i in range(0, BODY_PARTS):
            self.coordinates.append([0,0])
            
        for x,y in self.coordinates:
            
            square = canvas.create_rectangle(x,y,x+SPACE_SIZE,y+SPACE_SIZE,fill=SNAKE_COLOR,tag="snake")
            self.squares.append(square)
        
class Rat:
    
    def __init__(self):
        
        # random x,y
        x = random.randint(0, (GAME_WDITH/SPACE_SIZE)-1)*SPACE_SIZE
        y = random.randint(0, (GAME_HEIGHT/SPACE_SIZE)-1)*SPACE_SIZE
        
        self.coordinates = x,y
        
        canvas.create_oval(x,y,x+SPACE_SIZE,y+SPACE_SIZE,fill=RAT_COLOR,tag="rat")
        
def new_game():
    pass

def next_turn(snake,rat):
    
    x,y = snake.coordinates[0]
    
    if direction == "up":
        y -= SPACE_SIZE
    elif direction == "down":
        y += SPACE_SIZE
    elif direction == "left":
        x -= SPACE_SIZE
    elif direction == "right":
        x += SPACE_SIZE
    
    snake.coordinates.insert(0, (x,y))
    
    square = canvas.create_rectangle(x,y,x+SPACE_SIZE,y+SPACE_SIZE,fill=SNAKE_COLOR,tag="snake")
    
    snake.squares.insert(0, square)
    
    if x == rat.coordinates[0] and y == rat.coordinates[1]:
        
        global score
        
        score += 1
        
        score_label.config(text = f"Score :{score}")
        
        canvas.delete("rat")
        
        rat = Rat()
    
    else:
        
        del snake.coordinates[-1]
    
        canvas.delete(snake.squares[-1])
    
        del snake.squares[-1]
    
    if check_collision(snake):
        game_over()
    
    else: window.after(SPEED,next_turn,snake,rat)
    
def change_direction(new_direction):
    
    global direction
    
    if new_direction == "up":
        if direction != "down":
            direction = new_direction
            print("up")
    
    elif new_direction == "down":
        if direction != "up":
            direction = new_direction
            print("down")
    
    elif new_direction == "left":
        if direction != "right":
            direction = new_direction
            print("left")
            
    elif new_direction == "right":
        if direction != "left":
            direction = new_direction
            print("right")

def check_collision(snake):
    
    x,y = snake.coordinates[0]
    
    if x<0 or x >= GAME_WDITH:
        return True
    
    elif y<0 or y >= GAME_HEIGHT:
        return True
    
    for body_part in snake.coordinates[1:]:
        if x == body_part[0] and y == body_part[1]:
            return True
    
    return False
    
def game_over():
    
    canvas.delete(ALL)
        
    canvas.create_text(canvas.winfo_width()/2,canvas.winfo_height()/2,
                       text="GAME OVER",
                       fill="red",font=("consolas",70))
    
    
    
window = Tk()
window.resizable(False,False)

score = 0
direction = "down"

score_label = Label(window,text=f"Score:{score}",font=("consolas",40))
score_label.pack()

canvas = Canvas(window,width=GAME_WDITH,height=GAME_HEIGHT,bg=BG_COLOR)
canvas.pack()

window.update()

window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width/2)-(window_width/2))
y = int((screen_height/2)-(window_height/2))

window.geometry(f"{window_width}x{window_height}+{x}+{y}")

window.bind("<Up>",lambda x: change_direction("up"))
window.bind("<Down>",lambda x: change_direction("down"))
window.bind("<Left>",lambda x: change_direction("left"))
window.bind("<Right>",lambda x: change_direction("right"))

snake = Snake()
rat = Rat()

next_turn(snake, rat)

window.mainloop()
