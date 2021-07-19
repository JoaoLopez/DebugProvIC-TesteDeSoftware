import os
import shutil

def remove_gvs_and_pdfs():
    k=0
    for file in os.listdir():
        if "gv" in file.split("."):
            print(file) #os.remove(file)
            k+=1
    print(f"Foram excluídos {k} arquivos")   

def remove_noworkflow():
    if os.path.exists('.noworkflow'):
        shutil.rmtree('.noworkflow')
        print(".noworkflow foi removido")
    else:
        print(".noworkflow não estava presente")
def clean():
    remove_noworkflow()
    remove_gvs_and_pdfs()

