from collections import namedtuple

# list/tuple
color=(55, 155, 255)
# print(color[0])

# dictionary
color = {'red': 55, 'green': 155, 'blue': 255}
# print(color['red'])

# namedtuple
Color = namedtuple('Color', ['red', 'green', 'blue'])
color = Color(55,155,255)
print(color.red, color[1])