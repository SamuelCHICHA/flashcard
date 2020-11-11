import csv
import sys

from app.Bank import Bank
from app.Card import Card


def main():
    if len(sys.argv) != 2:
        print("Wrong number of arguments. Expects one.", file=sys.stderr)
        sys.exit()
    bank = Bank()
    cards = []
    with open(sys.argv[1], "r", encoding="utf16") as word_bank:
        read = csv.DictReader(word_bank)
        for line in read:
            cards.append(Card(line['Word'], line['Kana'], line['English']))
    bank.save(cards)


if __name__ == "__main__":
    main()
