#!/usr/bin/python
import os
import sys
import shutil
import datetime
def printf(string):
    if not(sys.argv[1]):
        print(string)
# Get directory name

def limpa(path=os.getcwd()):
    if len(sys.argv)==1:
        sys.argv.append(False)
    print("arg=", sys.argv[1], type(sys.argv[1]))
    mydir= path+'.noworkflow'
    hoje = str(datetime.date.today())
    ## Try to remove tree; if failed show an error using try...except on screen
    '''try:
        #shutil.rmtree(mydir)
        print("Pasta .noworkflow apagada")
    except OSError as e:
        print ("Error: %s - %s." % (e.filename, e.strerror))'''
    try:
        ehGv=lambda nome:nome[:4].isdigit()
        gvs=list(filter(ehGv, os.listdir()))
        adress=lambda n: path+'\\'+n
        for item in gvs:
            try:
                dia=os.path.getmtime(item)
                dia=datetime.datetime.fromtimestamp(dia).strftime('%Y-%m-%d')
                os.makedirs(f'{path}\\logs\\{dia}')
            except:
                pass
            novo=f'logs\\{dia}\\{item}'
            shutil.move(adress(item), adress(novo))
            printf(f'Transferido: {item}')
    except:
        printf("fail trivial")
    try:
        if '.noworkflow' in os.listdir():
            ehGv=lambda nome:nome[:4]=='exec'
            gvs=list(filter(ehGv, os.listdir()))
            ag=datetime.datetime.now()
            ag=ag.strftime('%Y-%m-%d(%H;%M)')
            os.makedirs(f'{path}\\logs\\oldflows\\{ag}')
            novo=f'{path}\\logs\\oldflows\\{ag}\\'
            shutil.move(adress('.noworkflow'), adress(novo))
            for item in gvs:
                novo2=f'{path}\\{novo}\\{{item}}'
                shutil.move(adress(item), adress(novo))
            printf("Cópia feita")
        else:
            printf("A pasta não existe")
    except:
        printf('fail .noworkflow')
        
if __name__=='__main__':
    limpa()