import xml.etree.ElementTree as ET

class XMLParser:
    def __init__(self, file_path):
        self.file_path = file_path

    def parse(self):
        tree = ET.parse(self.file_path)
        root = tree.getroot()

        xml_elements = []
        for xml_element in root.findall("Product"):
            xml_elements.append(xml_element)

        return xml_elements
