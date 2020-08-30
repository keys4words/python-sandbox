from xml.etree import ElementTree as ET
import pprint

# reading from xml file
tree = ET.parse('data/in1.xml')
root = tree.getroot()

children = list(root)
# for el in children:
#     print(el.tag, 'PK: ', el.attrib)
#     for sub_el in el:
#         print(f"\t{sub_el.tag} - > {sub_el.text}")

# create xml
root = ET.Element('record')
for i in range(10):
    sub_el = ET.SubElement(root, 'value{}'.format(i))
    sub_el.text = str(i*10)

# pprint.pprint(ET.dump(root))   # dump only for dev/tests

# create more complex data and write to file
data = [
    {'x': 10, 'y': 29, 'z': 99},
    {'x': 11, 'y': 28, 'z': 98},
    {'x': 12, 'y': 27, 'z': 97},
    {'x': 13, 'y': 26, 'z': 96},
    {'x': 14, 'y': 25, 'z': 95},
    {'x': 15, 'y': 24, 'z': 94}
]

root = ET.Element('records')
for item in data:
    record = ET.SubElement(root, 'record')
    for k, v in item.items():
        e = ET.SubElement(record, k)
        e.text = str(v)

tree = ET.ElementTree(root)
tree.write('data/out1.xml', encoding='utf-8')
