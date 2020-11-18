from .GUI import GUI

import random as rd


class Application:
    def __init__(self, cards, master=None):
        self.gui = GUI(master)
        self.cards = cards
        self.gui.correct_btn.bind('<Button-1>', self.correct)
        self.gui.incorrect_btn.bind('<Button-1>', self.incorrect)
        self.gui.check_btn.bind('<Button-1>', self.check)
        self.gui.write(cards[0].word, cards[0].kana)

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
            self.gui.write("Congratulations !")

    def validate(self):
        self.gui.validate()
        self.gui.write(self.cards[0].word, self.cards[0].kana)

    def check(self, event):
        self.gui.check()
        self.gui.write(self.cards[0].eng)
