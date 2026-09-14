# Projeto: Dashboard Analítico Ibovespa — Base de Dados

## Empresas selecionadas
PETR4 (Petrobras), VALE3 (Vale), ITUB4 (Itaú Unibanco), WEGE3 (WEG), ABEV3 (Ambev) —
setores diferentes de propósito (petróleo/gás, mineração, bancos, bens de capital, bebidas),
o que enriquece a comparação fundamentalista.

## Arquivos
- `empresas.csv` — cadastro das 5 empresas (ticker, setor, tipo de ação)
- `indicadores_anuais.csv` — os 7 indicadores fundamentalistas (P/L, P/VP, ROE, ROA,
  Dividend Yield, Margem Líquida, Crescimento de Receita) para 2023, 2024 e 2025, consolidados
  a partir de StatusInvest, Fundamentus e Investidor10 (referência: agosto/2026).
- `cotacoes_diarias.csv` — série diária de preços (Abertura, Máximo, Mínimo, Fechamento,
  Volume) para o gráfico de drill-down. **Está com dados SINTÉTICOS (placeholder)** — troque
  pelo resultado real do script `coleta_precos_yfinance.py` antes de finalizar o trabalho.
- `dashboard_ibovespa.db` — banco SQLite com as 3 tabelas acima, pronto para conectar
  no Power BI (Obter Dados → Banco de Dados → SQLite).
- `init_db.py` — recria o banco a partir dos CSVs.
- `coleta_precos_yfinance.py` — script real de coleta de preços via `yfinance` (rodar
  na máquina do grupo, com internet livre).
- `gerar_cotacoes_placeholder.py` — gerou a série sintética atual, só para teste.

## ⚠️ Ação obrigatória antes de entregar
1. Rodar `pip install -r requirements.txt` e depois
   `python coleta_precos_yfinance.py` para substituir `cotacoes_diarias.csv` por
   dados reais.
2. Rodar `python init_db.py` de novo para atualizar o banco com os preços reais.
3. Conferir/ajustar os valores de `indicadores_anuais.csv` direto nas fontes (StatusInvest,
   Fundamentus, RI de cada empresa) — os valores aqui são uma consolidação de referência,
   mas cada grupo deve validar os números que vai defender no artigo.

## Estrutura das tabelas (para o artigo, seção de Metodologia)
**empresas**(ticker PK, empresa, setor, segmento_b3, tipo_acao)
**indicadores_anuais**(ticker FK, empresa, setor, ano, preco_fechamento_ref, pl, pvp, roe, roa,
dividend_yield, margem_liquida, crescimento_receita)
**cotacoes_diarias**(Data, Ticker FK, Abertura, Maximo, Minimo, Fechamento, Fechamento_Ajustado,
Volume, Ano, Mes, Trimestre)
