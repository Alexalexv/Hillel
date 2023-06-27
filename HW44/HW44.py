import json
import xml.etree.ElementTree as ET

tree = ET.parse('pages.xml')
root = tree.getroot()
my_dict = {}

for element in root:
    key_0 = element.attrib['name']
    my_dict[key_0] = {}
    for sub_element in element:
        key_1 = sub_element.attrib['name']
        my_dict[key_0][key_1] = {}
        for i in sub_element:
            platform_name = i.attrib['platform']
            platform_values = [i.attrib['locator_type'], i.text]
            my_dict[key_0][key_1][platform_name] = platform_values

with open('test.json', 'w') as file:
    json.dump(my_dict, file)
