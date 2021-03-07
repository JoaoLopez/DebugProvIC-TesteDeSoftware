import sys
import json
from debugprov.node import Node
from prompt_toolkit.shortcuts import confirm
#from debugprov.json_manager import add_node_to_json


class ConsoleEvaluation:
    
    def evaluate_node(node: Node):
        print("-------------------------")
        print("Evaluating node {} {}".format(str(node.ev_id),node.name))
        print("Name: {}".format(node.name))
        print("Evaluation_id: {}".format(node.ev_id))
        print("Code_component_id: {}".format(node.code_component_id))
        print("Parameters: name | value ")
        for p in node.params:
            print (" {} | {} ".format(p.name, p.value))
        print("Returns: {}".format(node.retrn))
        #answer = confirm('Is correct? ')
        if str(node.ev_id) in auto_answer():
            answer = True
        else:
            answer = confirm('Is correct? ')
        return answer

def auto_answer():
    answer = False
    try:
        name = sys.argv[0][:-3]+"_auto.json"
        with open(name) as e:
            lin = e.readline().split()
    except:
        lin = []
    finally:
        return lin