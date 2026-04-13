🇧🇷 Consulta Feriados

Sistema CLI modular em Python para consultar feriados nacionais via API pública.
Permite busca por mês/ano, histórico persistente em JSON e interface validada no terminal.

🚀 Funcionalidades
✅ Consultar feriados por mês
Validação de mês (1–12)
Salva automaticamente no histórico
✅ Consultar todos os feriados do ano
Exibição formatada
✅ Histórico de consultas
Persistência em JSON
Exibição com timestamp
✅ Limpar histórico
Verifica se existe antes de apagar
✅ Encerramento do sistema
Saída controlada (graceful)
🛡️ Validações
Entrada apenas de números inteiros
Mês válido (1–12)
Opções do menu (1–5)
Tratamento de erro na API
🌐 API Utilizada
BrasilAPI
Endpoint:
GET https://brasilapi.com.br/api/feriados/v1/{ano}

Inclui feriados móveis como Carnaval e Páscoa.

📋 Como Executar
git clone https://github.com/Brunomdd/consulta-feriados.git
cd consulta-feriados
pip install requests
python main.py
📌 Menu do Sistema
--------------------------------
1 - Consultar feriados no mês
2 - Consultar todos os feriados no ano
3 - Ver histórico de consultas
4 - Limpar histórico
5 - Sair do sistema
--------------------------------
Escolha uma opção:
🗂️ Estrutura do Projeto
consulta-feriados/
├── main.py        # Menu e lógica principal
├── api.py         # Integração com API (timeout + retry)
├── uteis.py       # JSON, validações e interface
├── feriados.json  # Histórico persistente (auto-criado)
├── README.md
├── LICENSE
└── .gitignore
💡 Conceitos Aplicados
Programação modular
Consumo de API REST
Manipulação de JSON
Tratamento de exceções
Validação de entrada
Separação de responsabilidades
📄 Licença

Este projeto está sob a licença MIT.
