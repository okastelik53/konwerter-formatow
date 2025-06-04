import xml.etree.ElementTree as ET

def read_xml(path):
    tree = ET.parse(path)
    root = tree.getroot()
    return {root.tag: {child.tag: child.text for child in root}}
