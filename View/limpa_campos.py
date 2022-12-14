from View.alertas import alert


def clean_fields(window):
    try:
        window.find_element('auto').Update('')
    except ValueError:
        alert('Um Erro ocorreu', 'Contate o administrador')


def reset_fields(event, window):
    try:
        window.find_element('Auto de Infração').Update('')
        window.find_element('Relatório Financeiro').Update('')
        window.find_element('Relatório Resumido').Update('')
        window.find_element('Notificação de autuação').Update('')
        window.find_element('Notificação de Penalidade').Update('')
        window.find_element('auto').Update('')
        window.find_element('PastasSim').Update(False)
        window.find_element('PastasNão').Update(False)
        window.find_element('Output').Update('')
    except ValueError:
        alert('Um Erro ocorreu', 'Contate o administrador')

