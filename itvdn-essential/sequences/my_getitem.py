values = [1, 3, 5, 4, 22, 911]
# print(values.__getitem__(1), values[1])
# print(values.__getitem__(slice(2,5)))
print(values)
del values[:2]
values.__delitem__(-1)
print(values)
# import collections.abc
# print(dir(collections.abc.MutableSequence))

print('='*25)

values = [5, -1, 6, 0, 2, 909]
print(f"initial array: {values}")
values.sort(key=abs)
print(f"sorted by abs array: {values}")

print('='*25)
print('Problem of shallow copy')
def print_matrix(matrix):
    for row in matrix:
        print(' '.join(str(x) for x in row))


matrix = [[0] * 5] * 5
print_matrix(matrix)
print('-' * 20)
matrix[2][2] = 1
print_matrix(matrix)
print('-' * 20)
matrix = [[0] * 5 for _ in range(5)]
matrix[2][2] = 1
print_matrix(matrix)
