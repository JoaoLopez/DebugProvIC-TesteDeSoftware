from debugprov.parameter import Parameter
from debugprov.validity import Validity

class Node:
    
    def __init__(self, ev_id, code_component_id, retrn, name, parent):
        self.ev_id = ev_id
        self.code_component_id = code_component_id
        self.retrn = retrn
        self.name = name
        self.function_name = self.name[:self.name.find("(")]
        self.parent = parent
        self.childrens = []
        self.permanent_childrens = []
        self.validity = Validity.UNKNOWN
        self.params = []
        self.tree = []

    def has_childrens(self):
        return len(self.childrens) > 0

    def get_root(self):
        foo = self
        while foo.parent:
            foo = foo.parent
        self.root = foo
        foo.tree.append(self)

    def has_childrens_with_validity(self, validity:Validity):
        for c in self.childrens:
            if c.validity is validity:
                return True
        return False 
    
    def all_childrens_are_valid(self):
        for chd in self.childrens:
            if chd.validity is not Validity.VALID:
                return False
        return True

    def get_parameters(self, cursor):
        query = ("select CC.name, EV.repr as 'value' "
                 "from code_component CC "
                 "join evaluation EV on EV.code_component_id = CC.id "
                 "join dependency D on D.dependency_id = EV.id "
                 "where D.type = 'argument' " 
                 "and D.dependent_id = ? ")
        for tupl in cursor.execute(query, [self.ev_id]):
            self.params.append(Parameter(tupl[0], tupl[1]))

    def node_to_test(self, nbs):
        lines = ""
        if self.revised:            
            lines = ""
            lines+=f'{" "*4}def test_node_{self.ev_id}_{nbs}(self):\n'
            retrn = f"{' '*8}self.assertEqual({self.function_name}("
            for n, param in enumerate(self.params):
                lines+=f"{' '*8}var_{n} = {param.value}\n" 
                retrn+=f'var_{n}, '
            retrn+=f"), {self.retrn})\n"
            lines+=retrn
            lines+='\n\n'
            print(lines)
            #with open(SCRIPT_NAME, 'a', encoding='utf-8') as opt:
            #    opt.write(lines)
        return lines    
    
    def get_name(self):
        return "{} {}".format(self.ev_id, self.name)