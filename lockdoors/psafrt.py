import os
import sys
from lockdoors import main
from pathlib import Path
from datetime import datetime
from time import sleep
#VAR
yes = set(['yes', 'y', 'ye', 'Y'])
no = set(['no', 'n', 'nop', 'N'])
cwd = os.getcwd()
null = "" 
###Fonc
def psafrt():
    main.clscprilo()
    print("\033[91mHere is the list of the files :\033[90m")
    print("\033[92m")
    os.system("     find " + main.getinstalldir() + "/REPORT/TEMPLATES/ -type f")
    print("\033[90m")
    main.spc()
    main.oktocont()
    main.menu()