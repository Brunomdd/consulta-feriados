 Consulta Feriados 🇧🇷

Sistema CLI modular em Python para consultar feriados nacionais via BrasilAPI.
Busca por mês/ano, histórico JSON persistente, interface validada no terminal.
🚀 Funcionalidades (Exatas do Código)

✅ Opção 1: Feriados de mês específico (valida 1-12) + salva histórico
✅ Opção 2: Todos feriados do ano formatados centralizados
✅ Opção 3: Histórico completo com timestamp da consulta
✅ Opção 4: Limpar histórico (confirma se existe)
✅ Opção 5: Sair graceful
🛡️ Validações: Input inteiro, meses 1-12, opções 1-5, erros API
Endpoint oficial: GET https://brasilapi.com.br/api/feriados/v1/{ano} (Carnaval, Páscoa calculados)
📋 Como Executar

git clone https://github.com/Brunomdd/consulta-feriados.git
cd consulta-feriados
pip install requests # Única dependência
python main.py
Menu exato:

text
--------------------------------
1 - Consultar feriados no mês
2 - Consultar todos os feriados no ano
3 - Ver histórico de consultas
4 - Limpar histórico
5 - Sair do sistema
--------------------------------
Escolha uma opção:
🗂️ Estrutura (100% Modular)
text
consulta-feriados/
├── main.py # Menu + lógica (buscar_feriado, feriados_ano, listar_historico)
├── api.py # BrasilAPI (api_feriado com timeout=5 + 5x try/except)
├── uteis.py # JSON (carregar/salvar), UI (linha, leiaint loop while)
├── feriados.json # Auto-criado (UTF-8, indent=4)
├── README.md
├── LICENSE
└── .gitignore
