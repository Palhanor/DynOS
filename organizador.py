import os
import re
import shutil
import PySimpleGUI as sg

# TODO: Adicionar um campo com a pasta de destino?

# TODO: Criar biblioteca para funcções e telas dos projetos
# TODO: Criar um sistema de menu
# TODO: Fazer ajustes de design no sistema
#   Padding no input e botoes
#   Bordas no buscador
#   Hover e bordas no selection
#   Margens entre os elementos
#   Fazer bordas arredondadas
#   Cor na barra superior

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

# menu = [
#     [sg.Text(
#         'Menu',
#         background_color='#2E2E2E',
#         text_color='#D2D2D2',
#         font=("Helvetica", 14),
#     )],
#     [sg.Button(
#         'Reordenador',
#         key='-TELA-REORDENAR-',
#         button_color='#1879BB',
#         border_width=0,
#         font=("Helvetica", 14),
#         size=(14, 1),
#     )],
#     [sg.Button(
#         'Renomeador',
#         key='-TELA-RENOMEAR-',
#         button_color='#0D6358',
#         border_width=0,
#         font=("Helvetica", 14),
#         size=(14, 1),
#     )],
# ]

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

layout = [
    [
        # sg.Column(menu, size=(175, 380), background_color='#2E2E2E', expand_y=True, expand_x=True),
        sg.Column(organizador, background_color='#2E2E2E', expand_x=True, expand_y=True, key='-SCREEN-'),
        sg.Column(exibicao, background_color='#2E2E2E', expand_x=True, expand_y=True),
    ]
]

window = sg.Window(
    'DynOS - Organizador',
    layout,
    background_color='#202020',
    margins=(20, 20),
    resizable=True,
    size=(1280, 480),
    icon='./dynos.ico',
    titlebar_background_color='#3D3D3D',
    titlebar_text_color='#D2D2D2',
    font=("Helvetica", 12),
)


def ajusta_formatos(lista_formatos):
    lista_formatos = lista_formatos.replace(' ', '').split(',')
    nova_lista_formatos = []
    for formato_declarado in lista_formatos:
        if len(formato_declarado) >= 1 and formato_declarado[0] == '.':
            nova_lista_formatos.append(formato_declarado)
        elif len(formato_declarado) >= 1 and formato_declarado[0] != '.':
            nova_lista_formatos.append('.' + formato_declarado)
    return nova_lista_formatos


def arquivos_selecionados(entrada_diretorio, entrada_arquivos):
    # TODO: Implementar retorno direto dos arquivos selecionados
    if entrada_arquivos:
        lista_arquivos = arquivos.split(';')
        lista_arquivos_ajustada = []
        diretorio_arquivos = re.search(r'^.*/', lista_arquivos[0])
        diretorio_arquivos_formato = diretorio_arquivos.group()
        for arquivo_iterado in lista_arquivos:
            novo_arquivo = re.sub(r'^.*/', '', arquivo_iterado)
            lista_arquivos_ajustada.append(novo_arquivo)
        return diretorio_arquivos_formato, lista_arquivos_ajustada
    elif entrada_diretorio and not arquivos:
        lista_arquivos = os.listdir(entrada_diretorio)
        return entrada_diretorio, lista_arquivos


def adiciona_outros(diretorio_selecionado):
    arquivos_diretorio_selecionado = os.listdir(diretorio_selecionado)
    novo_diretorio_outros = os.path.join(diretorio_selecionado, 'Outros')
    if 'Outros' not in arquivos_diretorio_selecionado:
        os.mkdir(novo_diretorio_outros)

    for arquivo_restante in arquivos_diretorio_selecionado:
        rota_arquivo = os.path.join(diretorio_selecionado, arquivo_restante)
        if os.path.isfile(rota_arquivo):
            destino_arquivo = os.path.join(diretorio_selecionado, novo_diretorio_outros, arquivo_restante)
            shutil.copyfile(rota_arquivo, destino_arquivo)
            os.remove(rota_arquivo)


while True:
    event, values = window.read()

    diretorio = values['-DIRETORIO-']
    arquivos = values['-ARQUIVOS-']
    nome = values['-NOME-']
    formatos = ajusta_formatos(values['-FORMATOS-'])
    outros = values['-OUTROS-']

    diretorio_arquivos_selecionados, lista_arquivos_selecionados = \
        arquivos_selecionados(diretorio, arquivos)

    nome_valido = nome and not re.search('[\\\\/:*?"<>|]', nome)
    pode_visualizar = diretorio or arquivos
    pode_reordenar = pode_visualizar and nome_valido

    if event == sg.WINDOW_CLOSED:
        print('Encerrando!')
        break

    # TODO: Impedir que o sistema quebre quando roda sem diretório ou arquivos alvos (visualizar e reordenar)
    elif event == '-VISUALIZAR-':
        window.FindElement('-SAIDA-').Update('')
        for arquivo in lista_arquivos_selecionados:
            formato = os.path.splitext(arquivo)[1]
            rota = os.path.join(diretorio_arquivos_selecionados, arquivo)
            if os.path.isfile(rota) and (formato.lower() in formatos or len(formatos) == 0):
                print(arquivo)

    elif event == '-REORDENAR-' and nome_valido:
        arquivos_diretorio = os.listdir(diretorio_arquivos_selecionados)
        novo_diretorio = os.path.join(diretorio_arquivos_selecionados, nome)
        if nome not in arquivos_diretorio:
            os.mkdir(novo_diretorio)

        for arquivo in lista_arquivos_selecionados:
            formato = os.path.splitext(arquivo)[1]
            rota = os.path.join(diretorio_arquivos_selecionados, arquivo)
            if os.path.isfile(rota):
                if formato.lower() in formatos or len(formatos) == 0:
                    destino = os.path.join(diretorio_arquivos_selecionados, novo_diretorio, arquivo)
                    shutil.copyfile(rota, destino)
                    os.remove(rota)

        if outros == 'Adicionar em Outros':
            adiciona_outros(diretorio_arquivos_selecionados)

        window.FindElement('-SAIDA-').Update('')

window.close()
