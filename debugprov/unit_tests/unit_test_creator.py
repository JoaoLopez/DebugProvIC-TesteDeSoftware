import sys, os
import shutil

from typing import List, Dict
from debugprov.unit_tests.unit_test import UnitTest
from debugprov.entities.main_script import MainScript
from debugprov.entities.node import Node

class UnitTestCreator():
    def __init__(self, main_script: MainScript, nodes: List[Node]):
        self.__main_script = main_script
        self.__nodes = nodes

    def create_unit_tests(self) -> None:
        file_path = f"test_{self.__main_script.name}"
        if os.path.isfile(file_path):
            next_round = self.__get_number_of_next_round(file_path)
        else:
            next_round = 0

        unit_tests = self.__get_all_unit_tests(next_round)
        minimized_unit_tests = self.__minimize_unit_tests(unit_tests)
        self.__create_test_file(minimized_unit_tests, file_path)

    def __get_number_of_next_round(self, file_path:str) -> int:
        with open(file_path, 'r', encoding='utf-8') as file:
            for row in file:
                pass
            next_round = int(row.split(":")[1])+1
            return next_round

    def __get_all_unit_tests(self, round_id:int) -> List[UnitTest]:
        unit_tests = []
        for nd in self.__nodes:
            test = nd.get_unit_test(self.__main_script, round_id)
            if test:
                unit_tests.append(test)
        return unit_tests
    
    def __minimize_unit_tests(self, all_unit_tests:List[UnitTest]) -> List[UnitTest]:
        tests_by_function = {}
        for unit_test in all_unit_tests:
            try:
                tests_by_function[unit_test.func_tested].append(unit_test)
            except:
                tests_by_function[unit_test.func_tested] = [unit_test]
        
        #sys.exit()
        minimized_unit_tests = []
        for tests in tests_by_function.values():
            if len(tests) == 1:
                minimized_unit_tests.extend(tests)
            else:
                minimized_unit_tests.extend(self.__get_minimum_test_set_with_max_coverage(tests))
        return minimized_unit_tests

    def __get_minimum_test_set_with_max_coverage(self, tests:List[UnitTest]) -> List[UnitTest]:
        test_a = [tests[0]]
        for i in range(1, len(tests), 1):
            test_b = [tests[i]]
            test_ab = test_a + test_b
            
            cov_a = self.__get_test_coverage_of_test_set(test_a, "test_a.py")
            cov_b = self.__get_test_coverage_of_test_set(test_b, "test_b.py")
            cov_ab = self.__get_test_coverage_of_test_set(test_ab, "test_ab.py")
            
            test_a = self.__get_best_test_set({1:[test_a, cov_a], 2:[test_b, cov_b], 3:[test_ab, cov_ab]})
        return test_a

    def __get_test_coverage_of_test_set(self, unit_tests:List[UnitTest], filename:str) -> int:
        ##print("CRIANDO TESTE FILE")
        
        self.__create_test_file(unit_tests, filename)
        coverage = self.__get_test_coverage(filename)

        ##print(coverage)


        os.system(f"rm {filename}")
        return coverage

    def __create_test_file(self, unit_tests:List[UnitTest], filename:str) -> None:
        test_code = "\n\n"
        if os.path.isfile(filename):
            next_round = self.__get_number_of_next_round(filename)
        else:
            test_code+= f'import unittest\n'
            test_code+= f'from {self.__main_script.name[:-3]} import *\n'
            for script_name in self.__main_script.imported_scripts:
                test_code+= f'from {script_name[:-3]} import *\n'
            test_code+= f'\nclass Test_{self.__main_script.name[:-3].title()}(unittest.TestCase):\n\n'
            next_round = 0

        for test in unit_tests:
            test_code += test.source_code + "\n\n"
        test_code+= f"{' '*4}# End of round: {next_round}"

        
        ##print(test_code)


        with open(filename, 'a+', encoding='utf-8') as file:
            file.write(test_code)
            
    def __get_test_coverage(self, filename:str) -> int:
        import subprocess

        os.system(f'coverage run -m unittest {filename}')
        result = subprocess.run(['coverage', 'report'], stdout=subprocess.PIPE)
        output_msg = result.stdout.decode("utf-8")
        
        coverage = 0
        for line in output_msg.split("\n"):
            words = line.split()
            if len(words) == 4 and words[0].endswith(".py") and not words[0].startswith("test_"):
                coverage += int(words[-1][:-1])
        return coverage


    def __get_best_test_set(self, tests_and_covs:Dict[List[UnitTest], int]) -> List[UnitTest]:
        best_test_set = list(tests_and_covs.keys())[0]
        for test_set in tests_and_covs:
            if tests_and_covs[test_set][1] > tests_and_covs[best_test_set][1]:
                best_test_set = test_set
            elif tests_and_covs[test_set][1] == tests_and_covs[best_test_set][1] and \
                 len(tests_and_covs[test_set][0]) < len(tests_and_covs[best_test_set][0]):
                best_test_set = test_set
        return tests_and_covs[best_test_set][0]

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
