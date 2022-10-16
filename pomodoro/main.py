from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
new_check = ""
timer = ""


# ---------------------------- TIMER RESET ------------------------------- #

def reset():
    global reps, new_check
    window.after_cancel(timer)
    reps = 0
    new_check = ""
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer")
    check_label.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start():
    global reps
    reps += 1

    if reps % 8 == 0:
        countdown(LONG_BREAK_MIN * 60)
        timer_label.config(text="BREAK", fg=RED)
    elif reps % 2 == 0:
        countdown(SHORT_BREAK_MIN * 60)
        timer_label.config(text="BREAK", fg=PINK)
    else:
        countdown(WORK_MIN * 60)
        timer_label.config(text="WORK", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    global timer
    count_min = math.floor(count / 60)
    count_sek = count % 60
    if count_sek == 0 or count_sek < 10:
        count_sek = f"0{count_sek}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sek}")
    if count > 0:
        timer = window.after(1000, countdown, count - 1)
    else:
        start()
        if reps % 2 == 0 and reps != 0:
            global new_check
            new_check += "✓"
            check_label.config(text=new_check)


# ---------------------------- UI SETUP ------------------------------- #

# WINDOW

window = Tk()
window.title("Pomodoro")
window.config(pady=50, padx=100, bg=YELLOW)

# POMODORO

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# TIMER SIGN

timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 45, "bold"))
timer_label.grid(column=1, row=0)

# CHECK SIGN

check_label = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 15, "bold"))
check_label.grid(column=1, row=3)

# START BUTTON


start_button = Button(text="Start", command=start)
start_button.grid(column=0, row=2)

# RESET BUTTON


reset_button = Button(text="Reset", command=reset)
reset_button.grid(column=2, row=2)

window.mainloop()
