from debugprov.cli.console_interface import ConsoleInterface
from debugprov.cli.now_interface import NowInterface
import traceback

def main():
      try:
            NowInterface().run_script()
            ConsoleInterface().run()
      except:
            traceback.print_exc()      

if __name__ == "__main__":
    main()
