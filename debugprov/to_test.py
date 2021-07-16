def create_test(tree):
    #O nome do arquivo é test_{root.name}
    root = [x for x in tree if int(x.ev_id) == 1].pop()
    file_name = f'test_{root.name}'
    try:
        with open(file_name) as f:
            n = len(f.readlines())//3
    except:
        with open(file_name, 'w', encoding='utf8') as f:
            f.write(f"import unittest \n \n from {root.name[:-3]} import * \n \n class {root.name[:-3]}(unittest.TestCase):")
        n = 0
    new_tests = [nodo.nodo_to_test(n) for nodo in tree]
    
    print('NEW_TESTS')
    print(new_tests)
    with open(file_name, 'a', encoding='utf8') as f:
        for suit in new_tests:
            f.write(suit)
