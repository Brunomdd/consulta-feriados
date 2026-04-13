🇧🇷 Consulta Feriados
Sistema CLI modular em Python para consultar feriados nacionais brasileiros via BrasilAPI, com histórico persistente em JSON e interface validada no terminal.

📌 Sobre o Projeto
Este projeto foi desenvolvido como parte do meu aprendizado em Python, com foco em:

Integração com APIs REST externas

Tratamento de erros HTTP e de rede

Persistência de dados com arquivos JSON

Arquitetura modular (separação de responsabilidades)

Validação de entrada do usuário no terminal

A ideia é simples: o usuário informa um ano e mês, e o sistema consulta a BrasilAPI para retornar os feriados nacionais — incluindo datas móveis como Carnaval e Páscoa, que são calculadas automaticamente pela API.

🚀 Funcionalidades
Opção	Descrição
1	Consultar feriados de um mês específico + salva no histórico
2	Listar todos os feriados de um ano completo
3	Ver histórico de consultas realizadas com timestamp
4	Limpar o histórico salvo (verifica se existe antes)
5	Sair do sistema
🛡️ Validações implementadas
Entrada de opções aceita somente inteiros (loop while True + try/except ValueError)

Mês validado no intervalo 1 a 12

Erros de API tratados individualmente: ConnectionError, Timeout, JSONDecodeError, HTTPError

Histórico verifica existência antes de limpar ou listar

🗂️ Arquitetura Modular
text
consulta-feriados/
├── main.py          ← Ponto de entrada: menu, lógica de negócio
├── api.py           ← Comunicação com a BrasilAPI
├── uteis.py         ← Utilitários: JSON, UI, input validado
├── feriados.json    ← Histórico persistente (auto-criado, UTF-8, indent=4)
├── README.md
├── LICENSE
└── .gitignore
Por que modular?
Cada arquivo tem uma responsabilidade única:

api.py só sabe falar com a API — se a URL mudar, só este arquivo muda

uteis.py só sabe ler/salvar JSON e interagir
