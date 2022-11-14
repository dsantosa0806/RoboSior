import PySimpleGUI as sg
from PySimpleGUI import popup_animated


def alert(tipo, alerta):
    sg.popup(tipo, alerta,button_color='red', icon=r'images\robot.ico')


def loading():
    popup_animated(image_source=r'images\loader.gif')


def progress_bar(tipo):
    sg.theme('SystemDefaultForReal')
    layout = [[sg.Text(tipo)],
              [sg.ProgressBar(1000, orientation='h', size=(30, 20), key='progbar',)],
              [sg.Cancel()]
              ]

    window = sg.Window('Carregando...', layout)
    for i in range(1000):
        event, values = window.read(timeout=1)
        if event == 'Cancel' or event == sg.WIN_CLOSED:
            break
        window['progbar'].update_bar(i + 1)
    window.close()



