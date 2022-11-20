import PySimpleGUI as sg


def init_table_form():
    # Layout

    sg.SetOptions(background_color='#363636', text_element_background_color='#363636',
                  element_background_color='#363636', scrollbar_color=None, input_elements_background_color='#F7F3EC',
                  button_color=('white', '#4F4F4F'))

    layout = [

        [sg.Text("Tabela autos", font=('Segoe UI',12))],
        [sg.Table([['Auto de infracao', 'Nup', 'Situacao/Fase', 'Situação do Débito']],
                  num_rows=10,
                  size=(200, 500),
                  key='-TABLE-',
                  alternating_row_color='lightblue',
                  justification='center',
                  enable_events=False,
                  enable_click_events=False,
                  expand_x=False,
                  expand_y=True,
                  max_col_width=50

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
