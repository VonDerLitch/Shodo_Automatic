"Bibliotecas"
import fileinput
import time
import subprocess
import os

"Executar o programa Shodo 1.1.3"
subprocess.call("TASKKILL /F /IM shodo.exe", shell=True)
subprocess.call("TASKKILL /F /IM javaw.exe", shell=True)
os.startfile("C:\Program Files (x86)\Shodo\shodo.exe")
time.sleep(25)
subprocess.call("TASKKILL /F /IM shodo.exe", shell=True)
subprocess.call("TASKKILL /F /IM javaw.exe", shell=True)

