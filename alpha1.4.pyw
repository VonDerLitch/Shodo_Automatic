from PySimpleGUI import (Window, Button, Text, Image,
                         Column, VSeparator, Push, theme)
import subprocess
import time
import os




# layout
theme('Black')

layout_esquerda = [
    [Image(filename='log.png'),],
]

layout_direita = [
    [Text('Shodo Automatic')],
    [Button('Executar Shodo', size=20)], [Button('TUTORIAL:Como utilizar', size=20)], [Button('Sair', size=20)]
]

layout_u = [
    [Button('Disponível', size=20, button_color='green')]
]

layout_f = [
    [Button('Ocupado', size=20, button_color='red')]
]

layout = [
    [Column(layout_direita),  VSeparator(), Column(layout_esquerda), layout_u]
]

window = Window(
    'Shodo Automatic 1.2',
    layout=[[layout]],
    font=55,
    icon='icon.png'
)

# Funções
def startShodo():
    subprocess.call("TASKKILL /F /IM shodo.exe", shell=True)
    subprocess.call("TASKKILL /F /IM javaw.exe", shell=True)
    os.startfile("C:\Program Files (x86)\Shodo\shodo.exe")
    time.sleep(25)
    subprocess.call("TASKKILL /F /IM shodo.exe", shell=True)
    subprocess.call("TASKKILL /F /IM javaw.exe", shell=True)
def startD():
    window['Disponível'].update('Ocupado', button_color='red')

def closeD():
    window['Ocupado'].update('Disponível', button_color='green')

# evento de repetição
while True:
    event, values = window.read()
    if event == "Executar Shodo":
        startShodo()

    if event == "TUTORIAL:Como utilizar":
        os.startfile("www.google.com")


    if event == "Sair":
        exit()



