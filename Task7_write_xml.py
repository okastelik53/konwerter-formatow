import xml.etree.ElementTree as ET

def write_xml(path, data):
    root_tag = list(data.keys())[0]
    root = ET.Element(root_tag)
    for k, v in data[root_tag].items():
        ET.SubElement(root, k).text = str(v)
    tree = ET.ElementTree(root)
    tree.write(path, encoding='unicode')
