from typing import Optional
from debugprov.unit_tests.unit_test import UnitTest
from debugprov.entities.main_script import MainScript
from debugprov.util import Validity

class Parameter:
    def __init__(self, name, value):
        self.name = name
        self.value = value

class Node:
    def __init__(self, ev_id, code_component_id, retrn, name, parent):
        self.ev_id = ev_id
        self.code_component_id = code_component_id
        self.retrn = retrn
        self.name = name
        self.function_name = self.name[:self.name.find("(")]
        self.parent = parent
        self.children = []
        self.permanent_children = []
        self.validity = Validity.UNKNOWN
        self.params = []
        self.tree = []
        self.revised = False

    def has_children(self):
        return len(self.children) > 0

    def get_root(self):
        foo = self
        while foo.parent:
            foo = foo.parent
        self.root = foo
        foo.tree.append(self)

    def has_childrens_with_validity(self, validity:Validity):
        for c in self.children:
            if c.validity is validity:
                return True
        return False 
    
    def all_childrens_are_valid(self):
        for chd in self.children:
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

    def will_possibly_be_testable(self, main_script):
        #Note: if "main_script.is_a_testable_function(self.function_name)" returns True, this node is certainly testable not possibly, so we return False.
        return all([self.ev_id != 1, main_script.is_a_testable_function(self.function_name) is None])

    def __clean_function_name(self):
        #if the function name is on the form "MODULE.FUNCTION" it will be set to "FUNCTION"
        last_dot = self.function_name.rfind(".")
        if last_dot != -1:
            self.function_name = self.function_name[last_dot+1:]

    def __is_testable(self, main_script):        
        return all([self.ev_id != 1, main_script.is_a_testable_function(self.function_name), self.revised])

    def __get_unit_test_code(self, round_id:int) -> str:
        test_code = f'{" "*4}def test_{self.function_name}_{self.ev_id}_{round_id}(self):\n'
        for param in self.params:
            test_code += f"{' '*8}{param.name} = {param.value}\n" 
        
        test_code += f"{' '*8}self.assertEqual({self.function_name}("
        for param in self.params:
            test_code += f"{param.name}, "

        test_code += f"), {self.retrn})\n\n"
        return test_code

    def get_unit_test(self, main_script:MainScript, round_id:int) -> Optional[UnitTest]:
        if self.__is_testable(main_script):
            self.__clean_function_name()
            test_code = self.__get_unit_test_code(round_id)
            return UnitTest(self.function_name, test_code)
            
    def get_name(self):
        return "{} {}".format(self.ev_id, self.name)
