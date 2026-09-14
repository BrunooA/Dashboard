# 📊 Dashboard Analítico de Ações (Ibovespa)

Projeto de análise financeira e fundamentalista que integra automação em Python para coleta de dados de mercado, armazenamento estruturado em SQLite e visualização interativa no Power BI.

---

## 🛠️ Tecnologias Utilizadas

* **Python 3.x:** Coleta automática de preços de fechamento e histórico via `yfinance`.
* **SQLite / pandas:** Armazenamento e estruturação do banco de dados relacional.
* **Power BI Desktop:** Modelagem de dados, medidas DAX e dashboards interativos.
* **Artigo Acadêmico:** Documentação completa no padrão ABNT / UniSales.

---

## 📁 Estrutura do Projeto

* `data/`: Banco de dados SQLite (`dashboard_ibovespa.db`) e tabelas CSV (`cotacoes_diarias`, `empresas`, `indicadores_anuais`).
* `scripts/`: Codificação Python para extração e carga de dados (`coleta_precos_yfinance.py`, `init_db.py`).
* `docs/`: Artigo técnico ABNT em Word/PDF e roteiros de apresentação.
* `AP1_dashboard_analistico.pbix`: Arquivo completo do Power BI com o dashboard de 4 páginas.

---

## 👥 Integrantes (Squad 6)

* Arthur Cândido Pimentel
* Bruno Araújo Silva
* Luis Felipe Siliprande Coelho
* Polyana Raquel Dias de Souza Rodrigues

**Orientador:** Prof. James Junior
