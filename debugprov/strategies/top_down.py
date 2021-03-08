from debugprov.navegation.navgiation_strategy import NavigationStrategy
from debugprov.node import Node
from debugprov.validity import Validity

class TopDown(NavigationStrategy):

    def navigate(self):
        self.recursive_navigate(self.exec_tree.root_node)
        self.finish_navigation()
        return self.exec_tree

    def recursive_navigate(self, node: Node):
        if self.there_are_nodes_with_unknown_validity():
            self.evaluate(node)
            if node.validity is not Validity.VALID:
                for n in node.childrens:
                    self.recursive_navigate(n)
