# Roteiro para montar o dashboard no Power BI Desktop

Pré-requisito: ter o Power BI Desktop instalado (Windows) e os arquivos da pasta
esta pasta (de preferência já com `cotacoes_diarias.csv` gerado com dados reais via
`coleta_precos_yfinance.py`).

## 1. Importar os dados

1. Abra o Power BI Desktop → **Obter Dados** → **Banco de Dados** → **Banco de Dados
   SQLite** → selecione `dashboard_ibovespa.db`.
   - Alternativa sem SQLite: **Obter Dados** → **Texto/CSV** → importe os três arquivos
     `empresas.csv`, `indicadores_anuais.csv` e `cotacoes_diarias.csv` separadamente.
2. No **Poder Query** (Transformar Dados), confira os tipos de cada coluna:
   - `cotacoes_diarias`: `Data` → Data; `Abertura/Maximo/Minimo/Fechamento` → Decimal;
     `Volume` → Número inteiro.
   - `indicadores_anuais`: `pl, pvp, roe, roa, dividend_yield, margem_liquida,
     crescimento_receita` → Decimal; `ano` → Número inteiro.
3. Clique em **Fechar e Aplicar**.

## 2. Criar o relacionamento entre as tabelas

1. Vá em **Modelagem** → **Gerenciar Relacionamentos**.
2. Crie: `cotacoes_diarias[Ticker]` → `empresas[ticker]` (Muitos para Um).
3. Crie: `indicadores_anuais[ticker]` → `empresas[ticker]` (Muitos para Um).

## 3. Página 1 — Preço das ações (com drill-down)

1. Insira um **Gráfico de Linhas**.
2. Eixo X: arraste o campo `Data` de `cotacoes_diarias` — o Power BI cria
   automaticamente a hierarquia **Ano > Trimestre > Mês > Dia**.
3. Eixo Y: `Fechamento` (agregação: Média ou Soma, conforme preferir).
4. Legenda: `Ticker` (de `empresas` ou `cotacoes_diarias`).
5. Para habilitar o drill-down: clique com o botão direito no título do eixo → marque
   **"Ir para o próximo nível na hierarquia"**; ou clique nos ícones de seta que
   aparecem no canto superior esquerdo do visual ao selecioná-lo. Um duplo clique
   sobre um ponto do gráfico também desce um nível.
6. Adicione um **Segmentador de Dados (slicer)** com o campo `Ticker` para permitir
   isolar uma empresa por vez.

## 4. Página 2 — Indicadores fundamentalistas

1. **Gráfico de Colunas Agrupadas**: eixo X = `empresa`; valores = `roe` e
   `margem_liquida`; legenda = `ano` (ou crie um para cada ano com um slicer de ano).
2. **Matriz**: linhas = `empresa`; colunas = `ano`; valores = `pl`, `pvp`, `roe`,
   `roa`, `dividend_yield`, `margem_liquida`, `crescimento_receita`.
3. **Cartões de KPI**: crie 3 a 5 cartões (visual "Cartão") com o valor mais recente
   (2025) de P/L, Dividend Yield e ROE por empresa — filtre por `ano = 2025` na
   página ou use uma medida DAX (ver abaixo).

## 5. Medidas DAX sugeridas

```dax
Preço Médio no Período = AVERAGE('cotacoes_diarias'[Fechamento])

Variação % no Período =
DIVIDE(
    CALCULATE(MAX('cotacoes_diarias'[Fechamento]), LASTDATE('cotacoes_diarias'[Data])) -
    CALCULATE(MIN('cotacoes_diarias'[Fechamento]), FIRSTDATE('cotacoes_diarias'[Data])),
    CALCULATE(MIN('cotacoes_diarias'[Fechamento]), FIRSTDATE('cotacoes_diarias'[Data]))
)

ROE 2025 = CALCULATE(MAX('indicadores_anuais'[roe]), 'indicadores_anuais'[ano] = 2025)
```

## 6. Formatação final

- Aplique um tema de cores único em **Exibir → Temas**.
- Adicione títulos claros em cada visual (ex.: "Fechamento diário por empresa —
  arraste para expandir até o dia").
- Formatação condicional na matriz (Formatar visual → Formatação condicional) para
  destacar visualmente o maior/menor valor de cada indicador.
- Salve como `.pbix` e é esse arquivo que deve ser entregue junto ao artigo.
