import json
from bson import ObjectId
import datetime

class PrefixMiddleware(object):

    def __init__(self, app, prefix=''):
        self.app = app
        self.prefix = prefix

    def __call__(self, environ, start_response):

        if environ['PATH_INFO'].startswith(self.prefix):
            environ['PATH_INFO'] = environ['PATH_INFO'][len(self.prefix):]
            environ['SCRIPT_NAME'] = self.prefix
            return self.app(environ, start_response)
        else:
            start_response('404', [('Content-Type', 'text/plain')])
            return ["This url does not belong to the app.".encode()]



def dictify_document(doc):
    return doc.to_mongo().to_dict()


class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        if isinstance(o, datetime.datetime):
            return o.strftime('%Y-%m-%dT%H:%M:%SZ')
        return json.JSONEncoder.default(self, o)


def fetchCityStates():
    import json
    with open('data/city_states.json') as f:
        data = json.load(f)
    return data


def deliveryMapping():
    import json
    with open('data/delivery_charge_mapping.json') as f:
        data = json.load(f)
    return data


def fetchVariantMapping():
    import json
    with open('data/variant_mapping.json') as f:
        data = json.load(f)
    return data


def fetchSterilizationData():
    import json
    with open('data/sterilization_data.json') as f:
        data = json.load(f)
    return data


def updateProducts(data):
    import json
    with open('data/akeneo_products.json', 'w') as p:
        json.dump(data['product_data'], p, indent=4)
    with open('data/akeneo_family.json', 'w') as f:
        json.dump(data['family_data'], f, indent=4)
    with open('data/akeneo_category.json', 'w') as c:
        json.dump(data['category_data'], c, indent=4)
    return data


def fetchProductsFromJson():
    import json
    with open('data/akeneo_products.json') as p:
        data = json.load(p)
    return data


def fetchFamiliesFromJson():
    import json
    with open('data/akeneo_family.json') as f:
        data = json.load(f)
    return data


def fetchCategoriesFromJson():
    import json
    with open('data/akeneo_category.json') as c:
        data = json.load(c)
    return data


def fetchTransportersList():
    import json
    with open('data/transporters_list.json') as f:
        data = json.load(f)
    return data





