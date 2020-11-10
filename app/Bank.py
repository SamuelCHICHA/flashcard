from .CardEncoder import CardEncoder
import json, random

class Bank:
    def __init__(self, path_to_bank = "data/bank.json", path_to_done = "done.json"):
        self.path_to_bank = path_to_bank
        self.path_to_done = path_to_done
    
    def load(self, nb_card):
        card_encoder = CardEncoder()
        with open(self.path_to_bank, "r", encoding = "utf16") as bank_file:
            cards = json.load(bank_file, object_hook = CardEncoder.as_card)
        random.shuffle(cards)
        if nb_card > 0:
            cards = cards[:nb_card]
        else:
            raise Exception("The number of cards can't be negative.")
        return cards

    def save(self, cards):
        card_encoder = CardEncoder()
        with open(self.path_to_bank, "w", encoding = "utf16") as bank_file:
            bank_file.write(card_encoder.encode(cards))

        
    

