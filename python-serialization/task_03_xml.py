#!/usr/bin/python3


import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):

    root = ET.Element("data")

    for key, value in dictionary.items():
        item = ET.SubElement(root, "item", key=key)
        item.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename)


def deserialize_from_xml(filename):

    tree = ET.parse(filename)
    root = tree.getroot()

    dictionary = {}
    for item in root.findall('item'):
        key = item.get('key')
        value = item.text
        dictionary[key] = value

    return dictionary
