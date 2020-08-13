from itertools import product, chain, permutations, combinations, combinations_with_replacement

# product
# for i in range(2, 5):
#     for j in range(1, 3):
#         print('{} x {} = {}'.format(i, j, i*j))

# print('*'*24)
# for i, j in product(range(2, 5), range(1, 3)):
#     print('{} x {} = {}'.format(i, j, i*j))

# print('*'*24)

# chain
# for i in chain(range(2, 5), range(1, 3)):
#     print(i)

string = 'ABC'
elements = 2
# print(list(permutations(string, elements)))
# print(list(combinations(string, elements)))
# print(list(combinations_with_replacement(string, elements)))


from itertools import takewhile, dropwhile

values = [1, 4, 3, 33, 4, 1, 0, 2, 90]
cond_func = lambda x: x < 5
# first_part
for el in takewhile(cond_func, values):
    print(el)

print('-'*30)
# second_part
for el in dropwhile(cond_func, values):
    print(el)