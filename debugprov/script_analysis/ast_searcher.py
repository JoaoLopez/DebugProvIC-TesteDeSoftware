import ast
class ASTSearcher(ast.NodeVisitor):
    def search(self, AST, analyse_imports):
        self.__import_commands = []
        self.__functions = {}
        self.__analyse_imports = analyse_imports
        self.visit(AST)

        if analyse_imports:
            return self.__import_commands, self.__functions
        else:
            return self.__functions

    def visit_Import(self, node):
        #Adding new import command to self.__import_commands
        if self.__analyse_imports and node not in self.__import_commands:
            self.__import_commands.append(node)
        self.generic_visit(node)

    def visit_ImportFrom(self, node):
        #Adding new "from ... import ..." command to self.__import_commands
        if self.__analyse_imports and node not in self.__import_commands:
            self.__import_commands.append(node)
        self.generic_visit(node)

    def visit_ClassDef(self, node):
        """This function avoids that child nodes of a ClassDef node
        (ex.: class methods) be visited during search"""

    def visit_FunctionDef(self, node):
        #Adding only ast.FunctionDef instances that are defined on the global scope
        #Ignoring inner function definitions once it is not trivial to test them!
        self.__functions[node.name] = node
