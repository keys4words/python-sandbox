import random
import array
import os.path

# numbers = [random.randint(-1000000000, 1000000000) for _ in range(1000)]

# with open('inout/data/data4.txt', 'w') as f:
#     for number in numbers:
#         f.write('{}\n'.format(number))

# numbers_array = array.array('i', numbers)
# with open('inout/data/data4.bin', 'wb') as f:
#     f.write(numbers_array)

# numbers = []
# with open('inout/data/data4.txt', 'r') as f:
#     numbers = [int(line) for line in f]

# print(numbers)

filesize = os.path.getsize('inout/data/data4.bin')
count = filesize//array.array('i').itemsize
numbers = array.array('i', (0 for _ in range(count)))

with open('inout/data/data4.bin', 'rb') as f:
    f.readinto(numbers)

print(numbers)
