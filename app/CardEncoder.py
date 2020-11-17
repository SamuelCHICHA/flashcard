import json

from json import JSONEncoder
from .Card import Card


class CardEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Card):
            return obj.__dict__
        else:
            return json.JSONEncoder.default(self, obj)

    @staticmethod
    def as_card(card_dict):
        if 'eng' in card_dict and 'kana' in card_dict and 'word' in card_dict:
            return Card(word=card_dict['word'], eng=card_dict['eng'], kana=card_dict['kana'])
        else:
            raise Exception('Not a Card.')
