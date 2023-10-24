import os
from debugprov.entities.imported_script import ImportedScript
from debugprov.script_analysis.imported_scripts_finder import ImportedScriptsFinder
from debugprov.script_analysis.ast_searcher import ASTSearcher
from debugprov.util import get_AST

class MainScriptAnalyser():
    def __init__(self, mainScript):
        self.__mainScript = mainScript
        
    def analyse(self):
        #Analyzing MainScript
        s_AST, s_import_commands, s_functions, s_imported_scripts = self.__analyse_script(self.__mainScript)
        self.__mainScript.AST = s_AST
        self.__mainScript.import_commands = s_import_commands
        self.__mainScript.imported_scripts = s_imported_scripts
        self.__mainScript.functions = s_functions

        #Analyzing imported scripts
        for script in s_imported_scripts.values():
            script.AST, script.functions = self.__analyse_script(script, analyse_imports=False)
            
    def __analyse_script(self, script, analyse_imports=True):
        #Generating AST
        s_AST = get_AST(os.path.join(self.__mainScript.base_dir, script.name))
        if(s_AST is None):
            raise RuntimeError
        
        #Searching AST for import commands and functions defined
        if not analyse_imports:
            s_functions = ASTSearcher().search(s_AST, analyse_imports)
            return s_AST, s_functions
        else:
            s_import_commands, s_functions = ASTSearcher().search(s_AST, analyse_imports)
         
            #Getting all scripts imported by this script
            script_names = ImportedScriptsFinder(script.name, self.__mainScript.base_dir, s_import_commands).get_imported_scripts_names()
            s_imported_scripts = {}
            for name in script_names:
                s_imported_scripts[name] = ImportedScript(name)
            return s_AST, s_import_commands, s_functions, s_imported_scripts
        
