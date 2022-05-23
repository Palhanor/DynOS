# TODO: Adicionar um campo com a pasta de destino dos arquivos
#   Se o nome for vazio, entra direto na pasta de destino
#   Caso tenha nome, a pasta é criada nessa pasta de destino

import os
import re
import shutil
import PySimpleGUI as sg
from dynos_screens import organizador, exibicao
from dynos_defs import ajusta_formatos, arquivos_selecionados, adiciona_outros

layout = [
    [
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


while True:
    event, values = window.read()

    diretorio = values['-DIRETORIO-']
    arquivos = values['-ARQUIVOS-']
    nome = values['-NOME-']
    formatos = ajusta_formatos(values['-FORMATOS-'])
    outros = values['-OUTROS-']

    diretorio_arquivos_selecionados, lista_arquivos_selecionados = \
        arquivos_selecionados(diretorio, arquivos, formatos)

    nome_valido = nome and not re.search('[\\\\/:*?"<>|]', nome)
    pode_visualizar = diretorio or arquivos
    pode_reordenar = pode_visualizar and nome_valido

    if event == sg.WINDOW_CLOSED:
        break

    elif event == '-VISUALIZAR-':
        window.FindElement('-SAIDA-').Update('')
        for arquivo in lista_arquivos_selecionados:
            print(arquivo)

    elif event == '-REORDENAR-' and nome_valido:
        arquivos_diretorio = os.listdir(diretorio_arquivos_selecionados)
        novo_diretorio = os.path.join(diretorio_arquivos_selecionados, nome)
        if nome not in arquivos_diretorio:
            os.mkdir(novo_diretorio)

        for arquivo in lista_arquivos_selecionados:
            formato = os.path.splitext(arquivo)[1]
            rota = os.path.join(diretorio_arquivos_selecionados, arquivo)
            destino = os.path.join(diretorio_arquivos_selecionados, novo_diretorio, arquivo)
            shutil.copyfile(rota, destino)
            os.remove(rota)

        if outros == 'Adicionar em Outros':
            adiciona_outros(diretorio_arquivos_selecionados)

        window.FindElement('-SAIDA-').Update('')

window.close()
