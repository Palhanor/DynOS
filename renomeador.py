# TODO: Impedir que uma imagem receba o nome de outra (o programa quebra)
# TODO: Adicionar campos para remover espaços ou modificar o icone do contador

import os
import re
import PySimpleGUI as sg
from dynos_screens import renomeador, exibicao
from dynos_defs import ajusta_formatos, arquivos_selecionados

layout = [
    [
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

while True:
    event, values = window.read()

    diretorio = values['-DIRETORIO-']
    arquivos = values['-ARQUIVOS-']
    nome = values['-NOME-']
    formatos = ajusta_formatos(values['-FORMATOS-'])

    diretorio_arquivos_selecionados, lista_arquivos_selecionados = \
        arquivos_selecionados(diretorio, arquivos, formatos)

    nome_valido = not re.search('[\\\\/:*?"<>|]', nome)
    pode_visualizar = diretorio or arquivos
    pode_reordenar = pode_visualizar and nome_valido

    if event == sg.WINDOW_CLOSED:
        break

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
            if nome == '':
                nome = re.sub(r'^.*/', '', diretorio_arquivos_selecionados)
            formato = os.path.splitext(arquivo)[1]
            rota = os.path.join(diretorio_arquivos_selecionados, arquivo)
            new_file = f'{nome} #{str(contador).zfill(3)}' + formato
            new_path = os.path.join(diretorio_arquivos_selecionados, new_file)
            os.rename(rota, new_path)
            contador += 1

        window.FindElement('-SAIDA-').Update('')

window.close()
