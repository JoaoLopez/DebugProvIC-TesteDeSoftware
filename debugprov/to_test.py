import sys

def serialize_new_tests(all_nodes):
    FILENAME = f"test_{sys.argv[0]}"
    print("FILENAME: ", FILENAME)
    base = "\n\n"
    try:
        with open(FILENAME, 'r', encoding='utf-8') as file:
            for row in file:
                pass
            nps = int(row.split(":")[1])+1
    except:
        with open(FILENAME, 'w', encoding='utf-8') as file:
            pass
        base+= f'import unittest\n'
        base+= f'from {FILENAME} import *\n\n'
        base+= f'class {FILENAME[:-3].title()}(unittest.TestCase):\n\n'
        nps = 0
        
    for nd in all_nodes:
        base+=(nd.node_to_test(nps))
    
    base+= f"{' '*4}# End of round: {nps}"
    with open(FILENAME, 'a', encoding='utf-8') as file:
        file.write(base)
    
        