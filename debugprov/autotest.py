import sys
from ast import literal_eval
import json
from pprint import pprint


def tabs(n): return " "*4*n

def leval(expr):
    try:
        expr = literal_eval(expr)
        if isinstance(expr, str): expr=f"'{expr}'"
    except:
        pass
    return expr

def gera_teste_a_partir_do_nodo(entrada):
    '''
    Este é o núcleo do programa, ele recebe um dicionário
    contendo o Nodo a ser tratado.
    :params: entrada recebe o nodo em formato de dicionário
    :params type dict
    :return list de strings pronta para ser impressa.
    '''
    if not entrada['validity']:
        return []
    my_list = []
    #Criando o nome do teste
    nome_do_teste = f"{tabs(1)}def test_node_{entrada['ev_id']}(self):"    
    my_list.append(nome_do_teste)
    #print(entrada['name'])
    novo_nome = str(entrada['name'])
    #Iterando sobre os parametros
    for ch, item in enumerate(entrada['params']):
        for key, value in item.items(): pass
        #print(key, value)
        ch=f"var_{ch}"
        my_list.append(f"{tabs(2)}{ch} = {leval(value)}")
        novo_nome = novo_nome.replace(key, ch, 1)
    my_list.append(f"{tabs(2)}self.assertEqual({novo_nome}, {leval(entrada['retrn'])})")
    my_list.append("\n")
    my_list = modificacoes_do_usuário(my_list)
    return my_list

def modificacoes_do_usuário(my_list):
    '''
    Se no ele vai perguntar ao usuário se deseja salvar aquele
    caso de teste e se deseja renomea-lo.
    : params lista criada por gera_teste_a_partir_do_nodo
    : params b: Se deseja modificar algo
    
    '''
    if "m" in sys.argv:
        pprint(my_list)
        quer = input("Digite algo caso NÃO queira gerar um caso de teste nesse cenário")
        if quer: return []
        nome_do_teste = input("Renomeie o caso de teste se assim quiser")
        if nome_do_teste: my_list[0]= f"{tabs(1)}def test_{nome_do_teste.replace(' ', '_')}():"    
    return my_list

def corrige_o_modulo(file):
    if file.endswith(".py"): file = file[:-3]
    if not file.endswith(".json"): file+=".json"
    file = file.replace(" ", "_")
    return file
def leitor_json(file):
    #if not file.endswith('.json'): file+=".json"
    file = corrige_o_modulo(file)
    modulo = file[:-5]
    arquivo_de_teste = []
    arquivo_de_teste.append("import unittest")
    arquivo_de_teste.append(f"from {modulo} import *")
    arquivo_de_teste.append("\n\n")
    arquivo_de_teste.append(f"class Test_{modulo.title()}(unittest.TestCase):")
    try:
        with open(file, 'r') as json_file:
            dados = json.load(json_file)
    except:
        print("o arquivo é", file)
        print("O arquivo não existe")
        return []
    
    #print(dados)
    del dados['1']
    for v in dados.values():
        arquivo_de_teste+=gera_teste_a_partir_do_nodo(v)
    for lin in arquivo_de_teste:
        print(lin)
    persiste_lista_em_arquivo_py(arquivo_de_teste, modulo)
    
def persiste_lista_em_arquivo_py(lista, file):
    new_file = f"test_{file}.py"
    code = "\n".join(lista)
    with open(new_file, 'w', encoding='utf-8') as s:
        s.write(code)
    return None

if __name__ == "__main__":
    #doctest.testmod()
    j = 'soma'
    if len(sys.argv)>1: j=(sys.argv[1])
    l=leitor_json(j)
    
