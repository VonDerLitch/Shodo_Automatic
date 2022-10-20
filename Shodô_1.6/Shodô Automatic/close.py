from win import window
def startD():
    window['u'].update('Ocupado', button_color='red')
    window.refresh()

def closeD():
    window['u'].update('Disponível', button_color='green')
    window.refresh()