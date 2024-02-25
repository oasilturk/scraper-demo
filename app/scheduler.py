from apscheduler.schedulers.background import BackgroundScheduler
from xml_parser import XMLParser
from database import Database
from product import Product
import os


class Scheduler:
    def __init__(self, interval_seconds):
        self.scheduler = BackgroundScheduler()
        self.interval_seconds = interval_seconds

    def start(self):
        self.scheduler.add_job(self.job, "interval", seconds=self.interval_seconds)
        self.scheduler.start()

    def job(self):
        db = Database()
        collection = db.get_collection()

        xml_file_path = os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "..", "lonca-sample.xml"
        )
        xml_parser = XMLParser(xml_file_path)
        xml_elements = xml_parser.parse()

        for xml_element in xml_elements:
            product = Product.map_from_xml_element(xml_element)
            product.format()
            product.insert(collection)

    def stop(self):
        self.scheduler.shutdown()
