from tkinter import *
import math


def btn_enter(event):
    event.widget.config(bg="black", fg="white")


def btn_leave(event):
    event.widget.config(bg="white", fg="black")


def btn_click(event):
    clicked_btn = event.widget
    char = clicked_btn["text"]

    if char == "C":
        result.set("")  # Clear the display

    elif char == "=":
        if result.get() != "":
            result.set(str(eval(result.get())))  # Only evaluate non-empty inputs
        else:
            result.set("Error")  # Set error if empty

    elif char == "SQ":
        if result.get() != "" and result.get().isdigit():
            result.set(str(round(math.sqrt(float(result.get())), 2)))
        else:
            result.set("Error")  # Handle invalid or empty inputs

    elif char == ".":
        if "." not in result.get():
            result.set(result.get() + char)  # Add decimal only if absent

    elif char == "0":
        if result.get() == "" or result.get() == "0":
            result.set("0")  # Prevent multiple leading zeros
        else:
            result.set(result.get() + char)  # Append zero if valid

    elif char not in ["M"]:  # Ignore unimplemented "M"
        if result.get() == "0":
            result.set(char)  # Replace leading zero
        elif len(result.get()) < 10:
            result.set(result.get() + char)


win = Tk()
win.title('Calculator')
win.geometry("290x300")
win.config(bg="lightcyan")

buttons = [
    ["7", "8", "9", "/", "C"],
    ["4", "5", "6", "*", "M"],
    ["1", "2", "3", "-", "**"],
    ["0", ".", "=", "+", "SQ"]
]

result = StringVar()
(Entry(win
       , textvariable=result
       , font=("arial", 20)
       , state="readonly")
 .place(x=30, y=30, width=228))

distance = 48
width = 4
height = 2
start_x = 30
start_y = 80

for row in range(4):
    for col in range(5):
        text = buttons[row][col]
        btn = Button(win, text=text, width=width, height=height, bg="white", fg="black")
        btn.place(x=start_x + col * distance, y=start_y + row * distance)
        btn.bind("<Enter>", btn_enter)
        btn.bind("<Leave>", btn_leave)
        btn.bind("<ButtonRelease>", btn_click)

win.mainloop()
