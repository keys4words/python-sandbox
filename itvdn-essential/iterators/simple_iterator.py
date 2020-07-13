class SimpleIterable:
    def __getitem__(self, index):
        if 0 <= index <= 5:
            return index * 2
        else:
            raise IndexError

iterable = SimpleIterable()
for value in iterable:
    print(value)
