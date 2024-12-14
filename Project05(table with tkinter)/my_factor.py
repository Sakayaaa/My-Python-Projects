from tkinter import *
from tkinter import StringVar
from tkinter.ttk import Treeview
import tkinter.messagebox as msg  # alias
from my_validation import *
from persian_tools.digits import convert_to_word

product_list = []


def reset_form():
    id.set(0)
    name.set("")
    brand.set("")
    price.set(0)
    quantity.set(0)


def total_calculator():
    total.set(total.get() + price.get() * quantity.get())


def total_in_persian():
    total_text.set(convert_to_word(total.get()))


def add_click():
    if name_validator(name.get()) and name_validator(brand.get()) and price_validator(price.get()) and quantity_validator(quantity.get()):
        product = (id.get(), name.get(), brand.get(), price.get(), quantity.get())
        total_calculator()
        total_in_persian()
        table.insert("", END, values=product)
        reset_form()
        msg.showinfo("Save", "Saved Successfully !")
        product_list.append(product)
    else:
        msg.showerror("Save Error", "Invalid Data !!!")


win = Tk()
win.geometry("710x500")
win.title("Form")

# Id
Label(win, text="ID").place(x=20, y=20)
id = IntVar()
Entry(win, textvariable=id).place(x=80, y=20)

# Name
Label(win, text="Name").place(x=20, y=70)
name = StringVar()
Entry(win, textvariable=name).place(x=80, y=70)

# Brand
Label(win, text="Brand").place(x=20, y=120)
brand = StringVar()
Entry(win, textvariable=brand).place(x=80, y=120)

# Price
Label(win, text="Price").place(x=20, y=170)
price = IntVar()
Entry(win, textvariable=price).place(x=80, y=170)

# Quantity
Label(win, text="Quantity").place(x=20, y=220)
quantity = IntVar()
Entry(win, textvariable=quantity).place(x=80, y=220)

# Total
Label(win, text="Total").place(x=20, y=270)
total = IntVar()
Entry(win, textvariable=total, state="readonly").place(x=80, y=270)

# Total In Text (Persian)
total_text = StringVar()
Entry(win, textvariable=total_text, state="readonly").place(x=30, y=310, width=175)

# Table
table = Treeview(win, columns=["1", "2", "3", "4", "5"], height=21, show="headings")

# Title
table.heading("1", text="Id")
table.heading("2", text="Name")
table.heading("3", text="Brand")
table.heading("4", text="Price")
table.heading("5", text="Quantity")

# Width
table.column("1", width=60)
table.column("2", width=100)
table.column("3", width=100)
table.column("4", width=80)
table.column("5", width=80)
table.place(x=250, y=20)

# Save
Button(win, text="Add", width=12, command=add_click).place(x=80, y=370)

win.mainloop()
