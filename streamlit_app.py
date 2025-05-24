#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Produção Agrícola Bruta (US$ B)

#Este app foi desenvolvido com Python, Pandas e Streamlit para visualizar dados sobre a Produção Agrícola Bruta de diversos países ao longo dos anos.

#Os dados foram obtidos da United Nations Data e estão disponíveis neste repositório.

#Autor: Van Pontes
#Site: https://rochapontesbi.com.br
#Repositório: https://github.com/vanrpontes/Producao-Agricola-Bruta-US-B


#Importando bibliotecas Pandas e Streamlit
import pandas as pd
import streamlit as st

#Acessando o Dataset
df = pd.read_csv (r"C:\Users\vrpon\Documents\GitHub\Producao-Agricola-Bruta-US-B\data\agri.csv")

#Título do App
st.title("📊 Produção Agrícola Bruta (US$ B)")

#Mostrar resumo do dataset
st.subheader("Visualização Inicial do Dataset")
st.dataframe(df.head())


# In[ ]:




