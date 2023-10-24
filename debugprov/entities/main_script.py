import ast

class MainScript():
    def __init__(self, base_dir, main_script_name):
        self.__base_dir = base_dir
        self.__name = main_script_name
        self.__AST = None
        self.__import_commands = None
        self.__imported_scripts = None
        self.__functions = None

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
