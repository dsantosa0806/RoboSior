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


def init_janela_alerta():

    # Layout
    sg.SetOptions(background_color='#363636', text_element_background_color='#363636',
                 element_background_color='#363636', scrollbar_color=None, input_elements_background_color='#F7F3EC',
                 button_color=('white', '#4F4F4F'))

    # sg.theme('SystemDefaultForReal')
    layoutcampos = [


        [[sg.Col([[sg.Text('Estamos preparando tudo ! por favor aguarde...', grab=True,font=('Segoe UI', 8))]], pad=(0, 0)),
          sg.Col([[sg.Text(sg.SYMBOL_X, enable_events=True, key='-X-')]],  # '❎'
                 element_justification='r', grab=True, pad=(0, 0), expand_x=True)],
         [sg.HorizontalSeparator()]],
        [sg.Text('auto', key='mensagem', size=(50, 0), font=('Segoe UI', 8))],  # Usuario

    ]

    return sg.Window('', finalize=True,
                     layout=layoutcampos,
                     no_titlebar=True)

