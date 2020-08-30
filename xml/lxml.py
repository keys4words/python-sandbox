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
parser = et.XMLParser(target=PersonTarget())
tree = et.parse(infile, parser)

res = tree.getroot()

for el in res:
    print(el)
# pprint.pprint(res)
