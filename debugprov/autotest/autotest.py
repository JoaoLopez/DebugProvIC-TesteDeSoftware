import re
import sys
from ast import literal_eval
import json
from pprint import pprint

from debugprov.json_manager import set_dictionary

class Binder:
    def __init__(self):
        self.base = sys.argv[0].replace(" ", "_")
        #print(f"::::: base {base}")
        self.modulo  = self.base[:-3]
        self.my_json = self.modulo+".json"
        self.test = f"test_{self.base}"
        try:
            with open(self.test, 'r', encoding='utf-8') as e:
                self.content = e.readlines()
                self.arquivo_de_teste = []
        except:
            self.content = [""]
            self.arquivo_de_teste = self.header()
            
        
    def execution_number(self):
        try:
            self.ciclo = 1
            with open(self.test, encoding='utf-8') as e:
                for lin in e:
                    pass
            lin = lin[::-1]
            if re.match(r"[0-9]*#", lin):
                indice, _ = split("#", 1)
                indice = int(indice)
                self.ciclo = indice+1
        except:
            indice = 0
            self.ciclo = 0
        self.test_py_exists = bool(self.ciclo)

    
    #funções do núcleo
    def header(self):
        arquivo_de_teste = []
        arquivo_de_teste.append("import unittest")
        arquivo_de_teste.append(f"from {self.modulo} import *")
        arquivo_de_teste.append("\n\n")
        arquivo_de_teste.append(f"class Test_{self.modulo.title()}(unittest.TestCase):")
        arquivo_de_teste.append(f"\n")
        return arquivo_de_teste

    def gera_teste_a_partir_do_nodo(self, entrada):
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
        nome_do_teste = f"{tabs(1)}def test_node_{entrada['ev_id']}_{len(self.content)}(self):"    
        my_list.append(nome_do_teste)
        #print(entrada['name'])
        novo_nome = str(entrada['name'])
        #Iterando sobre os parametros
        for ch, item in enumerate(entrada['params']):
            for key, value in item.items(): pass
            #print(key, value)
            ch=f"var_{ch}"
            try:
                my_list.append(f"{tabs(2)}{ch} = {leval(value)}")
            except:
                return []
            novo_nome = novo_nome.replace(key, ch, 1)
        try:
            my_list.append(f"{tabs(2)}self.assertEqual({novo_nome}, {leval(entrada['retrn'])})")
        except:
            return []
        my_list.append("\n")
        my_list = modificacoes_do_usuário(my_list)
        self.arquivo_de_teste+=my_list

    def persiste_lista_em_arquivo_py(self):
        code = "".join(self.content)
        code+= "\n".join(self.arquivo_de_teste)
        with open(self.test, 'w', encoding='utf-8') as s:
            s.write(code)
        return None
        
    #funções para a geração sem json
    def header_manager2(self):
        modulo = self.modulo
        indice = execution_number(arquivo_de_teste)
        if not indice:
            arquivo_de_teste = header(modulo)
            persiste_lista_em_arquivo_py(arquivo_de_teste, modulo, 'w')
    
    def header_manager(self):
        arquivo_de_teste = header(self.modulo)
        persiste_lista_em_arquivo_py(arquivo_de_teste, self.modulo, 'w')

    def node_manager(self, nodo):
        if nodo.has_childrens():
            nodo = set_dictionary(nodo)
            arquivo_de_teste = self.gera_teste_a_partir_do_nodo(nodo)
        #persiste_lista_em_arquivo_py(arquivo_de_teste, modulo, 'a')
    
    def end(self):
        self.persiste_lista_em_arquivo_py()
        

'''def adiciona_numero_ao_fim_do_arquivo():
    ''
    O número serve para podermos saber qual o ciclo
    atual e impedir que nós sejam sobreescritos depois
    de novas execuções.
    
    persiste_lista_em_arquivo_py()'''
    
    

#funções auxiliares
def tabs(n): return " "*4*n

def leval(expr):
    expr = literal_eval(expr)
    if isinstance(expr, str): expr=f"'{expr}'"
    return expr
'''
def corrige_o_modulo(file):
    if file.endswith(".py"): file = file[:-3]
    if not file.endswith(".json"): file+=".json"
    file = file.replace(" ", "_")
    return file

def nomes_dos_arquivos(base):
    base    = sys.argv[0].replace(" ", "_")
    #print(f"::::: base {base}")
    modulo  = base[:-3]
    my_json = modulo+".json"
    test = f"test_{base}"
    return {'py':base, 'modulo':modulo, 'json':my_json, 'test':test}

#Programa a ser executado se existe json    
def leitor_json(file):
    #if not file.endswith('.json'): file+=".json"
    aux = nomes_dos_arquivos()
    modulo = aux.get('modulo')
    
    arquivo_de_teste = []
    arquivo_de_teste+=header(modulo)
    try:
        with open(aux.get('json'), 'r') as json_file:
            dados = json.load(json_file)
    except:
        print("o arquivo é", aux.get('json'))
        print("O arquivo não existe")
        return []
    
    #print(dados)
    #del dados['1']
    for v in dados.values():
        arquivo_de_teste+=gera_teste_a_partir_do_nodo(v)
    for lin in arquivo_de_teste:
        print(lin)
    persiste_lista_em_arquivo_py(arquivo_de_teste, modulo, 'm')
    
'''
#Condicionais a serem implementadas
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

def quer_os_tests(file):
    opcoes = ["[{}] - Não quero gerar testes",
              "[{}] - Quero gerar todos os testes e sem personalizações",
              "[{}] - Quero poder escolher que testes criar e editar seus respectivos nomes"]
    for key, value in enumerate(opcoes):
        print(value.format(key))
    resposta = int(input("O que deseja?"))
    return resposta
    

if __name__ == "__main__":
    #doctest.testmod()
    j = 'soma'
    if len(sys.argv)>1: j=(sys.argv[1])
    #l=leitor_json(j)
    
