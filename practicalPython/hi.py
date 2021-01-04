# in file: hello.py

# greetings = ["Hello", "Bonjour", "Hola"]

# for greeting in greetings:
#     print(f"{greeting}, World!")

import json, pprint

with open('cities.json') as f:
    data = json.load(f)
    pprint.pprint(data)
