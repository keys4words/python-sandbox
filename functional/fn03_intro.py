elem = lambda value, next: {'value': value, 'next': next}
to_str = lambda head: '' if head is None \
                        else str(head['value']) + ' ' + to_str(head['next'])

values = elem(1, elem(2, elem(3, None)))
print(to_str(values))