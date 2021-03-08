import sys
from debugprov.autotest.cls import limpa
from debugprov.console_interface import ConsoleInterface
from debugprov.now_interface import NowInterface
import traceback
from debugprov.autotest.json_manager import create_json


def main():
      try:
            limpa()
            NowInterface().run_script()
            ConsoleInterface().run()
      except:
            traceback.print_exc()      


if __name__ == "__main__":
    print("sucesso")
    main()
