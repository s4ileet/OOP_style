import tkinter
from tkinter import *


class InputCounter:

    def __init__(self, window):
        self.window = window
        window.geometry("300x200+10+20")
        window.title("Counter")
        window.rowconfigure(0, minsize=50, weight=1)
        window.columnconfigure([0, 1, 2], minsize=50, weight=1)

        self.frame = Frame(window)
        self.frame.pack()

        self.var = StringVar()
        self.entry = Entry(self.frame, textvariable=self.var, width=75)
        self.entry.pack()

        self.countButton = tkinter.Button(window, text="Count", command=self.countATCG)
        self.countButton.pack()

        self.clearButton = tkinter.Button(window, text="Clear", command=self.clear)
        self.clearButton.pack()

        self.closeButton = tkinter.Button(window, text="Goodbye", command=window.quit)
        self.closeButton.pack()

        self.var.trace('w', self.validate)

    count = ()

    def countATCG(self):
        A = 0
        T = 0
        C = 0
        G = 0
        variable = self.entry.get()
        for i in variable:
            if i == 'A':
                A = A + 1
            if i == 'T':
                T = T + 1
            if i == 'C':
                C = C + 1
            if i == 'G':
                G = G + 1
        count = ("Num As:%s Num Bs:%s Num Cs:%s Num Gs:%s" % (A, T, C, G))
        frame2 = Label(self.frame, text=count)
        frame2.pack()

    def clear(self):
        self.entry.delete(0, END)

    def scope(self, user_input):
        if user_input in ['A', 'C', 'T', 'G']:
            return True
        else:
            return False

    def validate(self, *args):
        if not self.scope(self.var.get()):
            corrected = ''.join(filter(self.scope, self.var.get()))
            self.var.set(corrected)


root = Tk()
my_gui = InputCounter(root)
root.mainloop()