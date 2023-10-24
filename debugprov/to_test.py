import sys, os
import shutil

def serialize_new_tests(all_nodes):
    FILENAME = f"test_{sys.argv[0]}"
    MODULE = sys.argv[0][:-3]
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
        base+= f'from {MODULE} import *\n\n'
        base+= f'class Test_{MODULE.title()}(unittest.TestCase):\n\n'
        nps = 0
        
    for nd in all_nodes:
        base+=(nd.node_to_test(nps))
    
    base+= f"{' '*4}# End of round: {nps}"
    with open(FILENAME, 'a', encoding='utf-8') as file:
        file.write(base)
    
def execute_coverage():
    '''
    Executa o coverage do teste
    Move os dados de cobertura para ..\coverage_data\{script}\{n}
    '''
    MODULE = sys.argv[0][:-3]
    os.system(f'coverage run -m unittest test_{MODULE}.py')
    if not os.path.isdir("coverage_data"):
        os.mkdir('coverage_data')
    PATH = os.path.join("coverage_data", MODULE)
    if not os.path.isdir(PATH):
        os.mkdir(PATH)
    total_files = len(os.listdir(PATH))
    PATH = os.path.join(PATH, f"{str(total_files).zfill(2)}_{MODULE}")
    os.mkdir(PATH)
    os.system("coverage html")
    
    shutil.move("htmlcov", PATH)
    shutil.copy(f"test_{MODULE}.py", os.path.join(PATH, f"test_{MODULE}.txt"))
