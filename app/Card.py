class Card:
    def __init__(self, word, eng, kana):
        self.word = word
        self.eng = eng
        self.kana = kana
    
    def __str__(self):
        return f"{self.word} - {self.eng} - {self.kana}"
    
    def __eq__(self, card):
        return self.eng == card.eng and self.kana == card.kana and self.word == card.word
