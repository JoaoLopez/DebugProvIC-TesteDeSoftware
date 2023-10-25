import sys, os
import shutil

from typing import List
from debugprov.entities.main_script import MainScript
from debugprov.entities.node import Node

def __get_number_of_next_round(file_path:str):
    with open(file_path, 'r', encoding='utf-8') as file:
        for row in file:
            pass
        next_round = int(row.split(":")[1])+1
        return next_round
    
def create_unit_tests(main_script: MainScript, all_nodes: List[Node]):
    file_path = f"test_{main_script.name}"
    test_code = "\n\n"

    if os.path.isfile(file_path):
        next_round = __get_number_of_next_round(file_path)
    else:
        test_code+= f'import unittest\n'
        test_code+= f'from {main_script.name[:-3]} import *\n'
        for script_name in main_script.imported_scripts:
            test_code+= f'from {script_name[:-3]} import *\n'
        test_code+= f'\nclass Test_{main_script.name[:-3].title()}(unittest.TestCase):\n\n'
        next_round = 0
        
    for nd in all_nodes:
        test_code+=(nd.get_test_code(main_script, next_round))
    
    test_code+= f"{' '*4}# End of round: {next_round}"
    with open(file_path, 'a+', encoding='utf-8') as file:
        file.write(test_code)
    
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
