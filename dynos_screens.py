# TODO: Criar um sistema de menu funcional
# TODO: Fazer ajustes de design no sistema
#   Padding no input e botoes
#   Bordas no buscador
#   Hover e bordas no selection
#   Margens entre os elementos
#   Fazer bordas arredondadas
#   Cor na barra superior

import PySimpleGUI as sg

# +-----------------------------------------------+
# |              COMPONENTES GERAIS               |
# +-----------------------------------------------+

exibicao = [
    [sg.Text(
        'Arquivos selecionados',
        background_color='#2E2E2E',
        text_color='#D2D2D2',
        font=("Helvetica", 14),
    ),
        sg.Push(background_color='#2E2E2E'),
        sg.Button(
            'Visualizar',
            key='-VISUALIZAR-',
            button_color='#4F4F4F',
            border_width=0,
        )],
    [sg.Output(
        size=(140, 380),
        background_color='#4F4F4F',
        expand_x=False,
        expand_y=False,
        key='-SAIDA-',
        font=("Helvetica", 14),
        text_color='#FFFFFF',
        sbar_arrow_color='#FFFFFF',
        sbar_background_color='#202020',
        sbar_trough_color='#4F4F4F',
    )]
]

menu = [
    [sg.Text(
        'Menu',
        background_color='#2E2E2E',
        text_color='#D2D2D2',
        font=("Helvetica", 14),
    )],
    [sg.Button(
        'Reordenador',
        key='-TELA-REORDENAR-',
        button_color='#1879BB',
        border_width=0,
        font=("Helvetica", 14),
        size=(14, 1),
    )],
    [sg.Button(
        'Renomeador',
        key='-TELA-RENOMEAR-',
        button_color='#0D6358',
        border_width=0,
        font=("Helvetica", 14),
        size=(14, 1),
    )],
]
# sg.Column(menu, size=(175, 380), background_color='#2E2E2E', expand_y=True, expand_x=True),

# +-----------------------------------------------+
# |                 ORGANIZADOR                   |
# +-----------------------------------------------+

organizador = [
    [sg.Text(
        'Diretório',
        background_color='#2E2E2E',
        text_color='#D2D2D2',
        font=("Helvetica", 14),
    )],
    [sg.Input(
        key='-DIRETORIO-',
        background_color='#3D3D3D',
        text_color='#D2D2D2',
        expand_x=True,
        border_width=0,
        font=("Helvetica", 14),
        pad=(8, 8),
    ),
        sg.FolderBrowse(
            button_color='#1879BB',
            button_text='Buscar',
            font=("Helvetica", 12),
            size=(10, 1),
        )],
    [sg.Text(
        'Arquivos',
        background_color='#2E2E2E',
        text_color='#D2D2D2',
        font=("Helvetica", 14),
    )],
    [sg.Input(
        key='-ARQUIVOS-',
        background_color='#3D3D3D',
        text_color='#D2D2D2',
        expand_x=True,
        border_width=0,
        font=("Helvetica", 14),
        pad=(8, 8),
    ),
        sg.FilesBrowse(
            button_color='#1879BB',
            button_text='Buscar',
            font=("Helvetica", 12),
            size=(10, 1),
        )],
    [sg.Text(
        'Nome da nova pasta',
        background_color='#2E2E2E',
        text_color='#D2D2D2',
        font=("Helvetica", 14),
    )],
    [sg.Input(
        key='-NOME-',
        background_color='#3D3D3D',
        text_color='#D2D2D2',
        border_width=0,
        expand_x=True,
        font=("Helvetica", 14),
        pad=(8, 8),
        # do_not_clear=False,
    )],
    [sg.Text(
        'Formatos selecionados',
        background_color='#2E2E2E',
        text_color='#D2D2D2',
        font=("Helvetica", 14),
    )],
    [sg.Input(
        key='-FORMATOS-',
        background_color='#3D3D3D',
        text_color='#D2D2D2',
        expand_x=True,
        border_width=0,
        font=("Helvetica", 14),
        pad=(8, 8),
        # do_not_clear=False,
    )],
    [sg.Text(
        'Arquivos excedentes',
        background_color='#2E2E2E',
        text_color='#D2D2D2',
        font=("Helvetica", 14),
    )],
    [sg.OptionMenu(
        key='-OUTROS-',
        default_value='Deixar na Raíz',
        values=('Deixar na Raíz', 'Adicionar em Outros'),
        background_color='#3D3D3D',
        text_color='#D2D2D2',
        auto_size_text=True,
        pad=(8, 8),
    )],
    [sg.Push(background_color='#2E2E2E'),
     sg.Button(
         'Reordenar',
         key='-REORDENAR-',
         button_color='#1879BB',
         border_width=0,
         font=("Helvetica", 14),
         size=(10, 1),
     )]
]

# +-----------------------------------------------+
# |                 RENOMEADOR                    |
# +-----------------------------------------------+

renomeador = [
    [sg.Text(
        'Diretório',
        background_color='#2E2E2E',
        text_color='#D2D2D2',
        font=("Helvetica", 14),
    )],
    [sg.Input(
        key='-DIRETORIO-',
        background_color='#3D3D3D',
        text_color='#D2D2D2',
        expand_x=True,
        border_width=0,
        font=("Helvetica", 14),
        pad=(8, 8),
    ),
        sg.FolderBrowse(
            button_color='#0D6358',
            button_text='Buscar',
            font=("Helvetica", 12),
            size=(10, 1),
        )],
    [sg.Text(
        'Arquivos',
        background_color='#2E2E2E',
        text_color='#D2D2D2',
        font=("Helvetica", 14),
    )],
    [sg.Input(
        key='-ARQUIVOS-',
        background_color='#3D3D3D',
        text_color='#D2D2D2',
        expand_x=True,
        border_width=0,
        font=("Helvetica", 14),
        pad=(8, 8),
    ),
        sg.FilesBrowse(
            button_color='#0D6358',
            button_text='Buscar',
            font=("Helvetica", 12),
            size=(10, 1),
        )],
    [sg.Text(
        'Nome dos arquivos',
        background_color='#2E2E2E',
        text_color='#D2D2D2',
        font=("Helvetica", 14),
    )],
    [sg.Input(
        key='-NOME-',
        background_color='#3D3D3D',
        text_color='#D2D2D2',
        border_width=0,
        expand_x=True,
        font=("Helvetica", 14),
        pad=(8, 8),
    )],
    [sg.Text(
        'Formatos selecionados',
        background_color='#2E2E2E',
        text_color='#D2D2D2',
        font=("Helvetica", 14),
    )],
    [sg.Input(
        key='-FORMATOS-',
        background_color='#3D3D3D',
        text_color='#D2D2D2',
        expand_x=True,
        border_width=0,
        font=("Helvetica", 14),
        pad=(8, 8),
    )],
    [sg.Push(background_color='#2E2E2E'),
     sg.Button(
         'Renomear',
         key='-RENOMEAR-',
         button_color='#0D6358',
         border_width=0,
         font=("Helvetica", 14),
         size=(10, 1),
     )]
]
