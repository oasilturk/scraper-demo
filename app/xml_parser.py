import xml.etree.ElementTree as ET

def parse(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    
    products = []
    for product in root.findall('Product'):
        product_data = {
            'product_id': product.get('ProductId'),
            'name': product.get('Name'),
            'images': [],
            'details': {},
            'description': None
        }

        for image in product.find('Images'):
            product_data['images'].append(image.get('Path'))

        for detail in product.find('ProductDetails'):
            name = detail.get('Name')
            value = detail.get('Value')
            product_data['details'][name] = value

        description = product.find('Description')
        if description is not None:
            product_data['description'] = ''.join(description.itertext())

        products.append(product_data)

    return products
