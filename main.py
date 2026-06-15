from api import api_feriado
from uteis import carregar, salvar, linha, leiaint
from datetime import datetime

def buscar_feriado_mes(ano, mes):
    """
    Busca feriados de um determinado mês e ano usando a API.

    Parâmetros:
        ano (int): Ano que será consultado.
        mes (int): Mês que será filtrado.

    Retorno:
        list: Lista de feriados encontrados no mês informado.

    Também salva os feriados encontrados no histórico (arquivo JSON).
    """
    feriados = api_feriado(ano)
    
    if not feriados:
        return []

    return [f for f in feriados if int(f['date'][5:7]) == mes]

def salvar_consulta_historico(feriados):
    historico = carregar()
    for feriado in feriados:
        item = {'nome':[feriado['name']],
                'data':feriado['date'],
                'consultado_em':datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
                }
        historico.append(item)
    salvar(historico)

def listar_feriados(ano):
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

def mostrar_historico():
    historico = carregar()
    if not historico:
        print('')
        return
    for item in historico:
        print(linha())
        print(f"Data: {item['date']}")
        print(f"Feriado: {item['name']}")
        print(f"Consultado em: {item['consultado_em']}")


def consultar_feriado_por_mes():
    ano = leiaint('digite o ano: ')
    mes = leiaint('digite o mes: ')

    if mes <1 or mes > 12:
            print('erro. o mes precisa estar no intervalo entre 1 e 12!')
            return
    feriados = buscar_feriado_mes(ano, mes)
    print(f"Temos {len(feriados)} feriados na lista")

    if not  feriados:
        print('Não tem feriado esse mes!')
        return
    salvar_consulta_historico(feriados)
    for feriado in feriados:
        print(f"data:feriado['date'] nome: {feriado['name']} ")

def listar_feriados_do_ano(ano):
    feriados = api_feriado(ano)
    if not feriados:
        print("Não encontramos esse ano na nossa base de dados.")
        return

    for feriado in feriados:
        print(linha())
        print(f"Nome: {feriado['name']}")
        print(f"Data: {feriado['date']}")

def consultar_ano_feriado():
    ano = leiaint('digite o ano: ')
    listar_feriados_do_ano(ano)
    

    
def mostrar_historico():
    historico = carregar()
    if not historico:
        print('')
        return
    for item in historico:
        print(linha())
        print(f"Data: {item['date']}")
        print(f"Feriado: {item['name']}")
        print(f"Consultado em: {item['consultado_em']}")

    

def limpar_historico():
    historico = carregar()
    if not historico:
        print('Não ná nada para limpar no historico!')
    else:
        salvar([])
        print('Historio limpo com sucesso!')


def menu(opc):
    for valor, item in enumerate(opc,start=1):
        print(f'{valor} - {item}  ')

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
        menu(['Consultar feriados no mês',
             'Consultar todos os feriados no ano',
             'Ver histórico de consultas',
             'Limpar historico',
             'Sair do sistema',])
        print(linha())

        opcao = leiaint('escolha uma opção: ')
        if opcao == 1:
           consultar_feriado_por_mes()
        
        elif opcao == 2:
            consultar_ano_feriado()
            
           

        elif opcao == 3:
            mostrar_historico()

        elif opcao == 4:
            limpar_historico()
            
        elif opcao == 5:
            print('Saindo do sistema . . .')
            break

        else:
            print('Erro, só aceitamos valores no intervalo entre 1 e 5.')


main()