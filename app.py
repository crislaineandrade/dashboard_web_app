import pandas as pd
import streamlit as st
import plotly.express as px

st.header('Dashboard') #titulo
df_vehicles = pd.read_csv('vehicles.csv') #lendo arquivo


hist_checkbox = st.checkbox('Criar Histograma') #criar botao do grafico de hist

if hist_checkbox:
    st.write('Criando um histograma para o conjunto de dados de anúncios de vendas de carros')
    #criar o grafico 
    fig = px.histogram(df_vehicles, x='odometer')
    #mostrar o grafico
    st.plotly_chart(fig, use_container_width=True)


scatter_checkbox = st.checkbox('Criar Gráfico de Dispersão') #criar botao do grafico de dispersao

if scatter_checkbox:
    st.write('Criando um gráfico de dispersão para o conjunto de dados de anúncios de vendas de carros')

    fig = px.scatter(df_vehicles, x='odometer', y='price')

    st.plotly_chart(fig, use_container_width=True)

print(df_vehicles.info())


# LÓGICA PARA USAR BOTÃO AO INVÉA E CHECKBOX
# hist_button = st.button('Criar histograma')
# scatter_button = st.button('Criar gráfico de dispersão')


# if hist_button: #botao para criar o histograma
#     st.write('Criando um histograma para o conjunto de dados de anúncios de vendas de carros')

#     #criar o histrograma
#     fig = px.histogram(df_vehicles, x='odometer')

#     #exibir o gráfico no plotly
#     st.plotly_chart(fig, use_container_width=True)

# if scatter_button:
#     st.write('Criando um gráfico de dispersão para o conjunto de dados de anúncios de vendas de carros')

#     fig = px.scatter(df_vehicles, x='odometer', y='price)

#     st.plotly_chart(fig, use_container_width=True)

