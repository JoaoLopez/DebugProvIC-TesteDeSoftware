import ast, os
from debugprov.util import get_relative_path

class ImportedScriptsFinder():
    def __init__(self, s_name, base_dir, import_commands):
        self.__script_name = s_name
        self.__import_commands = import_commands
        self.__base_dir = base_dir
    
    #This method returns all the imported scripts and modules defined by the user
    def get_imported_scripts_names(self):
        s_names = self.__get_explicitly_imported_scripts()
        s_names += self.__get_implicitly_imported_scripts(s_names)
        return list(dict.fromkeys(s_names)) #Removing duplicated scripts

    #This method takes all import commands and returns the paths to all the modules/scripts imported
    def __get_explicitly_imported_scripts(self):
        s_names = self.__get_scripts_names()
        return self.__get_scripts_paths(s_names)

    def __get_scripts_names(self):
        s_names = []
        for command in self.__import_commands:
            if(isinstance(command, ast.Import)):
                for alias in command.names:
                    s_names.append(alias.name)
            elif(isinstance(command, ast.ImportFrom)):
                name = command.level * "."
                if command.module:
                    name += command.module
                s_names.append(name)
        return s_names

    def __get_scripts_paths(self, s_names):
        s_paths = []
        for name in s_names:
            path = get_relative_path(os.path.dirname(self.__script_name), name)
            if path:
                s_paths.append(path)
        return s_paths

    #This method returns all "__init__.py" scripts implicitly imported when another python script is imported
    def __get_implicitly_imported_scripts(self, explicitly_scripts):
        def module_imported(name):
            return name.rfind(os.sep) != -1

        def get_initial_path(name):
            return name[0:name.rfind(os.sep) + 1] + "__init__.py"
        
        def update_path(path):
            path = path.split(os.sep)
            path.pop(-2)
            return os.sep.join(path)

        implicitly_scripts = []
        for name in explicitly_scripts:
            if(module_imported(name)):
                implicitly_path = get_initial_path(name)
                while(implicitly_path != "__init__.py"):
                    if os.path.exists(os.path.join(self.__base_dir, implicitly_path)):
                        implicitly_scripts.append(implicitly_path)
                    implicitly_path = update_path(implicitly_path)
        return implicitly_scripts
