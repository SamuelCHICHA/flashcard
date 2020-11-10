import json

from json import JSONEncoder
from .Card import Card

class CardEncoder(JSONEncoder):
    def default(self, object):
        if isinstance(object, Card):
            return object.__dict__
        else:
            return json.JSONEncoder.default(self, object)
    
    def as_card(dict):
        if 'eng' in dict and 'kana' in dict and 'word' in dict:
            return Card(dict['word'], dict['eng'], dict['kana'])
        else:
            raise Exception('Not a Card.')