import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException, NoSuchElementException
from View.alertas import alert, alert_notify
## Oh Lord, forgive for what i'm about to Code !


def acessa_sior(navegador):
    try:
        #Acesso a tela de login
        url_login = 'http://servicos.dnit.gov.br/sior/Account/Login/?ReturnUrl=%2Fsior%2F'
        navegador.get(url_login)
    except ValueError:
        alert('Erro', 'O SIOR apresentou instabilidade, por favor reinicie a aplicação e tente novamente')
        exit()


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
            exit()


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
    # Acessa a tela da notificação da autuação
    url_base = 'https://servicos.dnit.gov.br/sior/Infracao/ConsultaAutoInfracao/?SituacoesInfracaoSelecionadas=1'
    try:
        navegador.get(url_base)
    except ValueError:
        alert('Erro', 'O SIOR apresentou instabilidade, por favor reinicie a aplicação e tente novamente')
        exit()


def pesquisa_auto(navegador,auto):
    input_ait = auto
    path_auto = '//*[@id="NumeroAuto"]'
    path_btn_closefilter = '//*[@id="SituacoesInfracaoSelecionadas_taglist"]/li/span[2]'
    path_btn_consultar = '//*[@id="placeholder"]/div[1]/div/div[1]/button'
    path_details = '//*[@id="gridInfracao"]/table/tbody/tr/td[1]/a'
    path_auto_empty = '//*[@id="gridInfracao"]/div[1]'

    try:
        WebDriverWait(navegador, 60).until(
            EC.element_to_be_clickable((By.XPATH, path_auto))).clear()
    except TimeoutException:
        alert('Opss', 'O SIOR apresentou instabilidade, a aplicação será encerrada.'
                      ' Por favor reinicie a aplicação e tente novamente')
        exit()

    # INPUT AIT
    try:
        WebDriverWait(navegador, 10).until(
            EC.element_to_be_clickable((By.XPATH, path_auto))).send_keys(input_ait)
    except TimeoutException:
        alert('Erro', 'O SIOR apresentou instabilidade, por favor reinicie a aplicação e tente novamente')
        exit()

    # DESABILITA FILTRO AUTO
    if navegador.find_element(By.XPATH,path_btn_closefilter).is_displayed():
        try:
            WebDriverWait(navegador, 10).until(
                EC.element_to_be_clickable((By.XPATH, path_btn_closefilter))).click()
        except TimeoutException:
            alert('Erro', 'O SIOR apresentou instabilidade, por favor reinicie a aplicação e tente novamente')
            exit()
    else:
        pass
    # REALIZA A CONSULTA
    try:
        WebDriverWait(navegador, 10).until(
            EC.element_to_be_clickable((By.XPATH, path_btn_consultar))).click()
    except TimeoutException:
        alert('Erro', 'O SIOR apresentou instabilidade, por favor reinicie a aplicação e tente novamente')
        exit()

    #detalhes & Captura dados
    try:
        WebDriverWait(navegador, 10).until(
            EC.element_to_be_clickable((By.XPATH, path_details))).click()
    except TimeoutException:
        if navegador.find_element(By.XPATH,path_auto_empty).is_displayed():
            return True
        else:
            alert('Erro', 'O SIOR apresentou instabilidade, por favor reinicie a aplicação e tente novamente')
            exit()


def download_auto_infracao(navegador):
    path_auto_infra = '//*[@id="menu_relatorio_mn_active"]/div/ul/li[1]/a'
    path_menu_relat = '//*[@id="menu_relatorio"]/li/span'

    try:
        WebDriverWait(navegador, 10).until(
            EC.element_to_be_clickable((By.XPATH, path_menu_relat))).click()
        WebDriverWait(navegador, 10).until(
            EC.element_to_be_clickable((By.XPATH, path_auto_infra))).click()
    except ElementClickInterceptedException:
        alert_notify('Erro', 'O SIOR apresentou instabilidade, por favor reinicie a aplicação e tente novamente')
        exit()


def download_relatorio_resumido(navegador):
    path_id_relatorio = 'btnExportarRelatorioResumido'
    path_menu_relat = '//*[@id="menu_relatorio"]/li/span'
    try:
        WebDriverWait(navegador, 10).until(
            EC.element_to_be_clickable((By.XPATH, path_menu_relat))).click()
    except ElementClickInterceptedException:
        alert_notify('Erro', 'O SIOR apresentou instabilidade, por favor reinicie a aplicação e tente novamente')
        exit()

    # CLIQUE PARA BAIXAR RELATÓRIO RESUMIDO
    try:
        WebDriverWait(navegador, 10).until(
            EC.element_to_be_clickable(
                (By.ID, path_id_relatorio))).click()
    except ElementClickInterceptedException:
        alert_notify('Erro', 'O SIOR apresentou instabilidade, por favor reinicie a aplicação e tente novamente')
        exit()


def download_relatorio_financeiro(navegador):
    path_id_relatorio_financeiro = 'btnExportarRelatorioFinanceiro'
    path_menu_relat = '//*[@id="menu_relatorio"]/li/span'
    try:
        WebDriverWait(navegador, 10).until(
            EC.element_to_be_clickable((By.XPATH, path_menu_relat))).click()
    except ElementClickInterceptedException:
        alert_notify('Erro', 'O SIOR apresentou instabilidade, por favor reinicie a aplicação e tente novamente')
        exit()

    # CLIQUE PARA BAIXAR RELATÓRIO RESUMIDO
    try:
        WebDriverWait(navegador, 10).until(
            EC.element_to_be_clickable(
                (By.ID, path_id_relatorio_financeiro))).click()
    except ElementClickInterceptedException:
        alert('Erro', 'O SIOR apresentou instabilidade, por favor reinicie a aplicação e tente novamente')
        exit()


def download_na(navegador):
    path_download_na = '//*[@id="tabInfracao-1"]/fieldset[1]/div[1]/div[3]/a'
    try:
        WebDriverWait(navegador, 10).until(
            EC.element_to_be_clickable((By.XPATH, path_download_na))).click()
    except ElementClickInterceptedException:
        alert_notify('Erro', 'O SIOR apresentou instabilidade, por favor reinicie a aplicação e tente novamente')
        exit()


def download_np(navegador):
    path_download_np = '//*[@id="tabInfracao-1"]/fieldset[2]/div[1]/div[3]/a'
    try:
        WebDriverWait(navegador, 10).until(
            EC.element_to_be_clickable((By.XPATH, path_download_np))).click()
    except ElementClickInterceptedException:
        alert_notify('Erro', 'O SIOR apresentou instabilidade, por favor reinicie a aplicação e tente novamente')
        exit()


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


def extract_info_ait(navegador, auto):

    path_auto_text = '//*[@id="gridInfracao"]/table/tbody/tr/td[2]'
    path_data_infra = '//*[@id="gridInfracao"]/table/tbody/tr/td[4]'
    path_enquadramento = '//*[@id="gridInfracao"]/table/tbody/tr/td[5]'
    path_valor = '//*[@id="gridInfracao"]/table/tbody/tr/td[11]'
    path_debito = '//*[@id="gridInfracao"]/table/tbody/tr/td[13]'
    path_vencimento_np = '//*[@id="gridInfracao"]/table/tbody/tr/td[12]'
    path_situacao_fase_auto = '//*[@id="gridInfracao"]/table/tbody/tr/td[15]'

    input_ait = auto
    path_auto = '//*[@id="NumeroAuto"]'
    path_btn_closefilter = '//*[@id="SituacoesInfracaoSelecionadas_taglist"]/li/span[2]'
    path_btn_consultar = '//*[@id="placeholder"]/div[1]/div/div[1]/button'

    try:
        WebDriverWait(navegador, 60).until(
            EC.element_to_be_clickable((By.XPATH, path_auto))).clear()
    except TimeoutException:
        alert('Opss', 'O SIOR apresentou instabilidade, a aplicação será encerrada.'
                      ' Por favor reinicie a aplicação e tente novamente')
        exit()

    # INPUT AIT
    try:
        WebDriverWait(navegador, 10).until(
            EC.element_to_be_clickable((By.XPATH, path_auto))).send_keys(input_ait)
    except TimeoutException:
        alert('Erro', 'O SIOR apresentou instabilidade, por favor reinicie a aplicação e tente novamente')
        exit()

    # DESABILITA FILTRO AUTO
    if navegador.find_element(By.XPATH,path_btn_closefilter).is_displayed():
        try:
            WebDriverWait(navegador, 10).until(
                EC.element_to_be_clickable((By.XPATH, path_btn_closefilter))).click()
        except TimeoutException:
            alert('Erro', 'O SIOR apresentou instabilidade, por favor reinicie a aplicação e tente novamente')
            exit()
    else:
        pass
    # REALIZA A CONSULTA
    try:
        WebDriverWait(navegador, 10).until(
            EC.element_to_be_clickable((By.XPATH, path_btn_consultar))).click()
    except TimeoutException:
        alert('Erro', 'O SIOR apresentou instabilidade, por favor reinicie a aplicação e tente novamente')
        exit()

    # Auto
    try:
        auto = WebDriverWait(navegador, 10).until(
            EC.element_to_be_clickable((By.XPATH, path_auto_text))).text
        data_infra = WebDriverWait(navegador, 10).until(
            EC.element_to_be_clickable((By.XPATH, path_data_infra))).text
        enquadramento = WebDriverWait(navegador, 10).until(
            EC.element_to_be_clickable((By.XPATH, path_enquadramento))).text
        valor = WebDriverWait(navegador, 10).until(
            EC.element_to_be_clickable((By.XPATH, path_valor))).text
        debito = WebDriverWait(navegador, 10).until(
            EC.element_to_be_clickable((By.XPATH, path_debito))).text
        vencimento = WebDriverWait(navegador, 10).until(
            EC.element_to_be_clickable((By.XPATH, path_vencimento_np))).text
        situacao_fase = WebDriverWait(navegador, 10).until(
            EC.element_to_be_clickable((By.XPATH, path_situacao_fase_auto))).text

        return auto, data_infra, enquadramento, valor, debito, vencimento, situacao_fase

    except ElementClickInterceptedException:
        alert('Erro', 'O SIOR apresentou instabilidade, por favor reinicie a aplicação e tente novamente')
        exit()
