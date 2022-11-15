import PySimpleGUI as sg
import os
from View.alertas import alert, progress_bar
from View.tela_form import init_janela_form


def init_janela_login():
    # Layout
    sg.SetOptions(background_color='#363636', text_element_background_color='#363636',
                 element_background_color='#363636', scrollbar_color=None, input_elements_background_color='#F7F3EC',
                 button_color=('white', '#4F4F4F'))
    # sg.theme('SystemDefaultForReal')
    layoutcampos = [

        [sg.Text(f'Bem vindo(a), {os.getlogin()} !', size=(50, 0), font=('Segoe UI', 10))],  # Usuario
        [sg.Image('images\Robot.png',size=(400,400))],
        # [sg.Text('Caro colaborador, para o correto funcionamento da aplicação, '
        #          'verique a sua versão do Chromme em: chrome://settings/help  !',
        #          size=(50, 0), font=('Segoe UI', 8),tooltip='chrome://settings/help')],  # Versão
        [sg.Text('Para continuar, realize o login da sua conta no SIOR.', size=(50, 0), font=('Segoe UI', 8))],  # Usuario]
        [sg.Text('CPF ou E-mail (SIOR)',size=(20, 0),font=('Segoe UI',8))], # Usuario
        [sg.Input(size=(50, 0), key='Usuario',font=('Segoe UI',10))], # Usuario

        [sg.Text('Senha (SIOR)', size=(20, 0),font=('Segoe UI',8))],# Senha
        [sg.Input(size=(50, 0), key='Senha', password_char='*',font=('Segoe UI',10))],  # Senha
        [sg.Button('Validar', focus=True, button_color='red', font=('Segoe UI', 10))],
        [sg.Text('',key='mensagem', size=(50, 0), font=('Segoe UI', 8))],  # Usuario

    ]

    return sg.Window('Login',
                       enable_close_attempted_event=True,
                       finalize=True,
                       icon=r'images\robot.ico',layout=layoutcampos)