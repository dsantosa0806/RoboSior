import PySimpleGUI as sg
import pandas as pd

from View.alertas import alert
from View.limpa_campos import clean_fields, reset_fields


def init_janela_form():
    # Layout
    # sg.theme('SystemDefaultForReal')
    sg.SetOptions(background_color='#363636', text_element_background_color='#363636',
                 element_background_color='#363636', scrollbar_color=None, input_elements_background_color='#F7F3EC',
                 button_color=('white', '#4F4F4F'))
    menu = [[sg.Menu(
        [
         ['Inicio'],
         ['Sobre', ['Requisitos']],
         ['Ajuda']]
        )]
    ]

    layoutcampos = [

        [sg.Text('',key='Status')],
        [sg.Text('Quais Documentos deseja baixar ?',font=('Segoe UI',12))],
        [sg.Checkbox('Relatório Financeiro', key='Relatório Financeiro', font=('Segoe UI', 10))],
        [sg.Checkbox('Relatório Resumido', key='Relatório Resumido', font=('Segoe UI',10))],
        [sg.Checkbox('Notificação de autuação', key='Notificação de autuação',font=('Segoe UI',10))],
        [sg.Checkbox('Notificação de Penalidade', key='Notificação de Penalidade',font=('Segoe UI',10))],
        [sg.Text('______________________________')],
        [sg.Text('Insira os autos abaixo ?',font=('Segoe UI',12)),
         sg.Button('Limpar',font=('Segoe UI',10))
         ],
        [sg.Multiline(size=(30, 10),key='auto', font=('Segoe UI',10))],
        [sg.Text('______________________________')],
        [sg.Output(size=(50, 10),font=('Segoe UI',10))],
        [sg.Button('Iniciar',button_color='green',font=('Segoe UI',10)),
         sg.Button('Sair',font=('Segoe UI',10)),sg.Button('Resetar',font=('Segoe UI',10))
         ],
        ## [sg.Image('images\Serget.png', size=(200, 200))],
    ]

    # Janela
    return sg.Window('Baixar Documentos',
                       enable_close_attempted_event=True,
                       finalize=True,
                       icon=r'images\robot.ico').layout(menu + layoutcampos)


