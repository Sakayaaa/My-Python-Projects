from tkinter import *


# CLASS FOR ADDING NEW LABEL AND ENTRY USING TKINTER
class LabelAndEntry:
    def __init__(self, window, text, x, y, distance=80, data_type="str", state=None):
        Label(window, text=text).place(x=x, y=y)

        # CONDITION FOR EACH DATA TYPE INPUT
        match data_type:
            case "str":
                self.variable = StringVar()
            case "int":
                self.variable = IntVar()
            case "float":
                self.variable = DoubleVar()
            case "bool":
                self.variable = BooleanVar()
            case _:
                self.variable = StringVar()

        # ENTRY BOX INFORMATION
        Entry(window, textvariable=self.variable, state=state).place(x=x + distance, y=y)
