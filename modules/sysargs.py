import sys
import os.path

# print(sys.argv)
# print(sys.path)
# module_juja = os.path.join('..', 'juja')
# print(module_juja)


current_folder = os.path.dirname(os.path.abspath(__file__))
parent_path = os.path.dirname(current_folder)
module_juja = os.path.join(parent_path, 'juja')
# print('---', module_juja)
sys.path.append(module_juja)

import house

house_gen = house.NumberGenerator()
for _ in range(5):
    print(house_gen.get_next())