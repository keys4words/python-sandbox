elem = lambda value, next: {'value': value, 'next': next}
to_str = lambda head: '' if head is None \
                        else str(head['value']) + ' ' + to_str(head['next'])

values = elem(1, elem(2, elem(3, None)))
# print(to_str(values))

def make_powers(count):
    powers = []
    for i in range(count):
        # powers.append(lambda x: x ** i) # wrong code
        powers.append((lambda p: lambda x: x ** p)(i)) # wrong code
    return powers

powers = make_powers(5)
# for power in powers:
#     print(power(2))


handlers = []
for i in range(1, 4):
    def on_click(i=i):
        print('Button {} was clicked!'.format(i))
    handlers.append(on_click)

for handler in handlers:
    handler()