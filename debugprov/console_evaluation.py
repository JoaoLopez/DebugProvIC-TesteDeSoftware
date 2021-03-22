import sys
from debugprov.node import Node
from prompt_toolkit.shortcuts import confirm
#from debugprov.json_manager import add_node_to_json
from debugprov.json_config import get_auto_evaluation_node


class ConsoleEvaluation:
    
    def evaluate_node(node: Node):
        print("-------------------------")
        print("Evaluating node {} {}".format(str(node.ev_id),node.name))
        # print("Name: {}".format(node.name))
        # print("Evaluation_id: {}".format(node.ev_id))
        # print("Code_component_id: {}".format(node.code_component_id))
        print("Parameters: name | value ")
        for p in node.params:
            print (" {} | {} ".format(p.name, p.value))
        print("Returns: {}".format(node.retrn))
        #answer = confirm('Is correct? ')
        #answer = auto_answer(node.ev_id)
        answer = get_auto_evaluation_node(node.ev_id)
        if not answer:
            node.retrn = input("What is the expected return?")
        return answer


def auto_answer(ev_id):
    '''
    duas metodologias:
        - sinal vermelho     = Os nós que estão listados DEVEM parar
            Pede confirmação somente dos nós da lista                    
            confirm() if x not in lista else True
        
        - sinal verde        = Os nós que estão listados PASSAM automaticamente
            Pede confirmação somente dos nós que não estão na lista      
            confirm() if x in lista else True
    '''
    ev_id = str(ev_id)
    name = sys.argv[0][:-3]+"_spots.txt"
    try:
        with open(name) as e:
            #print("File exists")
            lin = e.readline().split()
            if lin[0].startswith("hot"):
                return confirm('Is correct? ') if ev_id in lin else True
            else:
                return confirm('Is correct? ') if ev_id not in lin else True
    except:
        print(f"File <{name}>does not exists")
        return confirm('Is correct? ')
    