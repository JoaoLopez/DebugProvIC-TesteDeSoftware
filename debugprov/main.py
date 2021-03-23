import sys
from debugprov.console_interface import ConsoleInterface
from debugprov.now_interface import NowInterface
import traceback
from debugprov.json_manager import create_json
from debugprov.cls import limpa
from debugprov.my_coverage import main_coverage
def main():
      try:
            limpa()
            NowInterface().run_script()
            ConsoleInterface().run()
            main_coverage()
      except:
            traceback.print_exc()      

if __name__ == "__main__":
    main()
