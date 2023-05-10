import tkinter as tk
import time
import pomodorotimer

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#38E54D"
YELLOW = "#f7f5dd"
BACK = "#BAD7E9"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    if not pomodorotimer.timer:
        return
    check.config(text="")
    timer_label.config(text="P O M O")
    canvas.itemconfig(timer_text, text="00:00")
    window.after_cancel(pomodorotimer.timer)
    pomodorotimer.reps = 0
    pomodorotimer.paused = False
    pomodorotimer.timer = None
# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    if pomodorotimer.paused or pomodorotimer.timer:
        return
    window.attributes("-topmost", True)
    time.sleep(0.2)
    window.attributes("-topmost", False)
    pomodorotimer.start()
    if pomodorotimer.reps % 2 == 1:
        timer_label.config(fg="#00FFCA", text="W O R K", bg="#088395")
        pomodorotimer.minutes = WORK_MIN
    elif pomodorotimer.reps % 2 == 0 and pomodorotimer.reps != 8:
        timer_label.config(fg="pink", text="sB R E A K", )
        pomodorotimer.minutes = SHORT_BREAK_MIN
    else:
        timer_label.config(fg="red", text="B R E A K")
        pomodorotimer.minutes = LONG_BREAK_MIN
    check.config(text=pomodorotimer.checks)
    countdown(pomodorotimer.minutes * 60)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def countdown(count=None):
    """it's recursive!"""
    if not count:
        count = pomodorotimer.seconds
    pomodorotimer.minutes = count // 60
    pomodorotimer.seconds = count % 60
    if pomodorotimer.seconds < 10:
        pomodorotimer.seconds = f"0{pomodorotimer.seconds}"
    canvas.itemconfig(timer_text, text=f"{pomodorotimer.minutes}:{pomodorotimer.seconds}")  # could have used :2d to format for leading zeroes
    if count > 0:
        pomodorotimer.timer = window.after(1000, countdown, count - 1)
    if count == 0:
        start_timer()
# ---------------------------- PAUSE / RESET ------------------------------- #


def pause_timer():
    if not pomodorotimer.timer:
        return
    elif not pomodorotimer.paused:
        window.after_cancel(pomodorotimer.timer)
        pomodorotimer.paused = True
    else:
        countdown(pomodorotimer.seconds + pomodorotimer.minutes*60)
        pomodorotimer.paused = False
# ---------------------------- UI SETUP ------------------------------- #

pomodorotimer = pomodorotimer.PomodoroTimer()
pomodorotimer.timer = None
window = tk.Tk()
window.title("Pomodoro")
window.config(padx=50, pady=25, bg="#BAD7E9")
window.geometry("400x400")
window.resizable(False, False)

# the after() method takes the time to wait and the fx to call, and then the arguments to pass to the called func
# after(time, func, args to pass to func)

# 1, 2
canvas = tk.Canvas(width=210, height=224, bg=BACK, highlightthickness=0)
tomato_img = tk.PhotoImage(file="tomato.png")
canvas.create_image(105, 112, image=tomato_img)
timer_text = canvas.create_text(108, 125, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=2)

# 1, 0
timer_label = tk.Label(text="P O M O", font=(FONT_NAME, 24, "normal"), bg=GREEN, anchor="center")
timer_label.grid(column=1, row=0)

# an empty row for spacing
empty_row = tk.Label(bg=BACK)
empty_row.grid(column=1, row=1)

# 0, 3
start_button = tk.Button(text="Start", bg=GREEN, command=start_timer)
start_button.grid(column=0, row=3)

# 1, 3
pause = tk.Button(text="Pause", bg=GREEN, command=pause_timer)
pause.grid(column=1, row=3)

# 2, 3
restart_button = tk.Button(text="Restart", bg=GREEN, anchor="e", command=reset_timer)
restart_button.grid(column=3, row=3)

# 1, 4
check = tk.Label(text=pomodorotimer.checks, bg=BACK, font=("arial", 24, "normal"))
check.grid(column=1, row=4)

window.mainloop()
