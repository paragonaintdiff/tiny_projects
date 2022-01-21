from tkinter import *

def button_press(num):
    
    global eq_text
    
    eq_text = eq_text + str(num)
    ui_text.set(eq_text)

def equals():
    
    global eq_text
    
    try:
        
        result = str(eval(eq_text))
        ui_text.set(result)
    
        eq_text = result
    
    except ZeroDivisionError:
        ui_text.set("Zero Divison Error")
        eq_text = ""
        
    except SyntaxError:
        ui_text.set("Syntax Error")
        eq_text = ""

def clear():
    
    global eq_text
    
    ui_text.set("")
    eq_text=""

window = Tk()

window.title("My Calculator")
window.config(background="grey")
window.geometry("500x500")

eq_text = ""

ui_text = StringVar()

ui_label = Label(window,textvariable=ui_text,font=("consolas",20),fg="cyan",
                 bg="black",width=24,height=2)
ui_label.pack()

btn_frame = Frame(window)
btn_frame.pack()

btn_1 = Button(btn_frame,text=1,width=9,height=4,font=50,fg="black",bg="orange",
               command = lambda: button_press(1))
btn_1.grid(row=0,column=0)
btn_2 = Button(btn_frame,text=2,width=9,height=4,font=50,fg="black",bg="orange",
               command = lambda: button_press(2))
btn_2.grid(row=0,column=1)
btn_3 = Button(btn_frame,text=3,width=9,height=4,font=50,fg="black",bg="orange",
               command = lambda: button_press(3))
btn_3.grid(row=0,column=2)
btn_4 = Button(btn_frame,text=4,width=9,height=4,font=50,fg="black",bg="orange",
               command = lambda: button_press(4))
btn_4.grid(row=1,column=0)
btn_5 = Button(btn_frame,text=5,width=9,height=4,font=50,fg="black",bg="orange",
               command = lambda: button_press(5))
btn_5.grid(row=1,column=1)
btn_6 = Button(btn_frame,text=6,width=9,height=4,font=50,fg="black",bg="orange",
               command = lambda: button_press(6))
btn_6.grid(row=1,column=2)
btn_7 = Button(btn_frame,text=7,width=9,height=4,font=50,fg="black",bg="orange",
               command = lambda: button_press(7))
btn_7.grid(row=2,column=0)
btn_8 = Button(btn_frame,text=8,width=9,height=4,font=50,fg="black",bg="orange",
               command = lambda: button_press(8))
btn_8.grid(row=2,column=1)
btn_9 = Button(btn_frame,text=9,width=9,height=4,font=50,fg="black",bg="orange",
               command = lambda: button_press(9))
btn_9.grid(row=2,column=2)
btn_0 = Button(btn_frame,text=0,width=9,height=4,font=50,fg="black",bg="orange",
               command = lambda: button_press(0))
btn_0.grid(row=3,column=0)
plus = Button(btn_frame,text="+",width=9,height=4,font=50,fg="black",bg="darkorange",
               command = lambda: button_press("+"))
plus.grid(row=0,column=3)
minus = Button(btn_frame,text="-",width=9,height=4,font=50,fg="black",bg="darkorange",
               command = lambda: button_press("-"))
minus.grid(row=1,column=3)
multiply = Button(btn_frame,text="*",width=9,height=4,font=50,fg="black",bg="darkorange",
               command = lambda: button_press("*"))
multiply.grid(row=2,column=3)
divide = Button(btn_frame,text="/",width=9,height=4,font=50,fg="black",bg="darkorange",
               command = lambda: button_press("/"))
divide.grid(row=3,column=3)
equal = Button(btn_frame,text="=",width=9,height=4,font=50,fg="black",bg="darkorange",
               command = equals)
equal.grid(row=3,column=2)
decimal = Button(btn_frame,text=".",width=9,height=4,font=50,fg="black",bg="darkorange",
               command = lambda: button_press("."))
decimal.grid(row=3,column=1)
clear_btn = Button(window,text="CLEAR",width=15,height=2,font=50,fg="black",bg="red",
               command = clear)
clear_btn.pack()


window.mainloop()