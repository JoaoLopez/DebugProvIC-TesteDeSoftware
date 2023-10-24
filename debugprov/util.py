import ast, os

def get_AST(file_name):
    """This function receives the path of a Python file and returns the AST of its source code"""
    try:
        #Opening file
        file = open(file_name, "r")
        code = file.read()
        file.close()

    except:
        print("Error while trying to open file!")
        print("Check if the file exists!")
        return None

    else:
        try:
            #Generating AST from Python code
            return ast.parse(code)

        except:
            print("Error while trying to generate AST from the Python code!")
            print("Check if your Python script is correctly writen.")
            return None

def get_relative_path(script_folder, imported_script_name):
    def need_to_place_separator(letter, normalized_name):
        return (letter == "." and normalized_name[-1] != ".") or \
                (letter != "." and normalized_name[-1] == ".")
    def get_normalized_path(normalized_name):
        path = os.path.join(script_folder, normalized_name)
        return os.path.normpath(path)
        
    normalized_name = imported_script_name[0]
    for i in range(1, len(imported_script_name), 1):
        letter = imported_script_name[i]
        if need_to_place_separator(letter, normalized_name):
            normalized_name += os.sep
        normalized_name += letter
    
    normalized_path = get_normalized_path(normalized_name)
    if(os.path.isdir(normalized_path) and os.path.isfile(os.path.join(normalized_path, "__init__.py"))):
        return os.path.join(normalized_path, "__init__.py")
    elif(os.path.isfile(normalized_path + ".py")):
        return normalized_path + ".py"
