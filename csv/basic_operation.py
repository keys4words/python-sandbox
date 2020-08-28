import csv

# reading to lines
# with open('data\data1.csv', 'r') as f:
#     reader = csv.reader(f)
#     print('Line qty:', reader.line_num)
#     print('Dialect', reader.dialect)
#     for line in reader:
#         print(line)


# reading to dict
# with open('data\data1.csv', 'r') as f:
#     reader = csv.DictReader(f)
#     print('Line qty:', reader.line_num)
#     print('Dialect', reader.dialect)
#     for line in reader:
#         print(line)


# write to csv file
# with open('data\output1.csv', 'w') as f:
#     writer = csv.writer(f, quoting=csv.QUOTE_MINIMAL)
#     writer.writerow(['1', '2', '3'])
#     writer.writerow(['1', '2', '3'])
#     writer.writerow(['1', '2', '3'])
#     writer.writerow(['1', '2', '3'])
#     writer.writerow(['1', '2', '3'])
#     writer.writerow(['1', '2', '3'])


# write dict to csv file
# with open('data\output2.csv', 'w') as f:
#     writer = csv.DictWriter(
#         f,
#         fieldnames=['first_name', 'last_name', 'age'],
#         quoting=csv.QUOTE_MINIMAL)
#     writer.writeheader()
#     writer.writerow({
#         'first_name': 'Ivan',
#         'last_name': 'Ivanov',
#         'age': 20
#     })
#     writer.writerow({
#         'first_name': 'Petr',
#         'last_name': 'Petrov',
#         'age': 26
#     })
#     writer.writerow({
#         'first_name': 'Sidor',
#         'last_name': 'Sidorov',
#         'age': 44
#     })

# write to csv file with custom dialect
# class CustomDialect(csv.Dialect):
#     quoting = csv.QUOTE_ALL
#     quotechar = "*"
#     delimiter = "!"
#     lineterminator = "\n"

# csv.register_dialect('test', CustomDialect)

# with open('data\output3.csv', 'w') as f:
#     writer = csv.writer(f, dialect='test')
#     writer.writerow([1, 44, 55])
#     writer.writerow([1, 44, 55])
#     writer.writerow([1, 44, 55])
#     writer.writerow([1, 44, 55])

# csv sniffer
sniffer = csv.Sniffer()
dialect = None

with open('data\output3.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

with open('data\output3.csv', 'r') as f:
    content = f.read()
    dialect = sniffer.sniff(content)

print(dialect.delimiter, dialect.doublequote, dialect.quoting)

with open('data\output3.csv', 'r') as f:
    reader = csv.reader(f, dialect=dialect)
    for row in reader:
        print(row)
