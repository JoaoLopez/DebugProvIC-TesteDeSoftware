from debugprov import update_json
class Parameter:

    def __init__(self, name, value):
        update_json.AdicionaParam(str((name, value)))
        self.name = name
        self.value = value