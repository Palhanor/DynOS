import os
import re
import PySimpleGUI as sg

# TODO: Impedir que o sistema quebre caso uma imagem vá ser nomeada como mesmo que outra existente

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
        sg.Column(renomeador, background_color='#2E2E2E', expand_x=True, expand_y=True, key='-SCREEN-'),
        sg.Column(exibicao, background_color='#2E2E2E', expand_x=True, expand_y=True),
    ]
]

window = sg.Window(
    'DynOS - Renomeador',
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
        diretorio_arquivos = re.search(r'^.*/', lista_arquivos[0]).group()
        for arquivo_iterado in lista_arquivos:
            novo_arquivo = re.sub(r'^.*/', '', arquivo_iterado)
            lista_arquivos_ajustada.append(novo_arquivo)
        return diretorio_arquivos, lista_arquivos_ajustada
    elif entrada_diretorio and not arquivos:
        lista_arquivos = os.listdir(entrada_diretorio)
        return entrada_diretorio, lista_arquivos


while True:
    event, values = window.read()

    diretorio = values['-DIRETORIO-']
    arquivos = values['-ARQUIVOS-']
    nome = values['-NOME-']
    formatos = ajusta_formatos(values['-FORMATOS-'])

    diretorio_arquivos_selecionados, lista_arquivos_selecionados = \
        arquivos_selecionados(diretorio, arquivos)

    nome_valido = not re.search('[\\\\/:*?"<>|]', nome)
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

    elif event == '-RENOMEAR-' and nome_valido:
        contador = 1
        arquivos_diretorio = os.listdir(diretorio_arquivos_selecionados)
        for arquivo in arquivos_diretorio:
            formato = os.path.splitext(arquivo)[1]
            rota = os.path.join(diretorio_arquivos_selecionados, arquivo)
            if os.path.isfile(rota):
                if arquivo in lista_arquivos_selecionados and (formato.lower() in formatos or len(formatos) == 0):
                    if nome == '':
                        nome = re.sub(r'^.*/', '', diretorio_arquivos_selecionados)
                    new_file = f'{nome} #{str(contador).zfill(3)}' + formato
                    new_path = os.path.join(diretorio_arquivos_selecionados, new_file)
                    os.rename(rota, new_path)
                    contador += 1
        window.FindElement('-SAIDA-').Update('')

window.close()
