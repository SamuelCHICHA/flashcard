import tkinter as tk


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.correct = tk.Button(self, text="Correct")
        self.correct.pack(side="right")
        self.incorrect = tk.Button(self, text="Incorrect")
        self.incorrect.pack(side="left")
        self.quit = tk.Button(self, text="Exit", command=self.master.destroy, fg="red")
        self.quit.pack(side="bottom")
