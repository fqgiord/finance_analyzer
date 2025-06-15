# 📊 Finance Analyzer

Projeto de análise financeira simples, com coleta de dados via Web (Yahoo Finance), processamento e visualização interativa usando **Streamlit**.

---

## 🚀 Descrição

Este projeto permite buscar dados históricos de ativos financeiros (ações, ETFs etc), aplicar algumas transformações básicas e exibir gráficos interativos com médias móveis, utilizando:

- Coleta de dados com `yfinance`
- Processamento com `pandas`
- Visualização interativa com `Streamlit`
- Estrutura modularizada em Python

---

## 🏗 Estrutura de diretórios

```bash
finance-analyzer/
│
├── app/                # Aplicação Streamlit
│   └── app.py
│
├── data/
│   ├── raw/            # Dados brutos baixados
│   └── processed/      # Dados processados
│
├── notebooks/          # Notebooks exploratórios
│
├── src/                # Código fonte (fetch, processamento, visualização)
│
├── tests/              # Testes unitários
│
├── .gitignore
├── requirements.txt
└── README.md
