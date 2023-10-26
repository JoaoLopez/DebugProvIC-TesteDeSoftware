class UnitTest():
    def __init__(self, func_tested:str, source_code:str):
        self.__func_tested = func_tested
        self.__source_code = source_code
    
    @property
    def func_tested(self):
        return self.__func_tested

    @property
    def source_code(self):
        return self.__source_code
