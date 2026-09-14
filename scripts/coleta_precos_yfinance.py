"""
Script de coleta de precos historicos diarios via yfinance.

IMPORTANTE: este script deve ser executado na maquina do grupo (com acesso
normal a internet), pois o ambiente onde este projeto foi montado nao tem
acesso ao dominio da Yahoo Finance. Basta rodar:

    pip install yfinance pandas
    python coleta_precos_yfinance.py

Ele gera o arquivo cotacoes_diarias.csv com Data, Ticker, Abertura,
Maximo, Minimo, Fechamento, Fechamento_Ajustado e Volume para os ultimos
3 anos das 5 empresas do trabalho. Esse CSV e o que deve ser importado
no Power BI (ou carregado no banco SQLite via init_db.py) para montar o
grafico de precos com drill-down ano -> dia.
"""

from pathlib import Path

import yfinance as yf
import pandas as pd
from datetime import date
from dateutil.relativedelta import relativedelta

TICKERS = ["PETR4.SA", "VALE3.SA", "ITUB4.SA", "WEGE3.SA", "ABEV3.SA"]
BASE_DIR = Path(__file__).resolve().parent

fim = date.today()
inicio = fim - relativedelta(years=3)

frames = []
for ticker in TICKERS:
    df = yf.download(ticker, start=inicio, end=fim, interval="1d", auto_adjust=False)
    # Versões recentes do yfinance retornam MultiIndex mesmo para um único ticker.
    # Mantemos apenas o nível que contém Open/High/Low/Close/Volume.
    if isinstance(df.columns, pd.MultiIndex):
        df.columns = df.columns.get_level_values(0)
    df = df.reset_index()
    df["Ticker"] = ticker.replace(".SA", "")
    df = df.rename(columns={
        "Date": "Data",
        "Open": "Abertura",
        "High": "Maximo",
        "Low": "Minimo",
        "Close": "Fechamento",
        "Adj Close": "Fechamento_Ajustado",
        "Volume": "Volume",
    })
    frames.append(df[["Data", "Ticker", "Abertura", "Maximo", "Minimo",
                       "Fechamento", "Fechamento_Ajustado", "Volume"]])

resultado = pd.concat(frames, ignore_index=True)
arquivo_saida = BASE_DIR / "cotacoes_diarias.csv"
resultado.to_csv(arquivo_saida, index=False)
print(f"Arquivo gerado em {arquivo_saida} com {len(resultado)} linhas para {len(TICKERS)} tickers.")
