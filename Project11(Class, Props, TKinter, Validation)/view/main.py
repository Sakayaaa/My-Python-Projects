# IMPORT SECTION
from tkinter import *
from view.component.label_and_entry import LabelAndEntry
from model.lesson import Lesson
import tkinter.messagebox as msg
from view.component.table import Table

# TO CREATE A NEW LESSON LIST
lesson_list = []


# DEF SECTION
def reset_form():
    name.variable.set("")
    code.variable.set(0)
    day.variable.set("")
    start_time.variable.set(0)
    duration.variable.set(0)
    teacher.variable.set("")

    lesson_table.show_data(lesson_list)


def save_click():
    try:
        # TO ADD THE GIVEN INFORMATION FROM USER TO THE LIST
        lesson = Lesson(
            name.variable.get(),
            code.variable.get(),
            day.variable.get(),
            start_time.variable.get(),
            duration.variable.get(),
            teacher.variable.get()
        )

        lesson_list.append(lesson)
        msg.showinfo("Save", "Lesson Saved")
        reset_form()

    # TO SHOW ERROR IF USER HAS GIVEN WRONG INFO
    except Exception as e:
        msg.showerror("Save Error", f"Error : {e}")


# TKINTER SECTION
win = Tk()
win.geometry("900x350")
win.title("Lessons")

name = LabelAndEntry(win, "Name", 20, 20)
code = LabelAndEntry(win, "Code", 20, 60)
day = LabelAndEntry(win, "Day", 20, 100)
start_time = LabelAndEntry(win, "S.Time", 20, 140)
duration = LabelAndEntry(win, "Duration", 20, 180)
teacher = LabelAndEntry(win, "Teacher", 20, 220)

headings = ["Name", "Code", "Day", "S.Time", "Duration", "Teacher"]
widths = [100, 80, 100, 100, 100, 100]

lesson_table = Table(win, headings, widths, 280, 20)

Button(win, text="Save", width=12, command=save_click).place(x=70, y=300)

win.mainloop()
