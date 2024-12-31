from view.component.table import Table
from view.component.label_and_entry import LabelAndEntry
from da.license_da import *
from tkinter import *
import tkinter.messagebox as msg
import tkinter.ttk as ttk



def reset_form():
    id.variable.set(0)
    name.variable.set("")
    grade.variable.set(0)
    license_date.variable.set(0)
    license_no.variable.set(0)
    table.show_data(find_all())


def save_click():
    try:
        license = License(None, name.variable.get(), grade.variable.get(), license_date.variable.get(),
                          license_no.variable.get())
        save(license)
        msg.showinfo("Save", "Save Done")
        reset_form()
    except Exception as e:
        msg.showerror("Save Error", f"Error : {e}")


def edit_click():
    try:
        license = License(id.variable.get(), name.variable.get(), grade.variable.get(), license_date.variable.get(),
                          license_no.variable.get())
        edit(license)
        msg.showinfo("Edit", "Edit Done")
        reset_form()
    except Exception as e:
        msg.showerror("Edit Error", f"Error : {e}")


def remove_click():
    if msg.askyesno("Confirm Remove", "Are you sure you want to remove this license?"):
        try:
            license = License(id.variable.get(), name.variable.get(), grade.variable.get(), license_date.variable.get(),
                              license_no.variable.get())
            save(license)
            msg.showinfo("Remove", "Remove Done")
            reset_form()
        except Exception as e:
            msg.showerror("Remove Error", f"Error : {e}")


win = Tk()
win.geometry("660x270")
win.title("License View")

id = LabelAndEntry(win, "ID", 20, 20, state="readonly", data_type="int")
name = LabelAndEntry(win, "Name", 20, 60)
grade = LabelAndEntry(win, "grade", 20, 100, data_type="int")
license_date = LabelAndEntry(win, "Date", 20, 140)
license_no = LabelAndEntry(win, "License No.", 20, 180)

table = Table(win, ["Id", "Name", "grade", "Date", "License No."], [50, 100, 60, 80, 100], 250, 20)

Button(win, text="Save", width=7, command=save_click).place(x=20, y=220)
Button(win, text="Edit", width=7, command=edit_click).place(x=92, y=220)
Button(win, text="Remove", width=7, command=remove_click).place(x=164, y=220)


win.mainloop()
