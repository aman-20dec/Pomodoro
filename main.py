from cgitb import text
from curses import window
from itertools import count
from math import floor

from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 1
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    timer_lbl.config(text="TIMER", fg= GREEN)
    global reps
    reps = 0
    create_canvas_text(0)
    canvas.itemconfig(timer_text, text="00:00" )
    
# ---------------------------- TIMER MECHANISM ------------------------------- # 

def pomodoro_loop():
    global reps 
    create_canvas_text(floor(reps/2))
    reps += 1
        
    if reps % 8 == 0:
        timer_lbl.config(text="BREAK", fg= PINK)
        count_down(LONG_BREAK_MIN * 15) 
        reps =0
        
    elif reps % 2 == 0:
        timer_lbl.config(text="BREAK", fg= RED)
        count_down(SHORT_BREAK_MIN * 5 )
    else:
        timer_lbl.config(text="WORK", fg= GREEN)
        count_down(WORK_MIN * 10)

        
    # call reset


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    
    minute = floor(count / 60)
    seconds = count % 60
    canvas.itemconfig(timer_text, text=f"{minute:02d}:{seconds:02d}" )
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        pomodoro_loop()
       
        
# ---------------------------- UI SETUP ------------------------------- #
def create_canvas_text(number):
    chk_text =""
    for num in range(0,number):
        chk_text += "✔"
    
    check_lbl.config(text=chk_text)


def btn_start_click():
    pomodoro_loop()


window = Tk()
window.title("Pomodoro Stopwatch")
window.config(padx=100, pady=50, bg= YELLOW)

tom_photo = PhotoImage(file="tomato.png")

canvas = Canvas(width=202, height= 224, bg= YELLOW, highlightbackground=YELLOW)
canvas.create_image(103, 112, image= tom_photo)
timer_text = canvas.create_text(103,135, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(row=1, column=1)


timer_lbl = Label(text="Timer", font=(FONT_NAME, 35 ), bg=YELLOW, fg= GREEN)
timer_lbl.grid(row=0, column=1)



start_btn = Button(text="Start", highlightbackground=YELLOW, command= btn_start_click)
start_btn.grid(row=2, column=0)

reset_btn = Button(text="Reset", highlightbackground=YELLOW, command=reset_timer)
reset_btn.grid(row=2, column=2)




check_lbl = Label (text="", fg=GREEN, bg=YELLOW)
check_lbl.grid(row=3, column=1)



window.mainloop()