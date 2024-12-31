from tkinter import *
from product_data_access import save_product
from component.label_and_entry import LabelAndEntry
import tkinter.messagebox as msg


def save_click():
    try:
        save_product(product.variable.get(), quantity.variable.get(), price.variable.get())
        msg.showinfo("Save", "Product Saved")
    except Exception as e:
        msg.showerror("Error", f"Something went wrong {e}")


win = Tk()
win.geometry("400x300")

id = LabelAndEntry(win, "Id", 20, 20, state="readonly")
product = LabelAndEntry(win, "Product", 20, 60)
quantity = LabelAndEntry(win, "Quantity", 20, 100)
price = LabelAndEntry(win, "Price", 20, 140)

Button(win, text="Save", command=save_click).place(x=80, y=220)

win.mainloop()
