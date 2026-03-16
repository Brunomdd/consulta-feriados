from api import api_feriado
from uteis import carregar, salvar, linha, leiaint
from datetime import datetime

def buscar_feriado(ano, mes):
    """
    Busca feriados de um determinado mês e ano usando a API.

    Parâmetros:
        ano (int): Ano que será consultado.
        mes (int): Mês que será filtrado.

    Retorno:
        list: Lista de feriados encontrados no mês informado.

    Também salva os feriados encontrados no histórico (arquivo JSON).
    """
    lista = carregar()
    feriados = api_feriado(ano)
    historico = []

    if not feriados:
        return []

    for f in feriados:
        mes_usuario = int(f['date'][5:7])
        if mes == mes_usuario:
            lista.append(f)
            historico.append(f)

    salvar(lista)
    return historico


def feriados_ano(ano):
    """
    Lista todos os feriados de um determinado ano.

    Parâmetros:
        ano (int): Ano que será consultado.

    Exibe no terminal o nome e a data de cada feriado retornado pela API.
    """
    feriados = api_feriado(ano)

    if not feriados:
        print('Não encontramos esse ano na nossa base dados')
        return

    for f in feriados:
        print(linha())
        print(f"nome: {f['name']}".center(32))
        print(f"data: {f['date']}".center(32))
        print()


def listar_historico(historico):
    """
    Mostra o histórico de consultas realizadas pelo usuário.

    Parâmetros:
        historico (list): Lista de feriados armazenados no arquivo JSON.

    Também exibe a hora atual da consulta.
    """
    hora_atual = datetime.now().strftime("%H:%M:%S")

    print("Lista de consultas")
    for item in historico:
        print(linha())
        print(f"data: {item['date']}")
        print(f"feriado: {item['name']}")

    print(f'hora da consulta: {hora_atual}')


def main():
    """
    Função principal do sistema.

    Responsável por:
    - Exibir o menu
    - Receber a escolha do usuário
    - Chamar as funções correspondentes

    O sistema permite:
    1. Consultar feriados de um mês
    2. Listar todos os feriados do ano
    3. Ver histórico de consultas
    4. Limpar histórico
    5. Sair do sistema
    """
    while True:
        print(linha())
        print('1 - Consultar feriados no mes')
        print('2 - Consultar todos os feriados no ano')
        print('3 - Ver historico de consultas')
        print('4 - Limpar historico')
        print('5 - Sair do sistema')
        print(linha())

        opcao = leiaint('escolha uma opção: ')

        if opcao == 1:
            ano = leiaint('digite o ano: ')
            mes = leiaint('digite o mes: ')

            if mes < 1 or mes > 12:
                print('erro. o mes precisa estar no intervalo entre 1 e 12!')
                continue

            resposta = buscar_feriado(ano, mes)

            print(f"Temos {len(resposta)} feriados na lista")

            if resposta:
                for feriados in resposta:
                    print(f"data: {feriados['date']} - nome: {feriados['name']}")
            else:
                print('Não tem feriado nesse mes!')

        elif opcao == 2:
            ano = leiaint('digite o ano: ')
            feriados_ano(ano)

        elif opcao == 3:
            historico = carregar()

            if not historico:
                print('Não há feriados para consultar no historico no momento!')
            else:
                listar_historico(historico)

        elif opcao == 4:
            limpar = carregar()

            if limpar:
                salvar([])
                print('Historico limpo com sucesso!!')
            else:
                print('Não há nada para limpar no historico!')

        elif opcao == 5:
            print('Saindo do sistema . . .')
            break

        else:
            print('Erro, só aceitamos valores no intervalo entre 1 e 3.')


main()