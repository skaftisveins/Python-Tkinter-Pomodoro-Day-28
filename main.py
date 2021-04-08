from tkinter import *
import tkinter.messagebox
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#2bc4a6"
YELLOW = "#f7f5dd"
BACKGROUND = "#c9c9c9"
BLACK = "#000000"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0
TIMER = None

# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():

    global REPS
    window.after_cancel(TIMER)  # Reset timer
    title_label.config(text="Timer")  # Reset title text
    canvas.itemconfig(timer_text, text="00:00")  # Reset timer text
    check_marks.config(text="")  # Reset checkmarks
    REPS = 0

# ---- ARE YOU SURE ---- #


def are_you_sure():
    msg_box = tkinter.messagebox.askyesno("Reset Pomodoro", "Are you sure?")
    if msg_box == True:
        print("Timer Reset")
        reset_timer()
    else:
        msg_box == False
# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global REPS
    REPS += 1
    work_seconds = WORK_MIN * 60
    short_break_seconds = SHORT_BREAK_MIN * 60
    long_break_seconds = LONG_BREAK_MIN * 60

    # while REPS < 9:

    if REPS % 8 == 0:
        count_down(long_break_seconds)  # If it's the 8th rep:
        title_label.config(text="Break", foreground=RED)
    elif REPS % 2 == 0:
        count_down(short_break_seconds)  # If it's 2nd/4th/6th reps:
        title_label.config(text="Break", foreground=PINK)
    else:
        count_down(work_seconds)  # If it's the 1st/3rd/5th/7th rep:
        title_label.config(text="Work", foreground=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    count_minutes = math.floor(count / 60)  # number of minutes
    count_seconds = count % 60  # number of seconds
    if count_seconds < 10:
        count_seconds = f"0{count_seconds}"

    canvas.itemconfig(timer_text, text=f"{count_minutes}:{count_seconds}")
    if count > 0:
        global TIMER
        TIMER = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(REPS/2)
        for _ in range(work_sessions):
            marks += "✔"
        check_marks.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, background=BACKGROUND)

canvas = Canvas(width=200, height=224,
                background=BACKGROUND, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white",
                                font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)


title_label = Label(text="Timer", font=(
    FONT_NAME, 35, "bold"), foreground=GREEN, background=BACKGROUND)
title_label.grid(column=1, row=0)

start_button = Button(text="Start", font=(
    FONT_NAME, 15, "bold"), foreground=BLACK, background=BACKGROUND, command=start_timer)
start_button.grid(column=0, row=2)

resest_button = Button(text="Reset", font=(
    FONT_NAME, 15, "bold"), foreground=BLACK, background=BACKGROUND, command=are_you_sure)
resest_button.grid(column=2, row=2)

quit_button = Button(text="QUIT", font=(
    FONT_NAME, 15, "bold"), foreground=RED, background=BLACK, command=window.destroy)
quit_button.grid(column=1, row=4)

check_marks = Label(font=(
    FONT_NAME, 15, "bold"), foreground=GREEN, background=BACKGROUND)
check_marks.grid(column=1, row=3)

window.mainloop()
