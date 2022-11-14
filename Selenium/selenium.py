import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import re
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException, NoSuchElementException
from View.alertas import alert
## Oh Lord, forgive for what i'm about to do !


def acessa_sior(navegador):
    #Acesso a tela de login
    url_login = 'http://servicos.dnit.gov.br/sior/Account/Login/?ReturnUrl=%2Fsior%2F'
    navegador.get(url_login)


def login(navegador,usuario,senha):
    username = usuario
    userpass = senha #'Trabalho@2021'
    cpfpath = '// *[ @ id = "UserName"]'
    senhapath = '//*[@id="Password"]'
    clickpath = '//*[@id="FormLogin"]/div[4]/div[2]/button'
    userpath = '//*[@id="center-pane"]/div/div/div[1]/div[2]'

    err = True
    while err:

        try:
            WebDriverWait(navegador, 120).until(
                EC.presence_of_element_located(
                    (By.XPATH, cpfpath))).send_keys(username)
            WebDriverWait(navegador, 120).until(
                EC.presence_of_element_located(
                    (By.XPATH, senhapath))).send_keys(userpass)
            WebDriverWait(navegador, 120).until(
                EC.element_to_be_clickable(
                    (By.XPATH, clickpath))).click()

            time.sleep(2)

            err = False

        except TimeoutException:
            alert('Loading', 'Aguardando...')


def validate_login_error(navegador):
    cpfpath = '// *[ @ id = "UserName"]'
    senhapath = '//*[@id="Password"]'
    login_error = '//*[@id="placeholder"]/div[3]/div/div/div/div'

    try:
        navegador.find_element(By.XPATH,login_error).is_displayed()
        alert('Error', 'Erro ao realizar o Login, verifique os dados e tente novamente')
        navegador.find_element(By.XPATH,cpfpath).clear()
        navegador.find_element(By.XPATH,senhapath).clear()
        return True
    except NoSuchElementException:
        return False


def acessa_tela_incial_auto(navegador):
    url_base = 'https://servicos.dnit.gov.br/sior/Infracao/ConsultaAutoInfracao/?SituacoesInfracaoSelecionadas=1'
    # Acessa a tela da notificação da autuação
    try:
        navegador.get(url_base)
    except:
        alert('Loading', 'Aguardando...')


def pesquisa_auto(navegador,auto):

    input_ait = auto
    path_auto = '//*[@id="NumeroAuto"]'
    path_btn_closefilter = '//*[@id="SituacoesInfracaoSelecionadas_taglist"]/li/span[2]'
    path_btn_consultar = '//*[@id="placeholder"]/div[1]/div/div[1]/button'
    path_details = '//*[@id="gridInfracao"]/table/tbody/tr/td[1]/a'
    path_menu_relat = '//*[@id="menu_relatorio"]/li/span'

    try:
        WebDriverWait(navegador, 10).until(
            EC.element_to_be_clickable((By.XPATH, path_auto))).clear()
    except TimeoutException:
        alert('Loading', 'Aguardando...')

    # INPUT AIT
    try:
        WebDriverWait(navegador, 10).until(
            EC.element_to_be_clickable((By.XPATH, path_auto))).send_keys(input_ait)
    except TimeoutException:
        alert('Loading', 'Aguardando...')

    # DESABILITA FILTRO AUTO
    if navegador.find_element(By.XPATH,path_btn_closefilter).is_displayed():
        try:
            WebDriverWait(navegador, 10).until(
                EC.element_to_be_clickable((By.XPATH, path_btn_closefilter))).click()
        except TimeoutException:
            alert('Loading', 'Aguardando...')
    else:
        pass

    # REALIZA A CONSULTA
    try:
        WebDriverWait(navegador, 10).until(
            EC.element_to_be_clickable((By.XPATH, path_btn_consultar))).click()
    except TimeoutException:
        alert('Loading', 'Aguardando...')

    #detalhes
    try:
        WebDriverWait(navegador, 10).until(
            EC.element_to_be_clickable((By.XPATH, path_details))).click()

    except TimeoutException:
        alert('Loading', 'Aguardando...')

    # CLIQUE PARA ABRIR MENU
    try:
        WebDriverWait(navegador, 120).until(
            EC.element_to_be_clickable((By.XPATH, path_menu_relat))).click()

    except ElementClickInterceptedException:
        alert('Loading', 'Aguardando...')


def download_relatorio_resumido(navegador):
    path_id_relatorio = 'btnExportarRelatorioResumido'
    path_menu_relat = '//*[@id="menu_relatorio"]/li/span'

    try:
        WebDriverWait(navegador, 120).until(
            EC.element_to_be_clickable((By.XPATH, path_menu_relat))).click()
    except ElementClickInterceptedException:
        print('Travei no sexto passo, clique em abrir o menu')

    # CLIQUE PARA BAIXAR RELATÓRIO RESUMIDO
    try:
        WebDriverWait(navegador, 120).until(
            EC.element_to_be_clickable(
                (By.ID, path_id_relatorio))).click()
        time.sleep(
            3)  # importante manter um Delay de Time, necessário implementar uma função que verifica se o download foi exec

    except ElementClickInterceptedException:
        print('Travei no 7 passo, clique em Baixar Relatório o menu')


def download_na_np(navegador):
    ## TRATAMENTO DE URL NA E NP
    urlBaseSior = 'https://servicos.dnit.gov.br/sior/Infracao/ConsultaAutoInfracao/'
    Url = navegador.page_source.encode('utf-8')
    soup = BeautifulSoup(Url, 'html.parser')
    elementos = str(soup.find_all("div", attrs={"class": 'lt-col-3'}))  # Class padrão da Na SIOR
    padrao_na = 'DownloadSegundaViaNA/'
    padrao_np = 'DownloadSegundaViaNP/'
    posicaoNa = elementos.find(padrao_na)
    posicaoNp = elementos.find(padrao_np)
    LenghtNa = len('DownloadSegundaViaNA/107851973?numeroAuto=D008521814&ampindicadorComprovacao=2101')
    LenghtNp = len('DownloadSegundaViaNP/107851973?numeroAuto=D008521814&amp;indicadorComprovacao=2101')
    LenghtCodInfraNp = len('DownloadSegundaViaNP/xxxxxxxxx')
    LenghtCodInfraNa = len('DownloadSegundaViaNA/xxxxxxxxx')
    urlDownloadNa = re.sub('amp;',"",elementos[posicaoNa:posicaoNa + LenghtNa])
    urlDownloadNp = re.sub('amp;',"",elementos[posicaoNp:posicaoNp + LenghtNp])
    padrao_CodInfra_Na = 'DownloadSegundaViaNA/'
    padrao_CodInfra_Np = 'DownloadSegundaViaNP/'

    'https://servicos.dnit.gov.br/sior/Infracao/ConsultaAutoInfracao/DownloadSegundaViaNP/118072531?numeroAuto=E002265146&amp;indicadorComprovacao='
    'https://servicos.dnit.gov.br/sior/Infracao/ConsultaAutoInfracao/DownloadSegundaViaNA/91599795?numeroAuto=E002265146&indicadorComprovacao=2101'



    posicaoCodInfraNa = urlDownloadNa.find(padrao_CodInfra_Na)
    posicaoCodInfraNp = urlDownloadNp.find(padrao_CodInfra_Np)
    codInfracaoNa = urlDownloadNa[len(padrao_CodInfra_Na):LenghtCodInfraNa]
    codInfracaoNp = urlDownloadNp[len(padrao_CodInfra_Np):LenghtCodInfraNp]


    # EXECUTANDO O DOWNLOAD NA, NP, AR

    try:
        navegador.get(urlBaseSior + urlDownloadNa)  # # DOWNLOAD NA
        time.sleep(2)
        trata_erro(navegador)

        navegador.get(urlBaseSior + urlDownloadNp)  # # # DOWNLOAD NP
        time.sleep(2)
        trata_erro(navegador)

    except TimeoutException:
        alert('Loading', 'Aguardando...')


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

