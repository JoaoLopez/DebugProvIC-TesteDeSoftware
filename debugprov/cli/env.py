import os
import shutil

def remove_gvs_and_pdfs_files():
    k=0
    for file in os.listdir():
        if "gv" in file.split("."):
            os.remove(file)
            k+=1
    print(f"Foram excluídos {k} arquivos")   

def remove_noworkflow_folder():
    if os.path.exists('.noworkflow'):
        shutil.rmtree('.noworkflow')
        print(".noworkflow foi removido")
    else:
        print(".noworkflow não estava presente")

def prepare_env():
    remove_noworkflow_folder()
    remove_gvs_and_pdfs_files()

