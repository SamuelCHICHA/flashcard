from app.Bank import Bank
from app.Card import Card

import sys

def main():
    bank = Bank()
    cards = bank.load(int(sys.argv[1]))
    for card in cards:
        print(f"{card}")
    


if __name__ == "__main__":
    main()