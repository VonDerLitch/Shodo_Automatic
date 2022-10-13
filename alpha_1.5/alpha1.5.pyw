from PySimpleGUI import (Window, Button, Text, Image,
                         Column, VSeparator, Push, theme)
import subprocess
import time
import os
import psutil

# layout
theme('Black')

layout_esquerda = [
    [Image(filename='logg.png')],
]

layout_direita = [
    [Text('Shodo Automatic ', text_color='OrangeRed', justification='center')],
    [Button('Executar Shodo', size=20)], [Button('TUTORIAL:Como utilizar', size=20)], [Button('Sair', size=20)]
]

layout_u = [
    [Button('Disponível', size=22, button_color='green', key='u')]
]

layout_f = [
    [Button('Ocupado', size=22, button_color='red', key='f')]
]

layout = [
    [Column(layout_direita),  VSeparator(), Column(layout_esquerda), layout_u]
]

window = Window(
    'Shodo Automatic 1.5',
    layout=[[layout]],
    font=55,
    icon=r'iconn.ico',
    size=(500,220),


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
    window['u'].update('Ocupado', button_color='red')

def closeD():
    window['u'].update('Disponível', button_color='green')

# evento de repetição
while True:
    event, values = window.read()
    if event == "Executar Shodo":
        startD()
        window.refresh()
        startShodo()
        closeD()
        window.refresh()




    if event == "TUTORIAL:Como utilizar":
        os.startfile("www.google.com")

    if event == "Sair":
        exit()

    if event == None:
        exit()