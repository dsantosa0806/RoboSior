import PySimpleGUI as sg
from DataBase.database import consulta_bd


def init_table_form():
    # Layout

    sg.SetOptions(background_color='#363636', text_element_background_color='#363636',
                  element_background_color='#363636', scrollbar_color=None, input_elements_background_color='#F7F3EC',
                  button_color=('white', '#4F4F4F'))

    # Cabeçalho
    headings = ['Auto','DataInfracao','Enquadramento','Valor','Debito','Vencimento','SituacaoFase','index']
    values = [['B123456789', '01/01/1900', 'tESTE', 'R$ 90,45', 'Em Aberto', '01/01/1900', 'Ativo / Publicado Edital NP', 1]]

    layout = [

        [sg.Text("Tabela autos", font=('Segoe UI',12))],
        [sg.Table(values=consulta_bd().values.tolist(), headings=headings,
                  num_rows=10,
                  size=(200, 600),
                  key='-TABLE-',
                  alternating_row_color='lightblue',
                  justification='center',
                  enable_events=False,
                  enable_click_events=False,
                  expand_x=False,
                  expand_y=True,
                  max_col_width=50,


                  )],
        [sg.Button("Voltar", key="voltar"),
         sg.Button("Exportar", key="Exportar")]

    ]

    # Janela
    return sg.Window('Tabela de dados',
                     enable_close_attempted_event=True,
                     finalize=True,
                     no_titlebar=True,
                     resizable=True,
                     icon=r'images\robot.ico').layout(layout)
