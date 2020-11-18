import tkinter as tk


class GUI(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.fullscreen = False
        self.master = master
        self.master.protocol('WM_DELETE_WINDOW', self.master.destroy)
        self.master.title("Flashcard")
        self.incorrect_btn = tk.Button(self, text="Incorrect")
        self.correct_btn = tk.Button(self, text="Correct")
        self.check_btn = tk.Button(self, text='Check')
        self.content = tk.StringVar()
        self.complementary_content = tk.StringVar()
        self.label = tk.Label(self, textvariable=self.content)
        self.complementary_label = tk.Label(self, textvariable=self.complementary_content)
        self.master.geometry("{0}x{1}+0+0".format(self.master.winfo_screenwidth(), self.master.winfo_screenheight()))
        self.master.bind('<KeyRelease-F12>', self.toggle_fullscreen_mode)
        self.pack()
        self.init_pack()

    def init_pack(self):
        self.check_btn.pack(side='bottom')
        self.label.pack()
        self.complementary_label.pack()

    def write(self, text="", complementary=""):
        self.content.set(text)
        if text != complementary or text == "":
            self.complementary_content.set(complementary)

    def check(self):
        self.check_btn.pack_forget()
        self.correct_btn.pack(side='right')
        self.incorrect_btn.pack(side='left')

    def validate(self):
        self.correct_btn.pack_forget()
        self.incorrect_btn.pack_forget()
        self.check_btn.pack(side='bottom')

    def toggle_fullscreen_mode(self, event):
        self.fullscreen = not self.fullscreen
        self.master.attributes('-fullscreen', self.fullscreen)
