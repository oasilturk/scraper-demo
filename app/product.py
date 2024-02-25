import logging
from datetime import datetime


class Product:
    def __init__(
        self,
        product_id,
        name,
        images,
        color,
        discounted_price,
        is_discounted,
        price,
        price_unit,
        product_type,
        quantity,
        sample_size,
        series,
        status,
        fabric,
        model_measurements,
        product_measurements,
        createdAt=None,
        updatedAt=None,
    ):
        self.stock_code = product_id
        self.name = name
        self.images = images
        self.color = [color]
        self.discounted_price = discounted_price
        self.is_discounted = is_discounted
        self.price = price
        self.price_unit = price_unit
        self.product_type = product_type
        self.quantity = quantity
        self.sample_size = sample_size
        self.series = series
        self.status = status
        self.fabric = fabric
        self.model_measurements = model_measurements
        self.product_measurements = product_measurements
        self.createdAt = createdAt if createdAt else datetime.utcnow()
        self.updatedAt = updatedAt if updatedAt else datetime.utcnow()

    @staticmethod
    def camel_to_snake(name):
        return "".join(["_" + i.lower() if i.isupper() else i for i in name]).lstrip(
            "_"
        )

    @staticmethod
    def map_from_xml_element(xml_element):
        product_id = xml_element.get("ProductId")
        name = xml_element.get("Name")
        images = [img.get("Path") for img in xml_element.find("Images")]

        product_attrs = {
            "color": [],
            "discounted_price": 0.0,
            "is_discounted": False,
            "price": 0.0,
            "price_unit": "USD",
            "product_type": "",
            "quantity": 0,
            "sample_size": "",
            "series": "",
            "status": "Active",
            "fabric": "",
            "model_measurements": "",
            "product_measurements": "",
        }

        for detail in xml_element.find("ProductDetails"):
            detail_name = Product.camel_to_snake(detail.get("Name"))
            detail_value = detail.get("Value")

            if detail_name in product_attrs:
                if detail_name in ["price", "discounted_price"]:
                    product_attrs[detail_name] = float(detail_value.replace(",", "."))
                elif detail_name == "quantity":
                    product_attrs[detail_name] = int(detail_value)
                else:
                    product_attrs[detail_name] = detail_value

        product_attrs["is_discounted"] = product_attrs["discounted_price"] > 0

        description_element = xml_element.find("Description")
        description_content = (
            "".join(description_element.itertext())
            if description_element is not None
            else ""
        )

        description_parser = DescriptionParser()
        description_parser.feed(description_content)

        product_attrs.update(
            {
                "fabric": description_parser.data.get("Kumaş Bilgisi", ""),
                "model_measurements": description_parser.data.get("Model Ölçüleri", ""),
                "product_measurements": description_parser.data.get(
                    "Ürün Ölçüleri", ""
                ),
            }
        )

        return Product(product_id=product_id, name=name, images=images, **product_attrs)

    def format(self):
        self.name = self.name.capitalize()

        if isinstance(self.price, str):
            try:
                self.price = float(self.price.replace(",", "."))
            except ValueError:
                pass

        if isinstance(self.discounted_price, str):
            try:
                self.discounted_price = float(self.discounted_price.replace(",", "."))
            except ValueError:
                pass

    def insert(self, db_collection):
        result = None

        try:
            existing_product = db_collection.find_one({"stock_code": self.stock_code})
            if existing_product is None:
                logging.info(f"Inserting new product {self.stock_code} into database")
                self.createdAt = datetime.utcnow()
                self.updatedAt = datetime.utcnow()
                result = db_collection.insert_one(self.__dict__)
                logging.info(
                    f"Product {self.stock_code} inserted successfully with ID {result.inserted_id}"
                )
            else:
                if self._is_different_from(existing_product):
                    self.updatedAt = datetime.utcnow()
                    update_data = self.__dict__.copy()
                    update_data["createdAt"] = existing_product["createdAt"]
                    logging.info(
                        f"Updating existing product {self.stock_code} in database"
                    )
                    result = db_collection.update_one(
                        {"stock_code": self.stock_code}, {"$set": update_data}
                    )
                    logging.info(f"Product {self.stock_code} updated successfully")
                else:
                    logging.info(
                        f"No changes for product {self.stock_code}. Skipping update."
                    )
                    result = None

            return result
        except Exception as e:
            logging.error(f"Error saving product {self.stock_code} to database: {e}")
            return result

    def _is_different_from(self, existing_product):
        for attr, value in self.__dict__.items():
            if attr not in ["createdAt", "updatedAt"]:
                if existing_product.get(attr) != value:
                    return True
        return False


from html.parser import HTMLParser


class DescriptionParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.data = {}
        self.current_data = ""
        self.is_li_tag = False

    def handle_starttag(self, tag, attrs):
        if tag == "li":
            self.is_li_tag = True
            self.current_data = ""

    def handle_endtag(self, tag):
        if tag == "li" and self.is_li_tag:
            self.is_li_tag = False
            key_value = self.current_data.split(":", 1)
            if len(key_value) == 2:
                key, value = key_value
                self.data[key.strip()] = value.strip()

    def handle_data(self, data):
        if self.is_li_tag:
            self.current_data += data
