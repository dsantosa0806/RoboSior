import PySimpleGUI as sg


def init_help_form():
    # Layout
    sg.SetOptions(background_color='#363636', text_element_background_color='#363636',
                  element_background_color='#363636', scrollbar_color=None, input_elements_background_color='#F7F3EC',
                  button_color=('black', '#4F4F4F'))

    # Colocar um Banner Explicativo
    layoutcampos = [


        [[sg.Col([[sg.Text('Algumas informações sobre a aplicação',
                           grab=True,font=('Segoe UI', 8))]], pad=(0, 0)),
          sg.Col([[sg.Text(sg.SYMBOL_CIRCLE, enable_events=False, key='-X-')]],  # '0'
                 element_justification='r', grab=True, pad=(0, 0), expand_x=True)],
         [sg.HorizontalSeparator()]],
        [sg.Image('images\Serget.png', size=(300, 300))],
        [sg.Button("Voltar", key="voltar")],
        [sg.Text('Desenvolvido por: Carlos Daniel da Silva Alves e Daniel Santos de Almeida.', key='mensagem',
                 size=(55, 0), font=('Segoe UI', 6,))],  # Mensagem

    ]

    return sg.Window('', finalize=True,
                     layout=layoutcampos,
                     no_titlebar=True,

                     )
