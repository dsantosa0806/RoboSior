import PySimpleGUI as sg


def init_janela_form():
    # Layout
    # sg.theme('SystemDefaultForReal')
    sg.SetOptions(background_color='#363636', text_element_background_color='#363636',
                  element_background_color='#363636', scrollbar_color=None, input_elements_background_color='#F7F3EC',
                  button_color=('white', '#4F4F4F'))
    menu = [[sg.Menu(
        [
         ['Inicio',['Sair']],
         ['Tabela', ['Dados']],
         ['Ajuda',['Requisitos']],
        ]
        )]
    ]

    layoutcampos = [

        [sg.Text('Quais Documentos deseja baixar ? *',font=('Segoe UI',12))],
        [sg.Checkbox('Auto de Infração', key='Auto de Infração', font=('Segoe UI', 10))],
        [sg.Checkbox('Relatório Financeiro', key='Relatório Financeiro', font=('Segoe UI', 10))],
        [sg.Checkbox('Relatório Resumido', key='Relatório Resumido', font=('Segoe UI',10))],
        [sg.Checkbox('Notificação de autuação', key='Notificação de autuação',font=('Segoe UI',10))],
        [sg.Checkbox('Notificação de Penalidade', key='Notificação de Penalidade',font=('Segoe UI',10))],
        [sg.Text('______________________________')],
        [sg.Text('Deseja criar pastas ? *', font=('Segoe UI', 12))],
        [sg.Radio('Sim', "RADIO1", key='PastasSim', font=('Segoe UI', 10)),
         sg.Radio('Não', "RADIO1", key='PastasNão', font=('Segoe UI', 10))],
        [sg.Text('______________________________')],
        [sg.Text('Insira os números dos autos abaixo *',font=('Segoe UI',12),tooltip='Limite de 10 autos por vez.')],
        [sg.Multiline(size=(30, 10),key='auto', font=('Segoe UI',10),
                      tooltip='Antes de alimentar os campos, verifique o tamanho do Nº do Auto.')],
        [sg.Button('Limpar', font=('Segoe UI', 10))],
        [sg.Text('______________________________')],
        [sg.Output(size=(50, 10),font=('Segoe UI',10),key='Output',)],
        [sg.Button('Iniciar',button_color='green',font=('Segoe UI',10)),sg.Button('Resetar',font=('Segoe UI',10))
         ]
    ]
# ,
    #          sg.Button('Sair',font=('Segoe UI',10))
    # Janela
    return sg.Window('Baixar Documentos',
                       enable_close_attempted_event=True,
                       finalize=True,
                       icon=r'images\robot.ico').layout(menu + layoutcampos)

