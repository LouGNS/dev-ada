import csv

with open('data.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    data = [row for row in reader]


import xml.etree.ElementTree as ET

root = ET.Element('data')
for row in data:
    item = ET.SubElement(root, 'item')
    for key, value in row.items():
        child = ET.SubElement(item, key)
        child.text = value


tree = ET.ElementTree(root)
tree.write('data.xml')
