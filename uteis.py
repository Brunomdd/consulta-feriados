import json
from json import JSONDecodeError

def linha(l=32):
    """
    Retorna uma linha de separação formada por hífens.

    Parâmetros:
        l (int): Tamanho da linha.

    Retorno:
        str: String contendo a linha de separação.
    """
    return '-' * l

def executar(funcao,valor):
    while True:
        try:
            valor = input(valor)
            if not valor:
                print('Erro! Não pode ficar vazio!')
            return funcao(valor)
        except ValueError:
            print("Erro! digite um número inteiro ")
            


def leiaint(valor):
    return executar(int,valor)

def carregar():
    """
    Carrega o histórico de feriados armazenado no arquivo JSON.

    Retorno:
        list: Lista de feriados armazenados no arquivo.

    Caso o arquivo não exista ou esteja vazio/corrompido,
    retorna uma lista vazia.
    """
    lista = []
    try:
        with open('feriados.json','r',encoding='utf-8') as arq:
            lista = json.load(arq)
    except (FileNotFoundError, JSONDecodeError):
        return []
    return lista


def salvar(lista):
    """
    Salva a lista de feriados no arquivo JSON.

    Parâmetros:
        lista (list): Lista contendo os feriados que serão armazenados.

    O arquivo é salvo com indentação para facilitar leitura.
    """
    with open('feriados.json','w',encoding='utf-8') as arq:
        json.dump(lista, arq, ensure_ascii=False, indent=4)