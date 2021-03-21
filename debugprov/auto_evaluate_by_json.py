import json
import sys

def read_json()
    with open('debugprov_params.json', 'r') as json_file:
        data = json.load(json_file)
    return data
    
def get_at_json(key, default_value):
    '''
    No json o provenance pode ter os seguintes valores:
    ('[0] - Para não usar provenance alguma')
    ('[1] - Use the last print as criterion')
    ('[2] - Use a wrong output as criterion')
    ('[3] - Select node as criterion')
    ('[4]' - Para perguntar qual provenance usar)
    '''
    data = read_json()
    module = module.name
    
    if data.get('auto_navegation').get(module):
        if data.get('auto_navegation').get(module).get(key):
            default_value = data.get('auto_navegation').get(module).get(key)
    elif data.get(key):
        default_value = data.get(provenance)
    return default_value


def get_provenance_criteria(prov = None):
    if prov is None:
        prov = get_at_json('use_prov', 0)
    if 0<prov<5:
        prov = 0
    elif prov == 4:
        print("How do you want to perform the enhancement? ")
        print('[1] - Use the last print as criterion')
        print('[2] - Use a wrong output as criterion')
        print('[3] - Select node as criterion')
        prov = int(prompt('> '))
    return prov

def get_strategy(nav_names):
    strategy = get_at_json("navegation_strategy", 1)
    if 0<strategy<5:
        for idx,obj in enumerate(nav_names):
            print('[{}] - {}'.format(str(idx+1),obj))
        strategy = prompt('> ')
    return strategy

def show_tree():
    show = bool(get_at_json('show_tree', False))
    return show

def get_auto_evaluation_node(nodo):
    conj = set(get_at_json("nodes"), [])
    should_ask_for_confirmation = nodo in conj
    everything_passes_except = get_at_json("everything passes except", True)
    if not everything_passes_except:
        should_ask_for_confirmation=not(should_ask_for_confirmation)
    if should_ask_for_confirmation:
        should_ask_for_confirmation = confirm("[Y/n]")
        
    return should_ask_for_confirmation
    

def module_name():
    return sys.argv[0]