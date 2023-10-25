from __future__ import unicode_literals

from graphviz import Graph

from debugprov.entities.node import Node
from debugprov.visualization.visualization import Visualization
from debugprov.util import Validity

class CustomVisualization(Visualization):

    def name_for_node(self, node:Node):
        return " {} {} '{}'".format(str(node.ev_id),node.name,str(node.retrn))

    def navigate(self, node:Node):
        chds = node.childrens
        for n in chds:
            self.graph.edge(str(node.ev_id), str(n.ev_id), None, dir='forward')
            if n.validity == Validity.INVALID:
                self.graph.node(str(n.ev_id), self.name_for_node(n), fillcolor=self.INVALID_COLOR, style='filled')
            elif n.validity == Validity.VALID: 
                self.graph.node(str(n.ev_id), self.name_for_node(n), fillcolor=self.VALID_COLOR, style='filled')
            elif n.validity == Validity.UNKNOWN:  
                self.graph.node(str(n.ev_id), self.name_for_node(n))
            elif n.validity is Validity.NOT_IN_PROV:
                self.graph.node(str(n.ev_id), self.name_for_node(n), fillcolor=self.PROV_PRUNED_NODE_COLOR, style='filled')
            
        if len(chds) > 0:
            g = Graph()
            for c in chds:
                g.node(str(c.ev_id))
            g.graph_attr['rank']='same'
            self.graph.subgraph(g)

        for n in chds: 
            self.navigate(n)