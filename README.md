# Consulta Feriados 🇧🇷

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![API](https://img.shields.io/badge/BrasilAPI-100%25-green.svg)](https://brasilapi.com.br)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

**Sistema CLI em Python para consultar feriados nacionais brasileiros via BrasilAPI.**  
Permite buscar feriados por mês/ano, listar todos do ano, visualizar e limpar histórico de consultas. Interface simples e intuitiva no terminal! [web:1][web:10]

## 🚀 Funcionalidades
- ✅ Consultar feriados de um **mês específico** (ex: janeiro/2026)
- ✅ Listar **todos os feriados nacionais de um ano**
- ✅ **Histórico de consultas** salvo localmente em JSON
- ✅ **Limpar histórico** com um clique
- ✅ Tratamento de erros e interface amigável no terminal
- 📱 Fácil de usar e expandir (sem dependências extras além de `requests`)

**Endpoint usado:** `https://brasilapi.com.br/api/feriados/v1/{ano}` – Calcula feriados móveis (Carnaval, Páscoa) + fixos. [web:15][web:2]

## 📋 Como Executar
```bash
git clone https://github.com/Brunomdd/consulta-feriados.git
cd consulta-feriados
python main.py

Siga o menu interativo:

text
1 - Consultar feriados por mês
2 - Listar todos feriados do ano
3 - Ver histórico
4 - Limpar histórico
0 - Sair

🗂️ Estrutura do Projeto
text
consulta-feriados/
├── main.py          # Menu principal e lógica central
├── api.py           # Integração com BrasilAPI (GET requests)
├── uteis.py         # Funções auxiliares (JSON load/save, input validado)
├── feriados.json    # Histórico local de consultas
├── README.md        # 📖 Você está aqui!
├── LICENSE          # Licença MIT
└── .gitignore       # Ignora __pycache__, .env, etc.
🔧 Tecnologias
Python 3.x – Linguagem principal

BrasilAPI – API pública gratuita para dados BR [web:1]

JSON – Armazenamento leve de histórico

Requests – Para chamadas HTTP seguras

Click/Rich (opcional futuro) – Para UI mais bonita

📊 Exemplo de Uso
text
Digite o ano (ex: 2026): 2026
Digite o mês (1-12): 1

Feriados em Janeiro/2026:
-  01/01 - Ano Novo
Histórico salvo automaticamente em feriados.json!

🤝 Contribuições
Fork o repo

Crie uma branch (git checkout -b feature/nova-func)

Commit suas mudanças (git commit -m 'Adiciona suporte a feriados estaduais')

Push para a branch (git push origin feature/nova-func)

Abra um Pull Request!
