import shutil
import os
import sys
import json
import webbrowser
import re

def main_coverage():
    #module = sys.argv[0]
    print("É provável que alguns testes quebrem nesse processo")
    os.system(f"coverage run -m unittest test_{module_name()}")
    os.system(f"coverage html")
    os.system(f"coverage json")
    
    '''try:
        with open('coverage.json', 'r') as json_file:
            data = json.load(json_file)
    except:
        data = dict()
    data 
    '''
    #print("É necessário fechar o programa para pross")
    create_path()
    move_coverage_folder()
    metrify()
    
def move_coverage_folder():
    module_path = f"holdcoverages\\{module_name()[:-3]}\\"
    try:
        tam = len([x for x in os.listdir(module_path) if not os.path.isfile(f'{module_path}\\{x}')])
    except:
        tam = 0
    shutil.move("htmlcov\\", f"{module_path}{tam} htmlcov")
    shutil.move("coverage.json", f"{module_path}{tam} coverage.json")
    #os.popen(os.getcwd()+'\\htmlcov\\index.html')
    os.popen(f"{module_path}{tam} htmlcov\index.html")
    
def create_path():
    module_path = f"\\holdcoverages\\{module_name()[:-3]}\\"
    if os.path.exists(module_path):
        print(f"{module_path} existe!")
        return True
    if not os.path.exists("\\holdcoverages"):
        os.mkdir("\\holdcoverages")
    
    if not os.path.exists(module_path):
        os.mkdir(module_path)
    return False

def metrify():
    #Essa função metrifica 
    # a. quantos novos testes foram criados e 
    # b. como a cobertura foi expandida
    #Verificando número de testes novos criados:
    with open(f'test_{module_name()}') as e:
        count_test_by_exec = dict()
        count_test_by_exec[-1]=0
        for lin in e:
            if lin.startswith("    def "):
                count_test_by_exec[-1]+=1
                generation = int(lin.split("_")[-1][:-8])
                if generation not in count_test_by_exec:
                    count_test_by_exec[generation]=0
                count_test_by_exec[generation]+=1
    #print(count_test_by_exec)
    list_tot = list(count_test_by_exec.items())
    list_tot.sort()
    #print(list_tot)
    print(f"{list_tot[-1][1]} new tests were created. There are {list_tot[0][1]} tests altogether")
    #module_path = f"\\holdcoverages\\{module_name()[:-3]}\\"
    #Verifcando os jsons
    all_jsons = [x for x in os.listdir(f"holdcoverages\\{module_name()[:-3]}\\") if x.endswith(".json")]
    print(os.listdir(f"holdcoverages\\{module_name()[:-3]}\\"))
    all_jsons.sort(reverse=1, key = lambda n: int(n.split(" ")[0]))
    print("===")
    print(all_jsons)
    if len(all_jsons)>2:
        #new = get_coverage_index_at_json(all_jsons[0])
        #old = get_coverage_index_at_json(all_jsons[1])
        matrix(all_jsons)
    else:
        print("Primeiro teste, não há base anterior de comparação")
    
def matrix(df):
    new = get_coverage_index_at_json(df[0])
    old = get_coverage_index_at_json(df[1])
    print(f"O teste adquiriu {(new['percent_covered']/old['percent_covered'])*100}% a mais de cobertura")
    

        
def get_coverage_index_at_json(indice):
    with open(f"holdcoverages\\{module_name()[:-3]}\\{indice}") as json_file:
        dados = json.load(json_file)
    summary = dados.get('files').get(f"test_{module_name()}").get("summary")
    summary['missing lines'] = dados.get('files').get(f"test_{module_name()}").get("missing_lines")
    summary['excluded lines'] = dados.get('files').get(f"test_{module_name()}").get("excluded_lines")
    print(summary)
    return summary
    
def module_name():
    return sys.argv[0]
#    return 'eh_primo_b.py'
            
        
if __name__ == '__main__':
    sys.argv.pop(0)
    main_coverage()
    