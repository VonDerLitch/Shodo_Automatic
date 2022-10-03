import fileinput
import sys
import time
import subprocess
sys.platform
'win64'
"Executar o programa Shodo 1.1.2"
import os
os.startfile("C:\Program Files (x86)\Shodo\shodo.exe")
time.sleep(30)
subprocess.call("TASKKILL /F /IM shodo.exe", shell=True)
subprocess.call("TASKKILL /F /IM javaw.exe", shell=True)