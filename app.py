import pandas as pd
import plotly.express as px
import streamlit as st

# Lendo os dados
car_data = pd.read_csv(r'vehicles.csv')

# Botão para criar histograma
hist_button = st.button('Criar histograma')

if hist_button:
    st.write('Criando um histograma para o conjunto de dados de anúncios de vendas de carros')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

# Botão para criar gráfico de dispersão
scatter_button = st.button('Criar gráfico de dispersão')

if scatter_button:
    st.write('Criando um gráfico de dispersão: Preço vs Quilometragem')
    fig = px.scatter(
        car_data,
        x="odometer",       # eixo X: quilometragem
        y="price",          # eixo Y: preço
        color="fuel",       # cor por tipo de combustível 
        title="Preço x Quilometragem por Tipo de Combustível"
    )
    st.plotly_chart(fig, use_container_width=True)
