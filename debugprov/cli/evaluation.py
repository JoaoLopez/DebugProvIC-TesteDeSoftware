from ast import literal_eval
from debugprov.entities.node import Node
from debugprov.entities.main_script import MainScript
from prompt_toolkit.shortcuts import confirm

def evaluate_node(node: Node, main_script:MainScript):
    print("-------------------------")
    print("Evaluating node {} {}".format(str(node.ev_id),node.name))
    # print("Name: {}".format(node.name))
    # print("Evaluation_id: {}".format(node.ev_id))
    # print("Code_component_id: {}".format(node.code_component_id))
    print("Parameters: name | value ")
    for p in node.params:
        print (" {} | {} ".format(p.name, p.value))
    print("Returns: {}".format(node.retrn))
    answer = confirm('Is correct? ')
    #answer = True
    if not answer:
        node.retrn = literal_eval(input("What would be the correct answer?"))
    
    if node.will_possibly_be_testable(main_script):
        is_safe = confirm('Is this function safe for testing (is it pure and side-effect free)? ')
        main_script.set_function_safe_for_testing(node.function_name, is_safe)
    
    node.revised = True
    return answer
