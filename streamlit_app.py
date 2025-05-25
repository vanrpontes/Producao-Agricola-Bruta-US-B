# Produção Agrícola Bruta (US$ B)
# Autor: Van Pontes
# Site: https://rochapontesbi.com.br
# Repositório: https://github.com/vanrpontes/Producao-Agricola-Bruta-US-B

import pandas as pd
import streamlit as st
import altair as alt

# Carregar dataset
df = pd.read_csv(r"data/agri.csv")

# Verificar se a coluna 'Region' existe antes de setar índice
if 'Region' in df.columns:
    df = df.set_index("Region")
else:
    st.error("A coluna 'Region' não foi encontrada no CSV.")
    st.stop()  # Para o app se não tiver a coluna

# Título do app
st.title("Produção Agrícola Bruta (US$ B)")

# Mostrar tabela com índice já definido
st.subheader("Produção Agrícola Bruta (US$ B) - Tabela")
st.dataframe(df, height=220)

# Multiselect de países
countries = st.multiselect(
    "Escolha os países",
    list(df.index),
    ["Brazil", "China", "United States of America"]
)

if not countries:
    st.error("Selecione pelo menos um país para visualizar os dados.")
else:
    # Filtrar e converter para bilhões
    data = df.loc[countries]
    data /= 1_000_000.0

    st.subheader("Produção Agrícola Bruta (US$ B)")
    st.dataframe(data.sort_index(), height=180)

    # Preparar dados para gráfico
    data = data.T.reset_index()  # resetar anos para coluna
    data = pd.melt(data, id_vars=["index"]).rename(
        columns={"index": "Ano", "value": "Produção Agrícola Bruta (US$ B)", "variable": "Region"}
    )

    # Criar gráfico de área
    chart = (
        alt.Chart(data)
        .mark_area(opacity=0.3, interpolate='monotone')
        .encode(
            x=alt.X("Ano:T", title="Ano"),
            y=alt.Y("Produção Agrícola Bruta (US$ B):Q", stack=None, title="Produção (US$ B)"),
            color=alt.Color("Region:N", legend=alt.Legend(title="País")),
            tooltip=["Ano:T", "Region:N", "Produção Agrícola Bruta (US$ B):Q"]
        )
    )

    st.altair_chart(chart, use_container_width=True)
