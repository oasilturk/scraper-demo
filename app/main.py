import os
import config
from xml_parser import XMLParser
from product import Product
from database import Database


def main():
    db = Database()
    collection = db.get_collection()

    file_path = os.path.join(config.APP_ABS_PATH, "..", "lonca-sample.xml")
    xml_parser = XMLParser(file_path)
    xml_elements = xml_parser.parse()
    for xml_element in xml_elements:
        product = Product.map_from_xml_element(xml_element)
        product.format()
        product.insert(collection)


if __name__ == "__main__":
    main()
