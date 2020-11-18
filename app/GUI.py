import tkinter as tk
import tkinter.ttk as ttk
import ttkthemes
import tkinter.font as tkfont


class GUI(ttkthemes.ThemedTk):
    def __init__(self):
        super().__init__(theme="equilux")
        self.font = tkfont.Font(family="Times", size=24)
        self.fullscreen = False
        self.title("Flashcard")
        self.config(bg="black")
        self.incorrect_btn = ttk.Button(self, text="Incorrect")
        self.correct_btn = ttk.Button(self, text="Correct")
        self.check_btn = ttk.Button(self, text='Check')
        self.content = tk.StringVar()
        self.complementary_content = tk.StringVar()
        self.label = ttk.Label(
            self, textvariable=self.content,
            font=self.font,
            justify="center",
            anchor="center"
        )
        self.complementary_label = ttk.Label(
            self,
            textvariable=self.complementary_content,
            font=self.font,
            justify="center",
            anchor="center"
        )
        self.init_config()
        self.init_pack()

    def init_config(self):
        self.protocol('WM_DELETE_WINDOW', self.destroy)
        self.geometry("{0}x{1}+0+0".format(self.winfo_screenwidth(), self.winfo_screenheight()))
        self.bind('<Shift-Up>', self.toggle_fullscreen_mode)

    def init_pack(self):
        self.check_btn.pack(
            side='bottom',
            pady=30,
            padx=self.winfo_screenwidth()/3,
            fill='x'
        )
        self.label.pack(
            ipady=10,
            pady=self.winfo_screenheight()/8,
            fill='x',
            padx=self.winfo_screenwidth()/4,

        )

    def write(self, text, complementary=None):
        self.content.set(text)
        if complementary is not None and text != complementary:
            self.complementary_label.pack(
                ipady=10,
                pady=self.winfo_screenheight()/8,
                fill='x',
                padx=self.winfo_screenwidth()/4,
            )
            self.complementary_content.set(complementary)
        else:
            self.complementary_label.pack_forget()

    def check(self):
        self.check_btn.pack_forget()
        self.correct_btn.pack(
            side='right',
            padx=self.winfo_screenwidth()/8,
            fill='x',
            pady=30
        )
        self.incorrect_btn.pack(
            side='left',
            padx=self.winfo_screenwidth()/8,
            fill='x',
            pady=30
        )

    def validate(self):
        self.correct_btn.pack_forget()
        self.incorrect_btn.pack_forget()
        self.check_btn.pack(
            side='bottom',
            pady=30,
            padx=self.winfo_screenwidth()/3,
            fill='x'
        )

    def toggle_fullscreen_mode(self, event):
        self.fullscreen = not self.fullscreen
        self.attributes('-fullscreen', self.fullscreen)
