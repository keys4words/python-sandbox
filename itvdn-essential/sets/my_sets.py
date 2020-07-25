import random as r

empty_set = set()
empty_frozen_set = frozenset()

empty_set = {1, 2, 3, 4, 4, 5}
empty_frozen_set = frozenset([1, 3, 3, 8])
set_ = {x*2 for x in range(6)}

empty_set.add(434)
print('empty_set', empty_set)
# empty_set.remove(4)
# print('empty_set', empty_set)

print('empty_frozen_set', empty_frozen_set)
# print(set_)

# print(empty_set.symmetric_difference(empty_frozen_set))
# print(empty_frozen_set < empty_set)
# print(empty_set.discard(400))
# print(empty_set.pop())
# print(empty_set.pop())
# print(empty_set.pop())
# print(empty_set.pop())
empty_set.update(empty_frozen_set)
print('empty_set', empty_set)
s1 = input('Enter first string: ').split(' ')
# s2 = input('Enter second string: ')
vowels = {'a', 'o', 'u', 'y', 'i', 'e'}
print(''.join(set(s1) & vowels))