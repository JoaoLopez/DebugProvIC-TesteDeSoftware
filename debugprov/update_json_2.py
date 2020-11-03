import json
from datetime import datetime
from time import time
import os

def Cria_novo_item_no_body():
    item=os.environ.get("item")
    with open('MyJson.json', 'r', encoding='utf-8') as json_file:
        dicio=json.load(json_file)
        
        dicio['body'][item]={"parametros":{}, "saida":"saida", "resultadoValido":1}
    with open('MyJson.json', 'w', encoding='utf-8') as json_file:    
        json.dump(dicio, json_file, indent=4)


def Adiciona_parametro(chave, valor):
    item=os.environ.get("item")
    with open('MyJson.json', 'r', encoding='utf-8') as json_file:
        dicio=json.load(json_file)
        
        dicio['body'][item]['parametros'][chave]=valor
    with open('MyJson.json', 'w', encoding='utf-8') as json_file:    
        json.dump(dicio, json_file, indent=4)

def Adiciona_saida(valor):
    item=os.environ.get("item")
    with open('MyJson.json', 'r', encoding='utf-8') as json_file:
        dicio=json.load(json_file)
        
        dicio['body'][item]['saida']=valor
    with open('MyJson.json', 'w', encoding='utf-8') as json_file:    
        json.dump(dicio, json_file, indent=4)
    
def adiciona_validor_do_resultado(booleano):
    item=os.environ.get("item")
    with open('MyJson.json', 'r', encoding='utf-8') as json_file:
        dicio=json.load(json_file)
        dicio['body'][item]['resultadoValido']=booleano
    with open('MyJson.json', 'w', encoding='utf-8') as json_file:    
        json.dump(dicio, json_file, indent=4)

def AdicionaNo(Nodo):
    with open('MyJson.json', 'r', encoding='utf-8') as json_file:
        dicio=json.load(json_file)
        
        dicio['body'][item]['parametros'][chave]=valor
    with open('MyJson.json', 'w', encoding='utf-8') as json_file:    
        json.dump(dicio, json_file, indent=4)


def CriaJson(modulo):
    dicio={
            "header": {
            "caminho":os.getcwd(),
            "modulo": modulo
        },
        "body": 
            {
		
            }
        }
    print(os.getcwd())
    with open(f'abcd.json', 'w', encoding='utf-8') as json_file:    
        json.dump(dicio, json_file, indent=4)
    print('json criado')

if __name__ == "__main__":
    CriaJson()        
    os.environ['item']=("MMC")
    Cria_novo_item_no_body()
    Adiciona_parametro("x", 12)
    Adiciona_parametro("y", 8)
    Adiciona_saida(24)
    adiciona_validor_do_resultado(1)

    os.environ['item']=("MMC2")
    Cria_novo_item_no_body()
    Adiciona_parametro("x", 12)
    Adiciona_parametro("y", 8)
    Adiciona_saida(25)
    adiciona_validor_do_resultado(0)
