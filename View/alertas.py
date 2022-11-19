import PySimpleGUI as sg


def alert(tipo, alerta):
    sg.popup(tipo, alerta,button_color=('yellow', '#4F4F4F'), icon=r'images\robot.ico',no_titlebar=True)


def init_janela_alerta():

    # Layout
    sg.SetOptions(background_color='#363636', text_element_background_color='#363636',
                  element_background_color='#363636', scrollbar_color=None, input_elements_background_color='#F7F3EC',
                  button_color=('black', '#4F4F4F'))

    # sg.theme('SystemDefaultForReal')
    layoutcampos = [


        [[sg.Col([[sg.Text('Estamos preparando tudo ! por favor aguarde...',
                           grab=True,font=('Segoe UI', 8))]], pad=(0, 0)),
          sg.Col([[sg.Text(sg.SYMBOL_X, enable_events=True, key='-X-')]],  # '❎'
                 element_justification='r', grab=True, pad=(0, 0), expand_x=True)],
         [sg.HorizontalSeparator()]],
        [sg.Text('auto', key='mensagem', size=(50, 0), font=('Segoe UI', 8))],  # Usuario

    ]

    return sg.Window('', finalize=True,
                     layout=layoutcampos,
                     no_titlebar=True,
                     auto_close=(True,4))


def init_janela_apresentacao():
    # Layout
    sg.SetOptions(background_color='#363636', text_element_background_color='#363636',
                  element_background_color='#363636', scrollbar_color=None, input_elements_background_color='#F7F3EC',
                  button_color=('black', '#4F4F4F'))

    # sg.theme('SystemDefaultForReal')
    layoutcampos = [


        [[sg.Col([[sg.Text('Iniciando a aplicação ! por favor aguarde...',
                           grab=True,font=('Segoe UI', 8))]], pad=(0, 0)),
          sg.Col([[sg.Text(sg.SYMBOL_CIRCLE, enable_events=True, key='-X-')]],  # '❎'
                 element_justification='r', grab=True, pad=(0, 0), expand_x=True)],
         [sg.HorizontalSeparator()]],
        [sg.Image('images\Serget.png', size=(300, 300))],
        [sg.Text('Desenvolvido por: Carlos Daniel da Silva Alves e Daniel Santos de Almeida.', key='mensagem',
                 size=(55, 0), font=('Segoe UI', 6,))],  # Mensagem

    ]

    return sg.Window('', finalize=True,
                     layout=layoutcampos,
                     no_titlebar=True,
                     auto_close=(True, 5))


