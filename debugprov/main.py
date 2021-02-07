from debugprov.console_interface import ConsoleInterface
from debugprov.now_interface import NowInterface
import traceback
from debugprov.json_manager import create_json
from debugprov.cls import limpa

def main():
      try:
            limpa()
            NowInterface().run_script()
            create_json()
            ConsoleInterface().run()
      except:
            traceback.print_exc()      

if __name__ == "__main__":
    main()
