import unittest
import sys

from debugprov.navigation_strategies.navigation_strategy import NavigationStrategy
from debugprov.execution_tree.execution_tree import ExecutionTree
from debugprov.entities.node import Node

class NavigationStrategyTest(unittest.TestCase):

    def test_create(self):
        root = Node(1, 1, None, 'a-script.py', None)
        exec_tree = ExecutionTree(root)
        nav = NavigationStrategy(exec_tree)
        self.assertEqual(nav.exec_tree, exec_tree)


if __name__ == '__main__':
    unittest.main()