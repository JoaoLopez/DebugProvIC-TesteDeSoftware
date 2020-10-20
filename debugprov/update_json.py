#import math
import json
from datetime import datetime
from time import time
import os
#from constant import *

def GravaModulo(modulo):
    print(f'{os.getcwd()} but in modulo')
    dicio={'modulo':modulo,
           'funcao':str(),
           'param' :[],
           'resultado_obtido':'',
           'resulado_esperado':''
           }
    
    with open('C:\\Users\\lucas\\Desktop\\temp.json', 'w', encoding='utf-8') as json_file:
        json.dump(dicio, json_file, indent=4)
    with open('C:\\Users\\lucas\\Desktop\\temp.xml', 'w', encoding='utf-8') as xisml:
        xisml.write(f'<xml>\n<modulo>{modulo}</modulo>')
    print("gravado")
    

def AdicionaChave(chave, valor):
    with open('temp.json', 'r', encoding='utf-8') as json_file:
        dicio=json.load(json_file)
        dicio[chave]=valor
    with open('temp.json', 'w', encoding='utf-8') as json_file:    
        json.dump(dicio, json_file, indent=4)
    with open('temp.xml', 'a', encoding='utf-8') as xisml:
        xisml.write(f'<{chave}>{valor}</{chave}>\n')
        if chave=='resultado_esperado':
            fim="ABxmlC".replace("A", chr(60)).replace("B", chr(47)).replace("C",chr(62))
            xisml.write(fim)
            xisml.write('\n')
            chave=False
    if not(chave):
        operaçõesFinais()
        chave=True
            
def AdicionaFuncao(funcao):
    AdicionaChave('funcao', funcao.__name__)

def AdicionaParam(param):
    if not(isinstance(param, list)):
        param=[param]
    AdicionaChave("param", param)

def AdicionaResultadoObtido(resultado):
    AdicionaChave('resultado_obtido', resultado)

def AdicionaResultadoEsperado(resultado):
    AdicionaChave('resultado_esperado', resultado)

def operaçõesFinais():  
    #Se o arquivo está completo 
    #Renomeia os arquivos com o nome do modulo testado + data e hora de criação
    with open('temp.json', 'r', encoding='utf-8') as json_file:
        dicio=json.load(json_file)
        nome=f"{dicio['modulo']} - {str(datetime.now())}"
        nome=nome.replace(":", "-")
        with open(f'{nome}.json', 'w', encoding='utf-8') as newJson:
            json.dump(dicio, newJson, indent=4)
    
    with open('temp.xml', 'r', encoding='utf-8') as entrada:
        with open(f'{nome}.xml', 'w', encoding='utf-8') as saida:
            for linha in entrada:
                print(linha)
                saida.write(linha)
    

'''if __name__=='__main__':
    GravaModulo(math)
    AdicionaFuncao(math.gcd)
    AdicionaParam([12, 8])
    AdicionaResultadoObtido(math.gcd(12, 8))
    AdicionaResultadoEsperado(4)
'''