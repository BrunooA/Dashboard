# 📊 Dashboard Analítico de Ações (Ibovespa)

Projeto de análise financeira e fundamentalista que integra automação em Python para coleta de dados de mercado, armazenamento estruturado em SQLite e visualização interativa no Power BI.

---

## 🛠️ Tecnologias Utilizadas

* **Python 3.x**: Coleta automática de preços de fechamento e histórico via `yfinance`.
* **SQLite / pandas**: Armazenamento e estruturação do banco de dados relacional.
* **Power BI Desktop**: Modelagem de dados, medidas DAX e dashboards interativos.
* **DAX Studio**: Otimização e validação de consultas DAX.

---

## 📂 Estrutura do Projeto

* `coleta_precos_yfinance.py`: Script de extração das cotações em tempo real via Yahoo Finance.
* `init_db.py`: Script para povoamento e sincronização do banco de dados SQLite (`dashboard_ibovespa.db`).
* `empresas.csv`: Mapeamento das empresas selecionadas, setores e tipos de ações.
* `indicadores_anuais.csv`: Indicadores fundamentalistas consolidados (P/L, P/VP, ROE, ROA, Dividend Yield, etc.).
* `cotacoes_diarias.csv`: Série histórica de preços de abertura, fechamento, máximas e mínimas.

---

## ⚡ Como Executar o Projeto

1. **Instalar dependências**:
   ```bash
   pip install -r requirements.txt
