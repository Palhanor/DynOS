import os
import re
import shutil
import PySimpleGUI as sg
from dynos_defs import ajusta_formatos, arquivos_selecionados, adiciona_outros
from dynos_screens import \
    menu_organizador, organizador, exibicao_organizador, \
    menu_renomeador, renomeador, exibicao_renomeador


def janela_organizador():
    layout = [
        [
            sg.Column(menu_organizador, size=(175, 380), background_color='#2E2E2E', expand_y=True, expand_x=True),
            sg.Column(organizador, background_color='#2E2E2E', expand_x=True, expand_y=True, key='-SCREEN-'),
            sg.Column(exibicao_organizador, background_color='#2E2E2E', expand_x=True, expand_y=True),
        ]
    ]
    return sg.Window(
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
        finalize=True
    )


def janela_renomeador():
    layout = [
        [
            sg.Column(menu_renomeador, size=(175, 380), background_color='#2E2E2E', expand_y=True, expand_x=True),
            sg.Column(renomeador, background_color='#2E2E2E', expand_x=True, expand_y=True, key='-SCREEN-'),
            sg.Column(exibicao_renomeador, background_color='#2E2E2E', expand_x=True, expand_y=True),
        ]
    ]
    return sg.Window(
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
        finalize=True
    )


tela_organizador, tela_renomeador = janela_organizador(), None
renomeador_is_opened = False
while True:
    window, event, values = sg.read_all_windows()

    if (window == tela_organizador or window == tela_renomeador) and event == sg.WINDOW_CLOSED:
        break

    if window == tela_organizador:
        diretorio = values['-DIRETORIO-']
        arquivos = values['-ARQUIVOS-']
        nome = values['-NOME-']
        formatos = ajusta_formatos(values['-FORMATOS-'])
        outros = values['-OUTROS-']

        nome_valido = nome and not re.search('[\\\\/:*?"<>|]', nome)
        pode_visualizar = diretorio or arquivos
        pode_reordenar = pode_visualizar and nome_valido

        if event == '-TELA-RENOMEAR-':
            if not renomeador_is_opened:
                tela_renomeador = janela_renomeador()
                renomeador_is_opened = True
            tela_renomeador.un_hide()
            tela_organizador.hide()

        elif event == '-TELA-REORDENAR-':
            if renomeador_is_opened:
                tela_organizador.un_hide()
                tela_renomeador.hide()
            else:
                pass

        elif event == '-VISUALIZAR-':
            if pode_visualizar:
                diretorio_arquivos_selecionados, lista_arquivos_selecionados = \
                    arquivos_selecionados(diretorio, arquivos, formatos)
                window['-SAIDA-ORDENADOR-'].Update('')
                for arquivo in lista_arquivos_selecionados:
                    window['-SAIDA-ORDENADOR-'].print(arquivo, text_color='#D2D2D2')

        elif event == '-REORDENAR-':
            if pode_reordenar:
                diretorio_arquivos_selecionados, lista_arquivos_selecionados = \
                    arquivos_selecionados(diretorio, arquivos, formatos)
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

                window['-SAIDA-ORDENADOR-'].Update('')

    elif window == tela_renomeador:
        diretorio = values['-DIRETORIO-']
        arquivos = values['-ARQUIVOS-']
        nome = values['-NOME-']
        formatos = ajusta_formatos(values['-FORMATOS-'])

        nome_valido = not re.search('[\\\\/:*?"<>|]', nome)
        pode_visualizar = diretorio or arquivos
        pode_renomear = pode_visualizar and nome_valido

        contador = 1

        if event == '-TELA-REORDENAR-':
            tela_organizador.un_hide()
            tela_renomeador.hide()

        elif event == '-TELA-RENOMEAR-':
            tela_renomeador.un_hide()
            tela_organizador.hide()

        elif event == '-VISUALIZAR-':
            if pode_visualizar:
                diretorio_arquivos_selecionados, lista_arquivos_selecionados = \
                    arquivos_selecionados(diretorio, arquivos, formatos)
                window['-SAIDA-RENOMEADOR-'].Update('')
                for arquivo in lista_arquivos_selecionados:
                    window['-SAIDA-RENOMEADOR-'].print(arquivo, text_color='#D2D2D2')

        elif event == '-RENOMEAR-':
            if pode_renomear:
                diretorio_arquivos_selecionados, lista_arquivos_selecionados = \
                    arquivos_selecionados(diretorio, arquivos, formatos)
                arquivos_diretorio = os.listdir(diretorio_arquivos_selecionados)
                for arquivo in arquivos_diretorio:
                    if arquivo in lista_arquivos_selecionados:
                        if nome == '':
                            nome = re.sub(r'^.*/', '', diretorio_arquivos_selecionados)
                        formato = os.path.splitext(arquivo)[1]
                        rota = os.path.join(diretorio_arquivos_selecionados, arquivo)
                        new_file = f'{nome} #{str(contador).zfill(3)}' + formato
                        new_path = os.path.join(diretorio_arquivos_selecionados, new_file)
                        os.rename(rota, new_path)
                        contador += 1
                window['-SAIDA-RENOMEADOR-'].Update('')

window.close()
