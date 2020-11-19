from .GUI import GUI
from .Bank import Bank
import random as rd

# Handles all the application (GUI, Cards, Bank, Events)


class Application:
    def __init__(self):
        self.gui = GUI()
        self.bank = Bank()
        self.cards = self.bank.load(20)
        self.__init_bind()
        self.gui.write_card(self.cards[0].word, self.cards[0].kana)

    def __init_bind(self):
        self.gui.correct_btn.bind('<Button-1>', self.correct)
        self.gui.incorrect_btn.bind('<Button-1>', self.incorrect)
        self.gui.check_btn.bind('<Button-1>', self.check)
        self.gui.reload_btn.bind('<Button-1>', self.reload)

    def __restart(self):
        self.gui.__initpack()
        self.gui.write_card(self.cards[0].word, self.cards[0].kana)

    def incorrect(self, event):
        self.cards.insert(rd.randint(0, len(self.cards) - 1), self.cards.pop(0))
        self.validate()

    def correct(self, event):
        self.cards.pop(0)
        if len(self.cards) > 0:
            self.validate()
        else:
            self.gui.incorrect_btn.pack_forget()
            self.gui.correct_btn.pack_forget()
            self.gui.write_card("Congratulations !")
            self.gui.reload_btn.pack()

    def validate(self):
        self.gui.validate()
        self.gui.write_card(self.cards[0].word, self.cards[0].kana)

    def check(self, event):
        self.gui.check()
        self.gui.write_card(self.cards[0].eng)

    def reload(self, event):
        self.cards = self.bank.load(20)
        self.gui.reload_btn.pack_forget()
