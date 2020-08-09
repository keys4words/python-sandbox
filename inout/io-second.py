filename = 'inout/data/data2.txt'

with open(filename) as f:
    lines = f.readlines()

lines.insert(1, 'inserted line\n')

with open(filename, 'w') as f:
    f.writelines(lines)