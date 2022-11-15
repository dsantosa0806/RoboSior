from View.alertas import alert
from View.alertas import alert, progress_bar


def clean_fields(window):
    try:
        window.find_element('auto').Update('')
    except:
        alert('Um Erro ocorreu', 'Contate o administrador')


def reset_fields(event, window):
    try:
        progress_bar('Resetando campos')
        window.find_element('Relatório Financeiro').Update('')
        window.find_element('Relatório Resumido').Update('')
        window.find_element('Notificação de autuação').Update('')
        window.find_element('Notificação de Penalidade').Update('')
        window.find_element('auto').Update('')

    except:
        alert('Um Erro ocorreu', 'Contate o administrador')

