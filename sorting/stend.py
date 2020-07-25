import random, time
from sort_methods import quick_sort, merging_sort, bubble_sort, insertion_sort, selection_sort

def create_random_list(size, max_value):
    return [random.randint(1, max_value) for x in range(size)]

size = int(input('What size list do you want to create? '))
max_value = int(input('What is the max value in the list? '))
qty_tests = int(input('How many times do want to run tests? '))


def analyze_algo(func, arr):
    start = time.time()
    func(arr)
    end = time.time()
    print(f'{func.__name__}\t->\t{end-start:.5f}')

print('='*18)
for i in range(qty_tests):
    l = create_random_list(size, max_value)
    print('Iteration #', (i+1))
    analyze_algo(sorted, l)
    analyze_algo(quick_sort, l)
    analyze_algo(merging_sort, l)
    analyze_algo(insertion_sort, l.copy())
    analyze_algo(selection_sort, l.copy())
    analyze_algo(bubble_sort, l.copy())
    print('-'*30)
    
