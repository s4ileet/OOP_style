import tkinter
from tkinter import *
import random


class RandomAdder:
    def __init__(self, window):
        self.window = window
        window.geometry("300x200+10+20")
        window.title("Random num adder")
        window.rowconfigure(0, minsize=50, weight=1)
        window.columnconfigure([0, 1, 2], minsize=50, weight=1)

        self.incDecButton = tkinter.Button(window, text="Inc", command=self.increaseDecrease)
        self.incDecButton.grid(row=0, column=2)

        self.closeButton = tkinter.Button(window, text="Goodbye", command=window.quit)
        self.closeButton.grid(row=1, column=0)

        self.clearButton = tkinter.Button(window, text="Clear", command=self.clear)
        self.clearButton.grid(row=1, column=2)

        self.lblValue = tkinter.Label(window, text="0")
        self.lblValue.grid(row=0, column=1)

    def increaseDecrease(self):
        value = int(self.lblValue["text"])
        self.lblValue["text"] = f"{value + random.randint(-100, 100)}"

    def clear(self):
        self.lblValue["text"] = "0"


root = Tk()
my_gui = RandomAdder(root)
root.mainloop()
