import random
import sort_methods

def create_random_list(size, max_value):
    return [random.randint(1, max_value) for x in range(size)]

size = int(input('What size list do you want to create? '))
max_value = int(input('What is the max value in the list? '))

print(create_random_list(size, max_value))
