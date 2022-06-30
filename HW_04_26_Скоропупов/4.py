import json
import string


ORDER = [i for i in range(10000, -1, -1)]
TABLE = dict()


def add_dict(symbols: str, name: str):
    TABLE[name] = {symbol: ORDER.pop() for symbol in symbols}


add_dict(string.whitespace, 'whitespace')
add_dict(string.punctuation, 'punctuation')
add_dict(string.ascii_letters, 'ascii_letters')

with open('4.json', 'w', encoding='utf-8') as fot:
    fot.write(json.dumps(TABLE, indent=4))
