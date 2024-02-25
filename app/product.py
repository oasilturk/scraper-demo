class Product:
    def __init__(self, product_id, name, images, details, description):
        self.product_id = product_id
        self.name = name
        self.images = images
        self.details = details
        self.description = description

    @staticmethod
    def map_from_xml_element(xml_element):
        product_id = xml_element.get('ProductId')
        name = xml_element.get('Name')
        images = [img.get('Path') for img in xml_element.find('Images')]

        details = {}
        for detail in xml_element.find('ProductDetails'):
            details[detail.get('Name')] = detail.get('Value')

        description_element = xml_element.find('Description')
        description = ''.join(description_element.itertext()) if description_element is not None else ''

        return Product(product_id, name, images, details, description)

    def format(self):
        self.name = self.name.capitalize()
        for key in ['Price', 'DiscountedPrice']:
            if key in self.details:
                try:
                    self.details[key] = float(self.details[key].replace(',', '.'))
                except ValueError:
                    pass

    def insert(self, db_collection):
        try:
            result = db_collection.update_one(
                {'product_id': self.product_id},
                {'$set': self.__dict__},
                upsert=True
            )
            return result
        except Exception as e:
            print(f"Error saving product to database: {e}")
            return None
