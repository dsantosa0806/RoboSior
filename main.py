import pandas as pd
from selenium import webdriver
from DataBase.database import create_db, cadastrar_demanda_base, export_dados, clean_bd
from Selenium.selenium import login, acessa_sior, pesquisa_auto, acessa_tela_incial_auto, download_relatorio_resumido, \
    validate_login_error, download_na, download_np, download_relatorio_financeiro, \
    download_auto_infracao, validate_logado, extract_info_ait
from View.ajuda import init_help_form
from View.diretorios import diretorios_exec, no_diretorio_exec, clean_diretorio_autos, verify_downloads, \
    create_diretorios_arquivos
from View.limpa_campos import clean_fields, reset_fields
from View.tabela import init_table_form
from View.tela_login import init_janela_login
from View.alertas import alert, init_janela_apresentacao, alert_notify
from View.tela_form import init_janela_form
import PySimpleGUI as sg
from View.verifica_form import valida_campos_auto, valida_campos_docs, valida_campos_pastas, valida_campos_senha
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def option_navegador():

    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Oculta o navegador
    download_path = r'C:\Robot autos'
    options.add_experimental_option('prefs', {
        "download.default_directory": download_path,  # change default directory for downloads
        "download.prompt_for_download": False,  # to auto download the file
        "download.directory_upgrade": True,
        "plugins.always_open_pdf_externally": True  # it will not show PDF directly in chrome
    })
    return options


navegador = webdriver.Chrome(options=option_navegador(),service=Service(ChromeDriverManager().install()))


def init_form_login(navegador):
    janela_login = init_janela_login()
    while True:
        event, values = janela_login.read()
        if (event == sg.WINDOW_CLOSED
                or event == sg.WINDOW_CLOSE_ATTEMPTED_EVENT):
            janela_login.close()
            navegador.quit()
            break
        if event == "Validar":
            janela_login['mensagem'].update('')
            janela_login.refresh()
            if valida_campos_senha(values['Usuario'], values['Senha']):
                janela_login['mensagem'].update('Atenção ! Verifique o usuario e senha informados.')
            else:
                ## janela_login['mensagem'].update('Logado !')
                login(navegador,values['Usuario'],values['Senha'])

                if validate_login_error(navegador):
                    janela_login['mensagem'].update('Acesso inválido ! Verifique o usuário e senha informados.')
                    janela_login.refresh()
                elif validate_logado(navegador) == 0:
                    janela_login.close()
                    navegador.quit()
                else:
                    janela_login['mensagem'].update('Acesso Validado !')
                    janela_login.refresh()
                    acessa_tela_incial_auto(navegador)
                    janela_login.close()
                    init_form_principal()


def init_form_principal():
    janela_form = init_janela_form()
    while True:
        event, values = janela_form.read()  # Ativa a Janela
        # print(values)
        if (event == sg.WINDOW_CLOSED
            or event == 'Sair'
            or event == sg.WINDOW_CLOSE_ATTEMPTED_EVENT)\
                and sg.popup_yes_no('Deseja Sair',
                                    icon=r'images\robot.ico',
                                    no_titlebar=True,
                                    font=('Segoe UI',10)) == 'Yes':
            janela_form.close()
            navegador.quit()
            break

## Botao Tabela
        if event == "Dados":
            janela_form.hide()
            tabela = init_table_form()
            event_table, values = tabela.read()
            if event_table == "voltar":
                tabela.close()
                janela_form.un_hide()
            if event_table == "Exportar":
                export_dados()
                alert_notify('Aguarde...','Gerando Relatório em Csv')
                tabela.close()
                janela_form.un_hide()
                alert('Relatório gerado !', 'Relatório disponível em: C:\Robot Relatorios')


## Botao Ajuda Requisitos
        if event == "Requisitos":
            janela_form.hide()
            ajuda = init_help_form()
            event_table, values_table = ajuda.read()
            if event_table == "voltar":
                ajuda.close()
                janela_form.un_hide()

## Botao limpar
        if event == "Limpar":
            clean_fields(janela_form)
## Botao Resetar
        if event == "Resetar":
            reset_fields(event,janela_form)
## Botao Iniciar
        if event == "Iniciar":
            clean_bd()
            clean_diretorio_autos()
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
                if valida_campos_docs(values['Auto de Infração'],values['Relatório Financeiro'],values['Relatório Resumido'],
                                      values['Notificação de autuação'],values['Notificação de Penalidade']) == 0:
                    break
                if valida_campos_auto(i,auto) == 0:
                    break
                if valida_campos_pastas(values['PastasSim'],values['PastasNão']) == 0:
                    break
                else:
                    janela_form.hide()

                    if pesquisa_auto(navegador,auto):
                        alert('Erro',f'O auto de infração {auto}, não foi localizado. Verifique a lista e tente novamente')
                        acessa_tela_incial_auto(navegador)
                        break

                    if values['Relatório Financeiro']:
                        alert_notify('Iniciando Relatório financeiro', f'{auto}')
                        download_relatorio_financeiro(navegador)
                    if values['Relatório Resumido']:
                        alert_notify('Iniciando Relatório Resumido', f'{auto}')
                        download_relatorio_resumido(navegador)
                    if values['Notificação de autuação']:
                        alert_notify('Iniciando Notificação de autuação', f'{auto}')
                        download_na(navegador)
                    if values['Notificação de Penalidade']:
                        alert_notify('Iniciando Notificação de Penalidade', f'{auto}')
                        download_np(navegador)
                    if values['Auto de Infração']:
                        alert_notify('Auto de Infração', f'{auto}')
                        download_auto_infracao(navegador)
                    if verify_downloads(values) == 1:
                        alert('Erro','O tempo limite foi alcançado a aplicação será fechada')
                        janela_form.close()
                        navegador.close()
                    if values['PastasSim']:
                        diretorios_exec(auto)
                    else:
                        no_diretorio_exec()
                    print(f'Auto - {auto} - Finalizado! ')

                    acessa_tela_incial_auto(navegador)

                    #
                    auto, data_infra, enquadramento, valor, debito, \
                        vencimento, situacao_fase = extract_info_ait(navegador, auto)

                    cadastrar_demanda_base(auto, data_infra, enquadramento, valor, debito,
                                           vencimento, situacao_fase)

                    acessa_tela_incial_auto(navegador)

            # df.to_csv("relatorio.csv", encoding='utf-8')
            janela_form.un_hide()


create_diretorios_arquivos()
create_db()
init_janela_apresentacao().read()
acessa_sior(navegador)
init_form_login(navegador)
