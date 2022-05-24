# TODO: Fazer ajustes de design no sistema
#   [] Margens e peddings laterais dos containers com Column
#   [] Adicionar padding no input e nos botões
#   [] Remover as bordas dos buscadores
#   [] Remover o hover e as bordas do selection
#   [] Fazer bordas arredondadas
#   [] Modificar a cor da barra superior

import PySimpleGUI as sg

# +-----------------------------------------------+
# |                 ORGANIZADOR                   |
# +-----------------------------------------------+

menu_organizador = [
    [sg.Push(background_color='#2E2E2E')],
    [sg.Text(
        'Menu',
        background_color='#2E2E2E',
        text_color='#D2D2D2',
        font=("Helvetica", 14),
    )],
    [sg.Push(background_color='#2E2E2E')],
    [sg.Push(background_color='#2E2E2E')],
    [sg.Button(
        'Reordenador',
        key='-TELA-REORDENAR-',
        button_color='#1879BB',
        border_width=0,
        font=("Helvetica", 14),
        size=(14, 1),
    )],
    [sg.Push(background_color='#2E2E2E')],
    [sg.Button(
        'Renomeador',
        key='-TELA-RENOMEAR-',
        button_color='#0D6358',
        border_width=0,
        font=("Helvetica", 14),
        size=(14, 1),
    )]
]

organizador = [
    [sg.Push(background_color='#2E2E2E')],
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

exibicao_organizador = [
    [sg.Push(background_color='#2E2E2E')],
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
    [sg.Push(background_color='#2E2E2E')],
    [sg.Push(background_color='#2E2E2E')],
    [sg.Multiline(
        size=(140, 380),
        background_color='#4F4F4F',
        expand_x=False,
        expand_y=False,
        key='-SAIDA-ORDENADOR-',
        font=("Helvetica", 14),
        text_color='#FFFFFF',
        sbar_arrow_color='#FFFFFF',
        sbar_background_color='#202020',
        sbar_trough_color='#4F4F4F',
    )]
]


# +-----------------------------------------------+
# |                 RENOMEADOR                    |
# +-----------------------------------------------+

menu_renomeador = [
    [sg.Push(background_color='#2E2E2E')],
    [sg.Text(
        'Menu',
        background_color='#2E2E2E',
        text_color='#D2D2D2',
        font=("Helvetica", 14),
    )],
    [sg.Push(background_color='#2E2E2E')],
    [sg.Push(background_color='#2E2E2E')],
    [sg.Button(
        'Reordenador',
        key='-TELA-REORDENAR-',
        button_color='#1879BB',
        border_width=0,
        font=("Helvetica", 14),
        size=(14, 1),
    )],
    [sg.Push(background_color='#2E2E2E')],
    [sg.Button(
        'Renomeador',
        key='-TELA-RENOMEAR-',
        button_color='#0D6358',
        border_width=0,
        font=("Helvetica", 14),
        size=(14, 1),
    )],
]

renomeador = [
    [sg.Push(background_color='#2E2E2E')],
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
    [sg.Push(background_color='#2E2E2E')],
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

exibicao_renomeador = [
    [sg.Push(background_color='#2E2E2E')],
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
    [sg.Push(background_color='#2E2E2E')],
    [sg.Push(background_color='#2E2E2E')],
    [sg.Multiline(
        size=(140, 380),
        background_color='#4F4F4F',
        expand_x=False,
        expand_y=False,
        key='-SAIDA-RENOMEADOR-',
        font=("Helvetica", 14),
        text_color='#FFFFFF',
        sbar_arrow_color='#FFFFFF',
        sbar_background_color='#202020',
        sbar_trough_color='#4F4F4F',
    )]
]
