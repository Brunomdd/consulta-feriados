import requests

def api_feriado(ano_feriado):
    """
    Consulta a API de feriados do Brasil para um determinado ano.

    Parâmetros:
        ano_feriado (int): Ano que será consultado na API.

    Retorno:
        list | None: Retorna uma lista de feriados em formato JSON
        caso a requisição seja bem-sucedida. Caso ocorra algum erro,
        a função exibe uma mensagem e retorna None.

    Possíveis erros tratados:
        - Falha de conexão com a API
        - Tempo de resposta excedido
        - Erro no formato do JSON retornado
        - Erro HTTP na requisição
    """
    try:
        resposta = requests.get(
            f"https://brasilapi.com.br/api/feriados/v1/{ano_feriado}",
            timeout=5
        )
        resposta.raise_for_status()
        return resposta.json()

    except requests.exceptions.ConnectionError:
        print('A API não conseguiu se conectar!')

    except requests.exceptions.Timeout:
        print('Tempo de resposta expirou!')

    except requests.JSONDecodeError:
        print('Erro no formato de dados!')

    except requests.exceptions.HTTPError as error:
        print(f'Erro {error}')