# TODO: Automatizar o sistema de visualização de arquivos (Organizador e Renomeador)

# TODO: Adicionar campos para remover espaçamento ou modificar o simbolo usado com o contador (Renomeador)

# TODO: Adicionar um campo com a pasta de destino dos arquivos (Organizador)
#   [] Se o nome for vazio, entra direto na pasta de destino
#   [] Caso tenha nome, a pasta é criada nessa pasta de destino
#   [] Usar números negativos para voltar na rota e extair os dados


import os
import re
import shutil

# +-----------------------------------------------+
# |              COMPONENTES GERAIS               |
# +-----------------------------------------------+


def ajusta_formatos(lista_formatos):
    lista_formatos = lista_formatos.replace(' ', '').split(',')
    nova_lista_formatos = []
    for formato_declarado in lista_formatos:
        if len(formato_declarado) >= 1 and formato_declarado[0] == '.':
            nova_lista_formatos.append(formato_declarado)
        elif len(formato_declarado) >= 1 and formato_declarado[0] != '.':
            nova_lista_formatos.append('.' + formato_declarado)
    return nova_lista_formatos


def arquivos_selecionados(entrada_diretorio, entrada_arquivos, formatos):
    if entrada_arquivos:
        lista_arquivos = entrada_arquivos.split(';')
        lista_arquivos_ajustada = []
        diretorio_arquivos = re.search(r'^.*/', lista_arquivos[0])
        diretorio_arquivos_formato = diretorio_arquivos.group()
        for arquivo_iterado in lista_arquivos:
            novo_arquivo = re.sub(r'^.*/', '', arquivo_iterado)
            lista_arquivos_ajustada.append(novo_arquivo)
        return filtro_arquivos_selecionados(diretorio_arquivos_formato, lista_arquivos_ajustada, formatos)
    elif entrada_diretorio and not entrada_arquivos:
        lista_arquivos = os.listdir(entrada_diretorio)
        return filtro_arquivos_selecionados(entrada_diretorio, lista_arquivos, formatos)


def filtro_arquivos_selecionados(diretorio, arquivos, formatos):
    lista_arquivos_filtrados = []
    for arquivo in arquivos:
        formato = os.path.splitext(arquivo)[1]
        rota = os.path.join(diretorio, arquivo)
        if os.path.isfile(rota) and (formato.lower() in formatos or len(formatos) == 0):
            lista_arquivos_filtrados.append(arquivo)
    return diretorio, lista_arquivos_filtrados

# +-----------------------------------------------+
# |                 ORGANIZADOR                   |
# +-----------------------------------------------+


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

# +-----------------------------------------------+
# |                 RENOMEADOR                    |
# +-----------------------------------------------+
