# 🇧🇷 Consulta Feriados

Sistema CLI modular em Python para consultar feriados nacionais via API pública.  
Permite busca por mês/ano, histórico persistente em JSON e interface validada no terminal.

---

## 🚀 Funcionalidades

- ✅ **Consultar feriados por mês** — validação de mês (1–12) e salvamento automático no histórico
- ✅ **Consultar todos os feriados do ano** — exibição formatada no terminal
- ✅ **Histórico de consultas** — persistência em JSON com timestamp
- ✅ **Limpar histórico** — verifica se existe antes de apagar
- ✅ **Encerramento do sistema** — saída controlada (graceful exit)

---

## 🛡️ Validações

- Entrada aceita apenas números inteiros
- Mês válido no intervalo 1–12
- Opções do menu limitadas a 1–5
- Tratamento de erros na comunicação com a API

---

## 🌐 API Utilizada

**[BrasilAPI](https://brasilapi.com.br/)**
GET https://brasilapi.com.br/api/feriados/v1/{ano}

text

> Inclui feriados móveis como Carnaval e Páscoa, calculados automaticamente.

---

## 📋 Como Executar

```bash
git clone https://github.com/Brunomdd/consulta-feriados.git
cd consulta-feriados
pip install requests
python main.py
```

---

## 📌 Menu do Sistema
1 - Consultar feriados no mês
2 - Consultar todos os feriados no ano
3 - Ver histórico de consultas
4 - Limpar histórico
5 - Sair do sistema

Escolha uma opção:

text

---

## 🗂️ Estrutura do Projeto
consulta-feriados/
├── main.py # Menu e lógica principal
├── api.py # Integração com a BrasilAPI (timeout + tratamento de erros)
├── uteis.py # JSON, validações e interface do terminal
├── feriados.json # Histórico persistente (criado automaticamente)
├── README.md
├── LICENSE
└── .gitignore

text

---

## 💡 Conceitos Aplicados

- Programação modular (separação de responsabilidades)
- Consumo de API REST com `requests`
- Manipulação e persistência de dados em JSON
- Tratamento de exceções por tipo (`ConnectionError`, `Timeout`, `HTTPError`, `JSONDecodeError`)
- Validação de entrada do usuário no terminal

---

## 📄 Licença

Este projeto está sob a licença [MIT](./LICENSE).
