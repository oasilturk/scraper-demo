import xml.etree.ElementTree as ET
import logging


class XMLParser:
    def __init__(self, file_path):
        self.file_path = file_path

    def parse(self):
        logging.info(f"Parsing XML file: {self.file_path}")

        tree = ET.parse(self.file_path)
        root = tree.getroot()

        xml_elements = []
        for xml_element in root.findall("Product"):
            xml_elements.append(xml_element)

        logging.info("XML parsing completed")
        return xml_elements
