from core.services.Providers import Provider


class XmlProvider(Provider):
    def identifier(self):
        return "xml_provider"

    def name(self):
        return "XML provider"

    def load(self, graph_name, graph_description, xml_doc):
        print(graph_name)
        print(graph_description)
        print(xml_doc)