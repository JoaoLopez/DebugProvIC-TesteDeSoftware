import sys
import os
import subprocess
from debugprov.update_json_2 import CriaJson
from debugprov.cls import limpa
class NowInterface:

    def run_script(self):
        args = sys.argv
        print(args)
        args.pop(0)
        os.environ['modulo']=args[0]
        CriaJson(args[0])
        #limpa()
        #GravaModulo(args[0])
        print(os.getcwd())
        now_call = ['now','run']
        now_call.extend(args)
        proc = subprocess.Popen(now_call, cwd=os.getcwd(), env=os.environ, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = proc.communicate()
        print(f"===stdout = {stdout} e {stderr} = stederr==")
        print(stdout.decode('utf-8'))
