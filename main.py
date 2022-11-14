import os

import pandas as pd
from selenium import webdriver
from Selenium.selenium import login, acessa_sior, pesquisa_auto, acessa_tela_incial_auto, download_relatorio_resumido, \
    validate_login_error, download_na_np
from View.limpa_campos import clean_fields, reset_fields
from View.tela_login import init_janela_login
from View.alertas import alert, progress_bar, loading
from View.tela_form import init_janela_form
import PySimpleGUI as sg


def option_navegador():

    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    download_path =r'C:\Users\Usuário\OneDrive\Documentos\GitHub\RoboSior\autos'
    options.add_experimental_option('prefs', {
        "download.default_directory": download_path,  # change default directory for downloads
        "download.prompt_for_download": False,  # to auto download the file
        "download.directory_upgrade": True,
        "plugins.always_open_pdf_externally": True  # it will not show PDF directly in chrome
    })
    return options


navegador = webdriver.Chrome(chrome_options=option_navegador())


def init_form_login(navegador):
    janela_login = init_janela_login()

    while True:
        event, values = janela_login.read()
        print(event, values)
        if (event == sg.WINDOW_CLOSED
                or event == sg.WINDOW_CLOSE_ATTEMPTED_EVENT):
            janela_login.close()
            navegador.quit()
            break
        if event == "Validar":
            if values['Usuario'] == '' or values['Senha'] == '':
                janela_login['mensagem'].update('Verifique o usuario e senha informados!')
            else:
                ## janela_login['mensagem'].update('Logado !')
                login(navegador,values['Usuario'],values['Senha'])

                if validate_login_error(navegador):
                    janela_login['mensagem'].update('Verifique o usuario e senha informados!')
                else:
                    acessa_tela_incial_auto(navegador)
                    janela_login.close()
                    init_form_principal()


def init_form_principal():
    janela_form = init_janela_form()
    while True:

        event, values = janela_form.read()  # Ativa a Janela
        # print(event, values)
        if (event == sg.WINDOW_CLOSED
            or event == 'Sair'
            or event == sg.WINDOW_CLOSE_ATTEMPTED_EVENT)\
                and sg.popup_yes_no('Deseja Sair',
                                    icon=r'images\robot.ico',font=('Segoe UI',10)) == 'Yes':
            janela_form.close()
            navegador.quit()
            break
## Botao limpar
        if event == "Limpar":
            clean_fields(janela_form)
## Botao Resetar
        if event == "Resetar":
            reset_fields(event,janela_form)
## Botao Iniciar
        if event == "Iniciar":
            auto = values['auto'].split('\n')
            #criação do DF
            df = pd.DataFrame(data=auto, columns=['autos'])
            #Diretório
            diretorio = 'autos'
            limite_array = 10
            # if not os.path.exists(diretorio):
            #     os.mkdir(diretorio)
            if len(auto) >= limite_array:
                alert('Atenção','O limite de 10 autos foi atingido')

            for i, auto in enumerate(df['autos']):
                if len(auto) < 10 or len(auto) > 10:
                    print(f'verificar o tamanho do auto - {auto}, seq.{i+1}')
                    alert('Atenção', f'verificar o tamanho do auto - {auto}, seq.{i+1}')
                    break
                elif ' ' in auto:
                    print(f'o auto - {auto}, seq.{i+1} contém espaço(s) em branco')
                    alert('Atenção', f'o auto - {auto}, seq.{i+1}, contém espaço(s) em branco')
                    break
                elif '\t' in auto:
                    print(f'verifique o auto - {auto}, seq.{i+1}')
                    alert('Atenção', f'verifique o auto - {auto}, seq.{i+1}')
                    break
                else:
                    # if not os.path.exists(diretorio + '\\' + str(auto)):
                    #     os.mkdir(diretorio + '\\' + str(auto))
                    # else:
                    #     alert('Atenção', f'verifique o auto - {auto}, seq.{i+1}, O diretório já existe.')
                    print(f'Baixando auto - {auto} ')
                    pesquisa_auto(navegador, auto)
                    download_relatorio_resumido(navegador)
                    df['relatório'] = 'Ok'
                    download_na_np(navegador)
                    df['NotificacaoNA'] = 'Ok'
                    df['NotificacaoNP'] = 'Ok'
                    print(f'Finalizado')
                    acessa_tela_incial_auto(navegador)

                alert('Sucesso !', 'Os arquivos foram baixados !')
            df.to_csv("saida.csv", encoding='utf-8')


acessa_sior(navegador)
init_form_login(navegador)


