from debugprov.console_interface import ConsoleInterface
from debugprov.now_interface import NowInterface
import traceback

def main():
      try:
            print('ok')
            NowInterface().run_script()
            ConsoleInterface().run()
      except:
            traceback.print_exc()      

if __name__ == "__main__":
    main()
