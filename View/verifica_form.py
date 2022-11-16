from View.alertas import alert


def valida_campos_auto(i, auto):
    if len(auto) < 10 or len(auto) > 10:
        alert('Atenção', f'verificar o tamanho do auto - {auto}, seq.{i + 1}')
        return 0
    elif ' ' in auto:
        alert('Atenção', f'o auto - {auto}, seq.{i + 1}, contém espaço(s) em branco')
        return 0
    elif '\t' in auto:
        alert('Atenção', f'verifique o auto - {auto}, seq.{i + 1}')
        return 0


def valida_campos_docs(relat_financeiro, relat_resumido, na, np):
    if relat_financeiro is False and relat_resumido is False and\
            na is False and np is False:
        alert('Atenção', 'Selecione um documento para baixar.')
        return 0


def valida_campos_pastas(sim, não):
    if sim is False and não is False:
        alert('Atenção', 'Indique se você deseja criar pastas.')
        return 0




