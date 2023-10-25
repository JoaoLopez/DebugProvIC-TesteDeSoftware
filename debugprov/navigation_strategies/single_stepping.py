from debugprov.navigation_strategies.navigation_strategy import NavigationStrategy
from debugprov.entities.node import Node
from debugprov.util import Validity

class SingleStepping(NavigationStrategy):
    
    def navigate(self):
        
        self.recursive_navigate(self.exec_tree.root_node)
        self.finish_navigation()
        return self.exec_tree

    def recursive_navigate(self, current_node: Node):
        
        if self.there_are_nodes_with_unknown_validity():
            if current_node.has_childrens():
                for c in current_node.childrens:
                    self.recursive_navigate(c)
            self.evaluate(current_node)  
