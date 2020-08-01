# one.py

def func():
    print('func in one.py')

print('TOP level in one.py')


if __name__ == '__main__':
    print('one.py runs directly')
else:
    print('one.py has been imported')