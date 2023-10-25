from debugprov.cli.console_interface import ConsoleInterface
from debugprov.cli.now_interface import NowInterface
from debugprov.cli.env import prepare_env
import traceback

def main():
      try:
            prepare_env()
            NowInterface().run_script()
            ConsoleInterface().run()
      except:
            traceback.print_exc()      

if __name__ == "__main__":
    main()
