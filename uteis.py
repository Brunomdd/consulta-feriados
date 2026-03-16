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


def leiaint(msg):
    """
    Lê um valor inteiro digitado pelo usuário.

    Parâmetros:
        msg (str): Mensagem exibida para solicitar o número.

    Retorno:
        int: Número inteiro digitado pelo usuário.

    Caso o usuário digite algo que não seja número,
    o programa continuará pedindo até receber um valor válido.
    """
    while True:
        try:
            valor = int(input(msg))
            return valor
        except ValueError:
            print('Erro, só aceitamos valores inteiros!')


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