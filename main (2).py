import tkinter as tk


# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#38E54D"
YELLOW = "#f7f5dd"
BACK = "#BAD7E9"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 1
reps = 0
check_mult = 0
checks = ""

# ---------------------------- TIMER RESET ------------------------------- # 


def reset_timer():
    pass  # TODO make the "resert" button reset the current timer
# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_timer():
    global reps
    global checks
    global check_mult
    if reps % 2 == 0:
        check_mult += 1
    reps += 1
    check = tk.Label(text=checks, bg=BACK, font=("arial", 24, "normal"))
    check.grid(column=1, row=4)
    if reps % 2 == 1:
        # odd # of reps
        timer_label.config(fg="#00FFCA", text="W O R K", bg="#088395")
        minutes = WORK_MIN
    elif reps % 2 == 0 and reps != 8:  # even # of reps, reps is not a multiple of 8 (or 8)
        timer_label.config(fg="pink", text="sB R E A K", )
        minutes = SHORT_BREAK_MIN
    else:
        timer_label.config(fg="red", text="B R E A K")
        minutes = LONG_BREAK_MIN
    checks = ""
    checks += "💯" * check_mult
    print(f"{checks=}")
    countdown(minutes * 60)  # 300 seconds, or 5 minutes
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 


def countdown(count):
    """it's recursive!"""
    global reps
    # count represents the seconds
    # count // 60 = minutes
    # count % 60 = seconds
    minutes = count // 60
    seconds = count % 60
    if seconds < 10:
        seconds = f"0{seconds}"
    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")  # could have used :2d to format for leading zeroes
    if count > 0:
        window.after(25, countdown, count - 1)
        # window.after(60_000, countdown, minutes - 1, seconds)
    if count == 0:
        start_timer()
# ---------------------------- UI SETUP ------------------------------- #


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

# 2, 3
restart_button = tk.Button(text="Restart", bg=GREEN, anchor="e", command=start_timer)
restart_button.grid(column=3, row=3)

# 1, 4

window.mainloop()
