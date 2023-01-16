from core.services.Providers import Provider
from xml_provider.services.XmlService import parse_xml


class XmlProvider(Provider):
    def identifier(self):
        return "xml_provider"

    def name(self):
        return "XML provider"

    def load(self, graph_name, graph_description, xml_doc):
        parse_xml(graph_name, graph_description, xml_doc)
        print(graph_name)
        print(graph_description)
        print(xml_doc)
