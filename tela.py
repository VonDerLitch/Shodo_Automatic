from PySimpleGUI import (Window, Button, Text, Image,
                         Column, VSeparator, Push, theme)
import os
#layout
theme('Black')

layout_esquerda = [
    [Image(filename='log.png'),],
]

layout_direita = [
    [Text('Escolha o certificado')],
    [Button('RENATA ZANARDI', size=20 )],[Button('LARISSA ALMEIDA', size=20)],[Button('CLARISSEROZALES',size=20)]
]

layout = [
    [Column(layout_direita),VSeparator(),Column(layout_esquerda)]
]
window = Window(
    'Shodo Automatic 1.0',
    layout=[[layout]],
    font=55,
    icon='ICON.jpg',



)
#ler os eventos
while True:
    event, values = window.read()
    if event == "RENATA ZANARDI":
        path = "N:\Publico_AM\TI\Certificados"
        list = []
        for (root, dirs, file) in os.walk(path):
            for f in file:
                if 'RENATA ZANARDI.pfx' in f:
                    print(f)
    if event == "LARISSA ALMEIDA":
        path = "N:\Publico_AM\TI\Certificados"
        list = []
        for (root, dirs, file) in os.walk(path):
            for f in file:
                if 'LARISSA ALMEIDA-140518.pfx' in f:
                    print(f)
    if event == "CLARISSEROZALES":
        path = "N:\Publico_AM\TI\Certificados"
        list = []
        for (root, dirs, file) in os.walk(path):
            for f in file:
                if 'CLARISSEROZALES.pfx' in f:
                    print(f)
                    exit()
    else:
        exit()

window.close()