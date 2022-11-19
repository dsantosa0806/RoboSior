import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import re
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException, NoSuchElementException
from View.alertas import alert
## Oh Lord, forgive for what i'm about to Code !


def acessa_sior(navegador):
    try:
        #Acesso a tela de login
        url_login = 'http://servicos.dnit.gov.br/sior/Account/Login/?ReturnUrl=%2Fsior%2F'
        navegador.get(url_login)
    except:
        alert('Erro', 'O SIOR apresentou instabilidade, por favor reinicie a aplicação e tente novamente')


def login(navegador,usuario,senha):
    username = usuario
    userpass = senha
    cpfpath = '// *[ @ id = "UserName"]'
    senhapath = '//*[@id="Password"]'
    clickpath = '//*[@id="FormLogin"]/div[4]/div[2]/button'

    err = True
    while err:

        try:
            WebDriverWait(navegador, 15).until(
                EC.presence_of_element_located(
                    (By.XPATH, cpfpath))).send_keys(username)
            WebDriverWait(navegador, 15).until(
                EC.presence_of_element_located(
                    (By.XPATH, senhapath))).send_keys(userpass)
            WebDriverWait(navegador, 15).until(
                EC.element_to_be_clickable(
                    (By.XPATH, clickpath))).click()

            time.sleep(2)

            err = False

        except TimeoutException:
            alert('Erro', 'O SIOR apresentou instabilidade, por favor reinicie a aplicação e tente novamente')


def validate_login_error(navegador):
    cpfpath = '// *[ @ id = "UserName"]'
    senhapath = '//*[@id="Password"]'
    login_error = '//*[@id="placeholder"]/div[3]/div/div/div/div'

    try:
        navegador.find_element(By.XPATH,login_error).is_displayed()
        navegador.find_element(By.XPATH,cpfpath).clear()
        navegador.find_element(By.XPATH,senhapath).clear()
        return True
    except NoSuchElementException:
        return False


def validate_logado(navegador):
    logado = '//*[@id="center-pane"]/div/div/div[1]/div[2]'
    try:
        WebDriverWait(navegador, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, logado))).is_displayed()
        valor = navegador.find_element(By.XPATH, logado).text
        alert('Acesso', f'Bem-vindo(a), {valor}')
        return True

    except TimeoutException:
        alert('Opss', 'O SIOR apresentou instabilidade, a aplicação será encerrada.'
                      ' Por favor reinicie a aplicação e tente novamente')
        return 0


def acessa_tela_incial_auto(navegador):
    url_base = 'https://servicos.dnit.gov.br/sior/Infracao/ConsultaAutoInfracao/?SituacoesInfracaoSelecionadas=1'
    # Acessa a tela da notificação da autuação
    try:
        navegador.get(url_base)
    except:
        alert('Erro', 'O SIOR apresentou instabilidade, por favor reinicie a aplicação e tente novamente')


def pesquisa_auto(navegador,auto):
    input_ait = auto
    path_auto = '//*[@id="NumeroAuto"]'
    path_btn_closefilter = '//*[@id="SituacoesInfracaoSelecionadas_taglist"]/li/span[2]'
    path_btn_consultar = '//*[@id="placeholder"]/div[1]/div/div[1]/button'
    path_details = '//*[@id="gridInfracao"]/table/tbody/tr/td[1]/a'
    path_menu_relat = '//*[@id="menu_relatorio"]/li/span'
    path_auto_empty = '//*[@id="gridInfracao"]/div[1]'
    class_name_empty_field = 'lt-empty-grid'
    empty_field = 'Nenhum registro encontrado!'

    try:
        WebDriverWait(navegador, 60).until(
            EC.element_to_be_clickable((By.XPATH, path_auto))).clear()
    except TimeoutException:
        alert('Opss', 'O SIOR apresentou instabilidade, a aplicação será encerrada.'
                      ' Por favor reinicie a aplicação e tente novamente')

    # INPUT AIT
    try:
        WebDriverWait(navegador, 10).until(
            EC.element_to_be_clickable((By.XPATH, path_auto))).send_keys(input_ait)
    except TimeoutException:
        alert('Erro', 'O SIOR apresentou instabilidade, por favor reinicie a aplicação e tente novamente')

    # DESABILITA FILTRO AUTO
    if navegador.find_element(By.XPATH,path_btn_closefilter).is_displayed():
        try:
            WebDriverWait(navegador, 10).until(
                EC.element_to_be_clickable((By.XPATH, path_btn_closefilter))).click()
        except TimeoutException:
            alert('Erro', 'O SIOR apresentou instabilidade, por favor reinicie a aplicação e tente novamente')
    else:
        pass
    # REALIZA A CONSULTA
    try:
        WebDriverWait(navegador, 10).until(
            EC.element_to_be_clickable((By.XPATH, path_btn_consultar))).click()
    except TimeoutException:
        alert('Erro', 'O SIOR apresentou instabilidade, por favor reinicie a aplicação e tente novamente')

    #detalhes
    try:
        WebDriverWait(navegador, 10).until(
            EC.element_to_be_clickable((By.XPATH, path_details))).click()

    except TimeoutException:
        if navegador.find_element(By.XPATH,path_auto_empty).is_displayed():
            return True
        else:
            ('Erro', 'O SIOR apresentou instabilidade, por favor reinicie a aplicação e tente novamente')


def download_auto_infracao(navegador):
    time.sleep(1)
    path_auto_infra = '//*[@id="menu_relatorio_mn_active"]/div/ul/li[1]/a'
    path_menu_relat = '//*[@id="menu_relatorio"]/li/span'

    try:
        WebDriverWait(navegador, 10).until(
            EC.element_to_be_clickable((By.XPATH, path_menu_relat))).click()
    except ElementClickInterceptedException:
        alert('Erro', 'O SIOR apresentou instabilidade, por favor reinicie a aplicação e tente novamente')
    time.sleep(1)
    # CLIQUE PARA BAIXAR O AUTO DE INFRACAO
    try:
        WebDriverWait(navegador, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, path_auto_infra))).click()
        time.sleep(7)  # importante manter um Delay de Time, necessário implementar uma função que verifica se o download foi exec

    except ElementClickInterceptedException:
        alert('Erro', 'O SIOR apresentou instabilidade, por favor reinicie a aplicação e tente novamente')


def download_relatorio_resumido(navegador):
    path_id_relatorio = 'btnExportarRelatorioResumido'
    path_menu_relat = '//*[@id="menu_relatorio"]/li/span'
    time.sleep(1)
    try:
        WebDriverWait(navegador, 10).until(
            EC.element_to_be_clickable((By.XPATH, path_menu_relat))).click()
    except ElementClickInterceptedException:
        alert('Erro', 'O SIOR apresentou instabilidade, por favor reinicie a aplicação e tente novamente')

    # CLIQUE PARA BAIXAR RELATÓRIO RESUMIDO
    try:
        WebDriverWait(navegador, 10).until(
            EC.element_to_be_clickable(
                (By.ID, path_id_relatorio))).click()
        time.sleep(
            2)  # importante manter um Delay de Time, necessário implementar uma função que verifica se o download foi exec

    except ElementClickInterceptedException:
        alert('Erro', 'O SIOR apresentou instabilidade, por favor reinicie a aplicação e tente novamente')


def download_relatorio_financeiro(navegador):
    path_id_relatorio_financeiro = 'btnExportarRelatorioFinanceiro'
    path_menu_relat = '//*[@id="menu_relatorio"]/li/span'
    time.sleep(1)
    try:
        WebDriverWait(navegador, 10).until(
            EC.element_to_be_clickable((By.XPATH, path_menu_relat))).click()
    except ElementClickInterceptedException:
        alert('Erro', 'O SIOR apresentou instabilidade, por favor reinicie a aplicação e tente novamente')

    # CLIQUE PARA BAIXAR RELATÓRIO RESUMIDO
    try:
        WebDriverWait(navegador, 10).until(
            EC.element_to_be_clickable(
                (By.ID, path_id_relatorio_financeiro))).click()
        time.sleep(
            2)  # importante manter um Delay de Time, necessário implementar uma função que verifica se o download foi exec

    except ElementClickInterceptedException:
        alert('Erro', 'O SIOR apresentou instabilidade, por favor reinicie a aplicação e tente novamente')


def download_na(navegador):
    # time.sleep(1)
    # ## TRATAMENTO DE URL NA
    # url_base_sior = 'https://servicos.dnit.gov.br/sior/Infracao/ConsultaAutoInfracao/'
    # url = navegador.page_source.encode('utf-8')
    # soup = BeautifulSoup(url, 'html.parser')
    # elementos = str(soup.find_all("div", attrs={"class": 'lt-col-3'}))  # Class padrão da Na SIOR
    # padrao_na = 'DownloadSegundaViaNA/'
    # posicao_na = elementos.find(padrao_na)
    # lenght_na = len('DownloadSegundaViaNA/107851973?numeroAuto=D008521814&ampindicadorComprovacao=2101')
    # url_download_na = re.sub('amp;',"",elementos[posicao_na:posicao_na + lenght_na])
    #
    #
    # # EXECUTANDO O DOWNLOAD NA
    # try:
    #     navegador.get(url_base_sior + url_download_na)  # # DOWNLOAD NA
    #     time.sleep(2)
    #     trata_erro(navegador)
    #
    # except TimeoutException:
    #     alert('Erro', 'O SIOR apresentou instabilidade, por favor reinicie a aplicação e tente novamente')

    path_download_na = '//*[@id="tabInfracao-1"]/fieldset[1]/div[1]/div[3]/a'
    try:
        WebDriverWait(navegador, 10).until(
            EC.element_to_be_clickable((By.XPATH, path_download_na))).click()
        time.sleep(3)
    except ElementClickInterceptedException:
        alert('Erro', 'O SIOR apresentou instabilidade, por favor reinicie a aplicação e tente novamente')


def download_np(navegador):
    # time.sleep(1)
    # ## TRATAMENTO DE URL NA E NP
    # url_base_sior = 'https://servicos.dnit.gov.br/sior/Infracao/ConsultaAutoInfracao/'
    # url = navegador.page_source.encode('utf-8')
    # soup = BeautifulSoup(url, 'html.parser')
    # elementos = str(soup.find_all("div", attrs={"class": 'lt-col-3'}))  # Class padrão da Na SIOR
    # padrao_np = 'DownloadSegundaViaNP/'
    # posicao_np = elementos.find(padrao_np)
    # lenght_np = len('DownloadSegundaViaNP/107851973?numeroAuto=D008521814&amp;indicadorComprovacao=2101')
    # url_download_np = re.sub('amp;',"",elementos[posicao_np:posicao_np + lenght_np])
    #
    # # EXECUTANDO O DOWNLOAD NP
    # try:
    #
    #     navegador.get(url_base_sior + url_download_np)  # # # DOWNLOAD NP
    #     time.sleep(2)
    #     trata_erro(navegador)
    #
    # except TimeoutException:
    #     alert('Erro', 'O SIOR apresentou instabilidade, por favor reinicie a aplicação e tente novamente')

    path_download_np = '//*[@id="tabInfracao-1"]/fieldset[2]/div[1]/div[3]/a'
    try:
        WebDriverWait(navegador, 10).until(
            EC.element_to_be_clickable((By.XPATH, path_download_np))).click()
        time.sleep(3)
    except ElementClickInterceptedException:
        alert('Erro', 'O SIOR apresentou instabilidade, por favor reinicie a aplicação e tente novamente')


def trata_erro(navegador):

    msg_erro = "Server Error in '/sior' Application."
    url_atual = navegador.page_source.encode('utf-8')
    soup_ulr_atual = BeautifulSoup(url_atual, 'html.parser')
    posicao_erro = str(soup_ulr_atual).find(msg_erro)

    if posicao_erro == -1:
        # Download feito com sucesso
        pass
    else:
        navegador.back()  # Deve retornar a tela anterior


def extract_info_ait(navegador):
    situacao_fase_auto_path = '//*[@id="center-pane"]/div/div/div/div[1]/div[2]/div[3]/text()'
    situacao_fase_auto = navegador.find_element(By.XPATH, situacao_fase_auto_path).text
    return situacao_fase_auto

