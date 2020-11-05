import json
import pprint
from difflib import get_close_matches

with open('data.json', 'r') as f:
    items = json.load(f)

# pprint.pprint(items)

def translate(word):
    word = word.lower()
    if word in items:
        return items[word]
    elif word.title() in items:
        return items[word.title()]
    elif word.upper() in items:
        return items[word.upper()]
    elif len(get_close_matches(word, items.keys())) > 0:
        print("Did you mean '%s' instead?" % get_close_matches(word, items.keys())[0])
        decide = input("Press y/Y for 'Yes' or n/no for 'No': ")
        if decide in ['y', 'Y']:
            return items[get_close_matches(word, items.keys())[0]]
        elif decide.lower() in ['n', 'no']:
            return 'No data'
        else:
            return 'Wrong input'
    else:
        print('no data')
        return ''


word = input('Enter word you want to search: ')
output = translate(word)
if type(output) == list:
    for item in output:
        print('\t->'+item)
else:
    print(output)
