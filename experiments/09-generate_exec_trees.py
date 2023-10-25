import os
import sqlite3

from graphviz import Graph
from debugprov.util import Validity
from debugprov.entities.node import Node
from debugprov.execution_tree.execution_tree import ExecutionTree
from debugprov.execution_tree.execution_tree_creator import ExecTreeCreator
from debugprov.navigation_strategies.top_down import TopDown
from debugprov.navigation_strategies.heaviest_first import HeaviestFirst
from debugprov.visualization.visualization import Visualization
from debugprov.provenance_enhancement.provenance_enhancement import ProvenanceEnhancement 
from debugprov.navigation_strategies.single_stepping import SingleStepping
from debugprov.navigation_strategies.divide_and_query import DivideAndQuery

from config import Config

config = Config()
config.go_to_scripts_path()

def generate_exec_trees(scripts):
    for script_path in scripts:
        print(script_path)
        directory = script_path.split('/')[0]
        os.chdir(script_path)
        os.chdir(config.mutants_with_wrong_result)
        for mutant_dir in os.listdir():
            os.chdir(mutant_dir)
            now2_sqlite_path = os.getcwd() + '/.noworkflow/db.sqlite'
            cursor = sqlite3.connect(now2_sqlite_path).cursor()
            exec_tree = ExecTreeCreator(cursor).create_exec_tree()
            vis = Visualization(exec_tree)
            vis.generate_exec_tree()
            vis.graph.render(filename='exec_tree',format='pdf')
            print('Rendering: '+os.getcwd()+'/exec_tree.pdf')
            os.chdir('..')
        os.chdir('../..')
            
generate_exec_trees(config.target_scripts)