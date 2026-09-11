"""
Cria o banco de dados SQLite (dashboard_ibovespa.db) a partir dos CSVs
na mesma pasta deste script. Rode assim:

    python init_db.py

Tabelas criadas:
  - empresas            (1 linha por empresa)
  - indicadores_anuais  (1 linha por empresa/ano com os 7 indicadores)
  - cotacoes_diarias    (1 linha por empresa/dia com OHLC + volume)

Esse .db pode ser aberto direto no Power BI (Obter Dados > Banco de
Dados SQLite) ou os CSVs desta pasta podem ser importados diretamente.
"""

import sqlite3
from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "dashboard_ibovespa.db"

empresas = pd.read_csv(BASE_DIR / "empresas.csv")
indicadores = pd.read_csv(BASE_DIR / "indicadores_anuais.csv")
cotacoes = pd.read_csv(BASE_DIR / "cotacoes_diarias.csv", parse_dates=["Data"])

# colunas auxiliares para o drill-down Ano -> Mes -> Dia no Power BI
cotacoes["Ano"] = cotacoes["Data"].dt.year
cotacoes["Mes"] = cotacoes["Data"].dt.month
cotacoes["Trimestre"] = cotacoes["Data"].dt.quarter

conn = sqlite3.connect(DB_PATH)

empresas.to_sql("empresas", conn, if_exists="replace", index=False)
indicadores.to_sql("indicadores_anuais", conn, if_exists="replace", index=False)
cotacoes.to_sql("cotacoes_diarias", conn, if_exists="replace", index=False)

conn.execute("CREATE INDEX IF NOT EXISTS idx_cot_ticker_data ON cotacoes_diarias(Ticker, Data)")
conn.execute("CREATE INDEX IF NOT EXISTS idx_ind_ticker_ano ON indicadores_anuais(ticker, ano)")
conn.commit()

print("Banco criado em", DB_PATH)
for tabela in ["empresas", "indicadores_anuais", "cotacoes_diarias"]:
    n = conn.execute(f"SELECT COUNT(*) FROM {tabela}").fetchone()[0]
    print(f"  {tabela}: {n} linhas")

conn.close()
