from __future__ import unicode_literals

import os
import sqlite3

from prompt_toolkit.shortcuts import prompt

from debugprov.entities.main_script import MainScript
from debugprov.script_analysis.main_script_analyser import MainScriptAnalyser

from debugprov.execution_tree.execution_tree_creator import ExecTreeCreator
from debugprov.navigation_strategies.top_down import TopDown
from debugprov.navigation_strategies.heaviest_first import HeaviestFirst
from debugprov.visualization.visualization import Visualization
from debugprov.provenance_enhancement.provenance_enhancement import ProvenanceEnhancement
from debugprov.navigation_strategies.single_stepping import SingleStepping
from debugprov.navigation_strategies.divide_and_query import DivideAndQuery
from debugprov.unit_tests.unit_test_creator import execute_coverage, UnitTestCreator

class ConsoleInterface:

    DEFAULT_SQLITE_PATH = '.noworkflow/db.sqlite'
    NAVIGATION_STRATEGIES = [SingleStepping, TopDown, HeaviestFirst, DivideAndQuery] 

    def __init__(self):
        self.db_path = self.DEFAULT_SQLITE_PATH

    def ask_output_file_name(self):
        out_filename = prompt('Output file name: ', default='exec_tree')
        return out_filename
        
    def ask_wrong_data(self):
        print("Tell me which output data is wrong ")
        wrong_data = prompt('> ')
        return wrong_data
        
    def ask_use_wrong_data(self):
        ans = 0
        while (ans != 1 and ans != 2 and ans != 3):
            print("How do you want to perform the enhancement? ")
            print('[1] - Use the last print as criterion')
            print('[2] - Use a wrong output as criterion')
            print('[3] - Select node as criterion')
            ans = int(prompt('> '))
        return ans

    def ask_use_prov(self):
        #return confirm('Do you want to use provenance enhancement? ')
        return False

    def select_nav_strategy(self):
        nav_names = [n.__name__ for n in self.NAVIGATION_STRATEGIES]
        print("Choose a navigation strategy: ")
        for idx,obj in enumerate(nav_names):
            print('[{}] - {}'.format(str(idx+1),obj))
        #ans = prompt('> ')
        ans = 1    #remover mais tarde
        return self.NAVIGATION_STRATEGIES[int(ans)-1] 

    def open_db(self):
        try:
            cursor = sqlite3.connect(self.db_path).cursor()
            return cursor
        except:
            raise Exception('Error reading database!')  
        
    def analyze_main_script(self):
        MainScriptAnalyser(self.main_script).analyse()

    def create_main_script(self, main_script_path):
        exp_base_dir, main_script_name = os.path.split(main_script_path)    
        return MainScript(exp_base_dir, main_script_name)
        
    def run(self):
        import sys
        self.main_script = self.create_main_script(sys.argv[0])
        self.analyze_main_script()
 
        cursor = self.open_db()
        creator = ExecTreeCreator(cursor)
        exec_tree = creator.create_exec_tree()

        self.choosen_nav_strategy = self.select_nav_strategy()
        nav = self.choosen_nav_strategy(exec_tree, self.main_script)
        if self.ask_use_prov():
            prov = ProvenanceEnhancement(exec_tree, cursor)
            strategy = self.ask_use_wrong_data() 
            if strategy == 1:
                # Slice Criterion: last print
                wrong_data_id = prov.get_last_print_evid()
                prov.enhance(wrong_data_id)
            elif strategy == 2:
                # Slice criterion: Wrong output (informed by user)
                wrong_data = self.ask_wrong_data()
                wrong_data_id = prov.get_wrong_data_evid(wrong_data)
                prov.enhance(wrong_data_id)
            elif strategy == 3:
                # Slice criterion: Node in tree (informed by user)
                tmp_vis = Visualization(exec_tree)
                tmp_vis.view_exec_tree('tmp_tree')
                print("Tell me which ID ")
                ev_id = int(prompt('> '))
                prov.enhance(ev_id)
    
        result_tree = nav.navigate()
        file_name = self.ask_output_file_name()
        vis = Visualization(result_tree)
        UnitTestCreator(self.main_script, exec_tree.get_all_nodes()).create_unit_tests()
        execute_coverage()
        vis.view_exec_tree(file_name)
    