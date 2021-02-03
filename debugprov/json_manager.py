import json
import sys
import os
from pprint import pprint

def create_json(new_data = {}):
    with open(name_json(), "w") as json_file:
        json.dump(new_data, json_file, indent=4)

def add_node_to_json(node):
    try:
        with open(name_json(), 'r') as json_file:
            my_json = json.load(json_file)
    except:
        my_json = dict()
    print("==dicio==")
    node_dict = node.__dict__
    print(node)
    pprint(my_json)
    my_json[nodo['ev_id']] = node_dict 
    create_json(my_json)

def name_json():
    return f"{sys.argv[0][:-3]}.json"