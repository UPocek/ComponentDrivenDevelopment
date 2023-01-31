import xml.etree.ElementTree as ET
from core.models import Graph, Node
_graph = None
_map = {}



def parse_xml(graph_name, graph_description, xml_doc):
    root, node = get_root(graph_name, xml_doc)
    find_nodes(root, node)


def get_root(graph_name, xml_doc):
    global _graph
    _graph = Graph(name=graph_name)
    _graph.save()
    tree = ET.parse('../xml_provider/xml_provider/uploaded_data/' + xml_doc)
    root = tree.getroot()
    node = Node(atributes={"title": root.tag})
    _graph.add_node(node)
    return root, node


def find_nodes(root, parent):
    global _graph
    for child in root:
        attributes = {"title": child.tag}
        if len(child.getchildren()) == 0:
            child_node = make_leaf_node(child)
            parent.add_neighbour(child_node)
            continue

        for attribute in child.attrib.keys():
            attributes[attribute] = child.attrib[attribute]
        node = Node(atributes=attributes)
        _graph.add_node(node)
        parent.add_neighbour(node)
        find_nodes(child, node)


def make_leaf_node(leaf_node):
    global _graph, _map
    if leaf_node.tag+leaf_node.text not in _map.keys():
        node = Node(atributes={"title": leaf_node.tag, "value": leaf_node.text})
        _graph.add_node(node)
        _map[leaf_node.tag+leaf_node.text] = node
        return node
    return _map[leaf_node.tag+leaf_node.text]
