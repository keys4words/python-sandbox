import os.path

# with open(os.path.join('inout', 'data', 'example.txt')) as myfile:
#     print(myfile.read())
# myfile.close()


class MyManager:
    def __init__(self):
        self.resource = 43

    def __enter__(self):
        print('Entered context')
        return self.resource

    def __exit__(self, exc_type, exc_value, exc_traceback):
        print('Left context')
        if exc_type:
            print('Exception occured: {}'.format(exc_type))

# with MyManager() as resource:
#     print("some actions with resource:", resource)
#     raise ValueError

with open(__file__) as source:
    for number, line in enumerate(source, 1):
        print('{:3}: {}'.format(number, line), end='')