import datetime
import json
from core.models import Node, Graph
from typing import Dict
from hashlib import md5
import os

def convert_jsonfile_to_data_structure(filename:str):
    with open(filename) as f:
        js_graph = json.load(f)
    return js_graph

def generate_graph(graph_name):
    graph = Graph(name=graph_name)
    graph.save()
    json_data_structure = convert_jsonfile_to_data_structure("..\ml-provider\ml_provider\examples\example.json")
    generate_nodes_from_json(graph, json_data_structure)

    return graph

def hash_json_object(object:Dict):
    dhash = md5()
    encoded = json.dumps(object, sort_keys=True).encode()
    dhash.update(encoded)
    return dhash.hexdigest()

def create_node(graph, potential_node, nodes_dict):
        hashed_dict_value = hash_json_object(potential_node)
        if hashed_dict_value not in nodes_dict:
            new_node = Node(atributes={})
            graph.add_node(new_node)           
            nodes_dict[hashed_dict_value] = new_node
        return hashed_dict_value

def create_graph_root_nodes(graph, json_data_structure, nodes_dict, json_objects_fifo):
    if isinstance(json_data_structure,dict):
        create_node(graph, json_data_structure, nodes_dict)
        json_objects_fifo.append(json_data_structure)

    elif isinstance(json_data_structure,list):
        for list_input in json_data_structure:
            create_node(graph, list_input, nodes_dict)
            json_objects_fifo.append(list_input)

def parse_attribute_value(value):
    try:
        attribute_value = datetime.datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%fZ')
    except:
        
        try:
            attribute_value = float(value)
        except:
            try:
                attribute_value = str(value)
            except:
                attribute_value = None
    return attribute_value

def connecting_new_node(parent, child_json_object, nodes_dict, json_objects_fifo, graph):
    hashed_dict_value = create_node(graph, child_json_object, nodes_dict)
    parent.add_neighbour(nodes_dict[hashed_dict_value])
    json_objects_fifo.append(child_json_object)

def breadth_searching_nodes(graph, nodes_dict, json_objects_fifo):
    while len(json_objects_fifo) > 0:
        json_object = json_objects_fifo.pop(0)
        json_hash = hash_json_object(json_object)
        node = nodes_dict[json_hash]
        for key in json_object:

            if isinstance(json_object[key], dict):
                connecting_new_node(node, json_object[key], nodes_dict, json_objects_fifo, graph)

            elif isinstance(json_object[key], list):
                if all(isinstance(list_input, dict) for list_input in json_object[key]):
                    for list_input in json_object[key]:
                        connecting_new_node(node, list_input, nodes_dict, json_objects_fifo, graph)
                else:
                    list_of_attribute_values = []
                    for attribute_value in json_object[key]:
                        parsed_attribute_value = parse_attribute_value(attribute_value)
                        if parsed_attribute_value != None:
                                list_of_attribute_values.append(parsed_attribute_value)

                    node.add_atribute(key, list_of_attribute_values)
            else:
                attribute_value = parse_attribute_value(json_object[key])
                if attribute_value != None:
                    node.add_atribute(key, attribute_value)

def generate_nodes_from_json(graph, json_data_structure):
    nodes_dict = {}
    json_objects_fifo = []

    create_graph_root_nodes(graph, json_data_structure, nodes_dict, json_objects_fifo)
    breadth_searching_nodes(graph, nodes_dict, json_objects_fifo)
      