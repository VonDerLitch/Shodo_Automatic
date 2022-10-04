"Bibliotecas"
import fileinput
import sys
import time
import subprocess
import os
from tkinter import *
"Janela para esconder o terminal"
'win64'
sys.platform
"Executar o programa Shodo 1.1.2"
os.startfile("C:\Program Files (x86)\Shodo\shodo.exe")
time.sleep(60)
subprocess.call("TASKKILL /F /IM shodo.exe", shell=True)
subprocess.call("TASKKILL /F /IM javaw.exe", shell=True)
