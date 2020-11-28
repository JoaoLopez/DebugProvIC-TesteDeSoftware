from debugprov.console_interface import ConsoleInterface
from debugprov.now_interface import NowInterface
import traceback
import os
from debugprov.moving import MyMove

def main():
    try:
        print('ok2')

        NowInterface().run_script()
        ConsoleInterface().run()
    except:
        traceback.print_exc()      
        #cls.limpa(os.getcwd())

        
      

if __name__ == "__main__":
    main()
       
    MyMove()
    #except:
    #    print("Move didn't work")
    #cls.limpa(os.getcwd())