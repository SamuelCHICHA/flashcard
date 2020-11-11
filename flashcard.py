from app.Bank import Bank
from app.Application import Application

import sys, tkinter as tk


def main():
    if len(sys.argv) != 2:
        print("Wrong number of arguments. Expects one.", file=sys.stderr)
        sys.exit()
    bank = Bank()
    cards = bank.load(int(sys.argv[1]))
    root = tk.Tk()
    gui = Application(master=root)
    gui.master.title("Flashcard")

    gui.mainloop()
    for card in cards:
        print(f"{card}")


if __name__ == "__main__":
    main()
