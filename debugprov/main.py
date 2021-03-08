import sys
from debugprov.console_interface import ConsoleInterface
from debugprov.now_interface import NowInterface
import traceback
from debugprov.autotest.json_manager import create_json
from debugprov.autotest.cls import limpa

def main():
      try:
            limpa()
            NowInterface().run_script()
            ConsoleInterface().run()
      except:
            traceback.print_exc()      

if __name__ == "__main__":
    main()
