import tkinter as tk
import tkinter.ttk as ttk
import ttkthemes
import tkinter.font as tkfont


# Themed GUI class.

class GUI(ttkthemes.ThemedTk):
    def __init__(self):
        super().__init__(theme="equilux")
        font = tkfont.Font(family="Times", size=24)
        self.fullscreen = False
        self.reload_btn = ttk.Button(
            self,
            text="Reload",
            style='R.TButton'
        )
        self.incorrect_btn = ttk.Button(
            self,
            text="Incorrect",
            style='I.TButton'
        )
        self.correct_btn = ttk.Button(
            self,
            text="Correct",
            style="C.TButton"
        )
        self.check_btn = ttk.Button(
            self,
            text='Check'
        )
        self.content = tk.StringVar()
        self.complementary_content = tk.StringVar()
        self.label = ttk.Label(
            self, textvariable=self.content,
            font=font,
            justify="center",
            anchor="center"
        )
        self.complementary_label = ttk.Label(
            self,
            textvariable=self.complementary_content,
            font=font,
            justify="center",
            anchor="center"
        )
        self.__init_config()
        self.__init_style()
        self.__init_pack()

    def __init_config(self):
        self.title("Flashcard")
        self.protocol('WM_DELETE_WINDOW', self.destroy)
        self.geometry("{0}x{1}+0+0".format(self.winfo_screenwidth(), self.winfo_screenheight()))
        self.bind('<Shift-Up>', self.toggle_fullscreen_mode)

    def __init_pack(self):
        self.check_btn.pack(
            side='bottom',
            pady=30,
            padx=self.winfo_screenwidth() / 3,
            fill='x'
        )
        self.label.pack(
            ipady=10,
            pady=self.winfo_screenheight() / 8,
            fill='x',
            padx=self.winfo_screenwidth() / 4
        )

    def __init_style(self):
        self.config(bg="#111111")
        style = ttk.Style()
        style.configure('I.TButton', background="#A00000", foreground="#FFFFFF")
        style.configure('C.TButton', background="#00A000", foreground="#FFFFFF")
        style.configure('R.TButton', background="#0000A0", foreground="#FFFFFF")

    def write_card(self, text, complementary=None):
        self.content.set(text)
        if complementary is not None and text != complementary:
            self.complementary_label.pack(
                ipady=10,
                pady=self.winfo_screenheight() / 8,
                fill='x',
                padx=self.winfo_screenwidth() / 4,
            )
            self.complementary_content.set(complementary)
        else:
            self.complementary_label.pack_forget()

    def check(self):
        self.check_btn.pack_forget()
        self.correct_btn.pack(
            side='right',
            padx=self.winfo_screenwidth() / 8,
            fill='x',
            pady=30,
        )
        self.incorrect_btn.pack(
            side='left',
            padx=self.winfo_screenwidth() / 8,
            fill='x',
            pady=30,
        )

    def validate(self):
        self.correct_btn.pack_forget()
        self.incorrect_btn.pack_forget()
        self.check_btn.pack(
            side='bottom',
            pady=30,
            padx=self.winfo_screenwidth() / 3,
            fill='x'
        )

    def toggle_fullscreen_mode(self, event):
        self.fullscreen = not self.fullscreen
        self.attributes('-fullscreen', self.fullscreen)
