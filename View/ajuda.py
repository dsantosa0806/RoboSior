import os
import PySimpleGUI as sg


def init_help_form():
    # Layout
    sg.SetOptions(background_color='#363636', text_element_background_color='#363636',
                  element_background_color='#363636', scrollbar_color=None, input_elements_background_color='#F7F3EC',
                  button_color=('black', '#4F4F4F'))

    # Colocar um Banner Explicativo
    layout1 = [
        [sg.Text('REQUISITOS\n'
                 '\n'
                 'Para o correto funcionamento da aplicação, o navegador Google Chromme deve estar instalado no computador.\n'
                 
                 'Acesse: https://www.google.com/intl/pt-BR/chrome/ \n'
                 '\n'
                 'Para o correto funcionamento da aplicação, deve-se verificar se o Chromme está atualizado com a versão mais recente \n'
                 
                 'Para verificar se a sua versão é a mais recente, acesse: chrome://settings/help.'
                 '\n'
                 ,key='mensagem aba 1')],
        [sg.Image(r'C:\Users\Usuário\OneDrive\Documentos\GitHub\RoboSior\images\VChromme.png', size=(674, 129))],

                ]

    layout2 = [
        [sg.Text('SOBRE A APLICAÇÃO\n'
                 '\n'
                 'Esta aplicação realiza a manipulação do SIOR de maneira automatizada com o objetivo de: \n'
                 '\n'
                 '1 - Extrair dados\n'
                 '2 - Realizar o download de documentos\n'
                 '3 - Consultar algumas informações referente aos autos de infração\n'                                        
                 '\n'
                 '\n'
                 'IMPORTANTE.\n'
                 '\n'
                 'Por se tratar de manipulação de um sistema, devido a extremas volatividades do ambiente, será frequente \n'
                 'a necessidade de reiniciar a aplicação.\n'
                 '\n'
                 'Caso o SIOR esteja apresentando instabilidade, orientamos que não utilize a ferramenta e aguarde a normalização.'


                 ,key='mensagem aba 2')
         ]
            ]

    final_layout = [[sg.TabGroup([[sg.Tab('Requisitos', layout1), sg.Tab('Sobre', layout2)]])],
                    [sg.Button("Voltar", key="voltar")],
                    [sg.Text('Desenvolvido por: Carlos Daniel da Silva Alves e Daniel Santos de Almeida.',
                             key='mensagem',
                             size=(55, 0), font=('Segoe UI', 6,))]
                    ]  # Layout abas

    return sg.Window('', finalize=True,
                     layout=final_layout,
                     no_titlebar=True,
                     )

janela = init_help_form()
janela.read()