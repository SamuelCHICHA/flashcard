import sys

from app.Application import Application
from app.Bank import Bank


def main():
    if len(sys.argv) != 2:
        print("Wrong number of arguments. Expects one.", file=sys.stderr)
        sys.exit()
    bank = Bank()
    cards = bank.load(int(sys.argv[1]))
    app = Application(cards)
    app.gui.mainloop()


if __name__ == "__main__":
    main()
