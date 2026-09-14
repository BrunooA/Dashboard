"""
Gera cotacoes_diarias.csv com uma serie SINTETICA (random walk calibrado
pelos precos de referencia de fechamento de 2023/2024/2025 do arquivo
indicadores_anuais.csv). Serve so para testar a estrutura do banco e do
dashboard antes de o grupo rodar coleta_precos_yfinance.py com dados reais.

NAO usar estes numeros no artigo final -- sao apenas placeholder.
"""

from pathlib import Path

import numpy as np
import pandas as pd

np.random.seed(42)

anchors = {
    "PETR4": {2023: 35.85, 2024: 38.10, 2025: 41.98},
    "VALE3": {2023: 68.40, 2024: 61.20, 2025: 70.96},
    "ITUB4": {2023: 29.80, 2024: 33.40, 2025: 38.70},
    "WEGE3": {2023: 38.90, 2024: 45.10, 2025: 48.90},
    "ABEV3": {2023: 13.20, 2024: 12.60, 2025: 13.90},
}

start = pd.Timestamp("2023-08-25")
end = pd.Timestamp("2026-08-24")
dias_uteis = pd.bdate_range(start, end)

rows = []
for ticker, precos_ano in anchors.items():
    anos = sorted(precos_ano.keys())
    n = len(dias_uteis)
    # preco alvo por dia via interpolacao linear entre os 3 pontos-ancora anuais
    marcos_data = [pd.Timestamp(f"{a}-12-30") for a in anos]
    marcos_valor = [precos_ano[a] for a in anos]
    marcos_data = [start] + marcos_data + [end]
    marcos_valor = [precos_ano[anos[0]] * 0.9] + marcos_valor + [precos_ano[anos[-1]]]
    alvo = np.interp(dias_uteis.astype(np.int64), pd.DatetimeIndex(marcos_data).astype(np.int64), marcos_valor)

    ruido = np.random.normal(0, 1, n).cumsum()
    ruido = ruido / (np.std(ruido) + 1e-9) * (np.mean(alvo) * 0.03)
    fechamento = np.maximum(alvo + ruido, 0.5)

    for i, d in enumerate(dias_uteis):
        f = fechamento[i]
        abertura = f * (1 + np.random.normal(0, 0.004))
        maximo = max(abertura, f) * (1 + abs(np.random.normal(0, 0.006)))
        minimo = min(abertura, f) * (1 - abs(np.random.normal(0, 0.006)))
        volume = int(np.random.uniform(8_000_000, 40_000_000))
        rows.append([d.date().isoformat(), ticker, round(abertura, 2), round(maximo, 2),
                     round(minimo, 2), round(f, 2), round(f, 2), volume])

df = pd.DataFrame(rows, columns=["Data", "Ticker", "Abertura", "Maximo", "Minimo",
                                  "Fechamento", "Fechamento_Ajustado", "Volume"])
arquivo_saida = Path(__file__).resolve().parent / "cotacoes_diarias.csv"
df.to_csv(arquivo_saida, index=False)
print(f"Gerado {arquivo_saida} com {len(df)} linhas (PLACEHOLDER sintetico).")
