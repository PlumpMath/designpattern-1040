from xml.etree import ElementTree
import json


class JSONConnector:
    def __init__(self, filepath):
        self.data = {}
        with open(filepath, encoding="utf-8") as f:
            self.data = json.load(f)

    @property
    def parsed_data(self):
        return self.data


class XMLConnector:
    def __init__(self, filepath):
        self.tree = ElementTree.parse(filepath)

    @property
    def parsed_data(self):
        return self.tree


def connector_factory(filepath):
    if filepath.endswith(".json"):
        connector = JSONConnector
    elif filepath.endswith(".xml"):
        connector = XMLConnector
    else:
        raise ValueError("Cannot connect to {}".format(filepath))

    return connector(filepath)


def connect_to(filepath):
    connector = None
    try:
        connector = connector_factory(filepath)
    except ValueError as ve:
        print(ve)
    return connector


if __name__ == '__main__':
    # sqlite
    sqlite_connector = connect_to("data/person.sq3")
    print()

    # xml
    xml_connector = connect_to("data/person.xml")
    xml_data = xml_connector.parsed_data
    liars = xml_data.findall(".//{}[{}='{}']".format("person", "lastName", "Liar"))
    print("* found: {} Liars.".format(len(liars)))
    for liar in liars:
        print("first name: {}".format(liar.find("firstName").text))
        print("last name: {}".format(liar.find("lastName").text))
        for p in liar.find("phoneNumbers"):
            print("phone number ({}):".format(p.attrib["type"]), p.text)
        print()
    print()

    # json
    json_connector = connect_to("data/dount.json")
    json_data = json_connector.parsed_data
    print("* found: {} dounts".format(len(json_data)))
    for dount in json_data:
        print("name: {}".format(dount["name"]))
        print("price: ${}".format(dount["ppu"]))
        for t in dount["topping"]:
            print("topping: {} {}".format(t["id"], t["type"]))
        print()
    print()