import sys
import os
import subprocess
from debugprov.update_json_2 import CriaJson
class NowInterface:

    def run_script(self):
        args = sys.argv
        print(args)
        Modulo = args.pop(0)
        os.environ['modulo']=Modulo
        CriaJson()
        #GravaModulo(args[0])
        print(os.getcwd())
        now_call = ['now','run']
        now_call.extend(args)
        proc = subprocess.Popen(now_call, cwd=os.getcwd(), env=os.environ, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = proc.communicate()
        print(stdout.decode('utf-8'))
