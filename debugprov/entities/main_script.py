from typing import Optional
import ast

class MainScript():
    def __init__(self, base_dir, main_script_name):
        self.__base_dir = base_dir
        self.__name = main_script_name
        self.__AST = None
        self.__import_commands = None
        self.__imported_scripts = None
        self.__functions = None

    def __get_user_defined_function(self, function_name:str) -> Optional[ast.FunctionDef]:
        if function_name in self.functions:
            return self.functions[function_name]
        
        for script in self.imported_scripts.values():
            for func in script.functions:
                if function_name in [func, ".".join([script.name[:-3], func])]:
                    return script.functions[func]

    def is_a_testable_function(self, function_name:str) -> Optional[bool]:
        func = self.__get_user_defined_function(function_name)

        if func is None: #it is not an user defined function
            return False

        if not hasattr(func, "safe_for_testing"):
            func.safe_for_testing = None

        return func.safe_for_testing
        
    def set_function_safe_for_testing(self, function_name:str, value:bool):
        func = self.__get_user_defined_function(function_name)
        func.safe_for_testing = value
        
    ###DEBUG####
    def print(self, indent=0):
        print(indent * " " + "##### MAIN SCRIPT #####")
        print(indent * " " + "    base_dir:", self.__base_dir)
        print(indent * " " + "    Name:", self.__name)
        print(indent * " " + "    AST:", ast.dump(self.__AST))
        print(indent * " " + "    Import Commands:")
        for command in self.__import_commands:
            print(indent * " " + "        " + ast.dump(command))
        print(indent * " " + "    Imported Scripts:")
        for script in self.__imported_scripts:
            print(indent * " " + "        " + self.__imported_scripts[script].name)
        print(indent * " " + "    Functions:", self.__functions)



        for script in self.__imported_scripts:
            self.__imported_scripts[script].print(indent+4)     
   
    @property
    def base_dir(self):
        return self.__base_dir
   
    @property
    def name(self):
        return self.__name

    @property
    def AST(self):
        return self.__AST

    @AST.setter
    def AST(self, AST):
        self.__AST = AST

    @property
    def import_commands(self):
        return self.__import_commands

    @import_commands.setter
    def import_commands(self, import_commands):
        self.__import_commands = import_commands
    
    @property
    def imported_scripts(self):
        return self.__imported_scripts

    @imported_scripts.setter
    def imported_scripts(self, imported_scripts):
        self.__imported_scripts = imported_scripts

    @property
    def functions(self):
        return self.__functions

    @functions.setter
    def functions(self, functions):
        self.__functions = functions
