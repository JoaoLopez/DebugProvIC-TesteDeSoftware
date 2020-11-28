import os
import datetime
import shutil

def move(arvorefinal):
    resumo=input()
    pasta='.\\logs'
    if not os.path.isdir('logs'):
        os.makedirs(pasta)
    pasta+='\\{os.environ.get("modulo")}'
    if not os.path.isdir(f'logs\\{os.environ.get("modulo")}'):
        os.makedirs(pasta)
        with open(f'{pasta}/readme.txt', 'w', encoding='utf-8') as _: pass
    agora = str(datetime.datetime.now())[2:18].replace(':', '_')
    pastah=pasta+hoje
    os.makedirs(pastah)
    mydir= '.noworkflow'
    ehGv=lambda nome:nome[:4].isdigit()
    gvs=list(filter(ehGv, os.listdir()))
    adress=lambda n: os.getcwd()+'\\'+n
    try:
        for item in gvs:
            '''try:
                #dia=os.path.getmtime(item)
                #dia=datetime.datetime.fromtimestamp(dia).strftime('%Y-%m-%d')
                os.makedirs(f'.\\logs\\{dia}')
            except:
                pass
            '''
            novo=f'logs\\{dia}\\{item}'
            shutil.move(adress(item), adress(pastah))
            printf(f'Transferido: {item}')
    except:
        pass
    
    if '.noworkflow' in os.listdir():
        #ehExec=lambda nome: nome[:4]=='exec'
        #gvs=list(filter(ehExec, os.listdir()))
        #ag=datetime.datetime.now()
        #ag=ag.strftime('%Y-%m-%d(%H;%M)')
        #os.makedirs(f'.\\logs\\oldflows\\{ag}')
        #novo=f'.\\logs\\oldflows\\{ag}\\'
        shutil.move(adress('.noworkflow'), adress(pastah))
        #for item in gvs:
        #    novo2=f'{novo}\\{{item}}'
        #    shutil.move(adress(item), adress(novo))
        printf("Cópia feita")
    else:
        printf("A pasta não existe")
    
    
    json=f'{os.environ.get("modulo")}.json'
    if arvorefinal.endswith('r'):
        json=arvorefinal+'.json'
    shutil.move(adress(f'{arvorefinal}.gz.pdf'))
    shutil.move(adress(json))
    if resumo:
        with open(f'{pasta}\readme.txt', 'a', encoding='utf-8') as saida:
            saida.write(agora)
            saida.write('\n')
            saida.write(resumo)
            print("Resumo atualizado")
        
    #except:
    #    printf('fail .noworkflow')
    
    
