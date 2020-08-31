# from lxml import etree as ET
import xml.etree.ElementTree as et
import pprint
import csv


class PersonTarget:
    def __init__(self):
        self.records = []
        self.current_index = None
        self.current_node = None

    def start(self, tag, attrib):
        if tag == 'person':
            self.records.append({
                'first_name': '',
                'last_name': '',
                'age': None
            })
            self.current_index = len(self.records) - 1
        self.current_node = tag

    def end(self, tag):
        self.current_node = ''

    def data(self, data):
        if self.current_node in ['first_name', 'last_name', 'age']:
            self.records[self.current_index][self.current_node] = data

    def close(self):
        return self.records



infile = 'data/in2.xml'
# target parser
# parser = et.XMLParser(target=PersonTarget())
# tree = et.parse(infile, parser)

# xpath parser
tree = et.parse(infile)
res = tree.getroot()

# for el in res:
    # print(el)
# pprint.pprint(res)
for student in res:
    print('PK: ', (student.attrib, student.get('pk')))
    print(f"\t{student.find('./first_name').text}")
    print(f"\t{student.find('./last_name').text}")
    print(f"\t{student.find('./age').text}")


first_names = res.findall('./person/first_name')
last_names = res.findall('./person/last_name')
ages = res.findall('./person/age')

for values in zip(first_names, last_names, ages):
    row = {value.tag: value.text for value in values}
    print(row)

z = zip(['a', 'b', 'c'], [10, 20, 30], ['one', 'second', 'third'])
pprint.pprint(list(z))
