import sys
import os
import subprocess

from debugprov.clean import clean
class NowInterface:

    def run_script(self):
        args = sys.argv
        args.pop(0)
        clean()
        now_call = ['now','run']
        now_call.extend(args)
        proc = subprocess.Popen(now_call, cwd=os.getcwd(), env=os.environ, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = proc.communicate()
        print(stdout.decode('utf-8'))
