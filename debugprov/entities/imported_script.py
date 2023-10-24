import ast

class ImportedScript():
    def __init__(self, name):
        self.__name = name
        self.__AST = None
        self.__functions = None

    ###DEBUG####
    def print(self, indent=0):
        print(indent * " " + "#####SCRIPT#####")
        print(indent * " " + "    Name:", self.__name)
        print(indent * " " + "    AST:", ast.dump(self.__AST))
        print(indent * " " + "    Functions:", self.__functions)
        
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
    def functions(self):
        return self.__functions

    @functions.setter
    def functions(self, functions):
        self.__functions = functions
