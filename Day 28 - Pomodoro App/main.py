from cgitb import text
from time import time
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECKMARK = '✔'
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    # cancels window.after loop
    reset_button.config(state='disabled')
    window.after_cancel(timer)

    # change the labels as it was in starting
    timer_label.config(text='Timer!')
    canvas.itemconfig(timer_text, text='00:00')
    checkmark_label.config(text='')
    global reps
    reps = 0
    start_button.config(state='active')

    


# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    start_button.config(state='disabled')
    reset_button.config(state='active')
    global reps 
    reps += 1
    if reps == 8:
        countdown(LONG_BREAK_MIN * 60)
        timer_label.config(text='Break!', fg=PINK)
    elif reps % 2 == 0:
        countdown(SHORT_BREAK_MIN * 60)
        timer_label.config(text='Break!', fg=RED)
    else:
        countdown(WORK_MIN * 60)
        timer_label.config(text='Work!', fg=GREEN)


    
    

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def countdown(time_seconds):
    minutes = time_seconds // 60
    seconds = time_seconds % 60
    if seconds < 10:
        seconds = f'0{seconds}'
    if minutes < 10:
        minutes = f'0{minutes}'
    canvas.itemconfig(timer_text, text=f'{minutes}:{seconds}')
    if time_seconds > 0:
        global timer
        timer = window.after(1000, countdown, time_seconds-1)
    else:
        start_timer()
        check_text = ''
        for _ in range(reps // 2):
            check_text += f'{CHECKMARK}'
        checkmark_label.config(text=check_text)
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg=YELLOW)

# topmost timer text layout
timer_label = Label(text='Timer!', fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40, 'bold') )
timer_label.grid(row=0, column=1)

# tomato image & timer layout using canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill='white', font=(FONT_NAME, 32, 'bold'))
canvas.grid(row=1, column=1)



# start button layout
start_button = Button(text='Start', command=start_timer)
start_button.grid(row=2, column=0)

# reset button layout
reset_button = Button(text='Reset', command=reset_timer)
reset_button.grid(row=2, column=2)
reset_button.config(state='disabled')

# pomodoro checkmark layout 
checkmark_label = Label(text='', fg=GREEN, bg=YELLOW, font=(FONT_NAME, 14, 'bold'))
checkmark_label.grid(row=3, column=1)


window.mainloop()