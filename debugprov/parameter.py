from debugprov import update_json_2
class Parameter:

    def __init__(self, name, value):
        #update_json.AdicionaParam(str((name, value)))
        print(name, value, 'Um oferecimento, PARAM')
        self.name = name
        self.value = value
    
    def __repr__(self):
        return f'{self.name}|{self.value}'
        
    def __str__(self):
        return self.__repr__()