import sys, csv

from app.Card import Card
from app.CardEncoder import CardEncoder
from app.Bank import Bank

def main():
    bank = Bank()
    cards = []
    with open(sys.argv[1], "r", encoding = "utf16") as word_bank:
        read = csv.DictReader(word_bank)
        for line in read:
            cards.append(Card(line['Word'], line['Kana'], line['English']))
    bank.save(cards)

if __name__ == "__main__":
    main()