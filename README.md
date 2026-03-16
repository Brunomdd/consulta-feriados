Consulta Feriados 🇧🇷

Sistema em Python para consultar feriados nacionais usando a BrasilAPI. Permite consultar feriados por mês, listar todos os feriados do ano, visualizar histórico de consultas e limpar o histórico.

Funcionalidades

Consultar feriados de um mês específico

Listar todos os feriados de um ano

Histórico das consultas feitas

Limpar o histórico

Interface simples no terminal

Tecnologias

Python 3.x

BrasilAPI (API pública para dados do Brasil)

JSON para armazenar histórico

Como executar
git clone https://github.com/Brunomdd/consulta-feriados.git
cd consulta-feriados
python main.py
Estrutura do projeto
main.py         # Código principal e menu
api.py          # Comunicação com a API BrasilAPI
uteis.py        # Funções auxiliares como carregar/salvar JSON e leitura de dados
feriados.json   # Histórico de consultas armazenado localmente
README.md       # Documentação do projeto
LICENSE         # Licença MIT
.gitignore      # Arquivos e pastas ignoradas pelo Git
