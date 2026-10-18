import streamlit as st
import pandas as pd
import plotly.graph_objects as go

car_data = pd.read_csv('vehicles_us.csv')

st.header('Condiciones de los vehículos en el mercado de EE. UU.')

hist_button = st.button('Construir un histograma')

if hist_button:
    st.write('Creación de un histograma para un conjunto de datos de anuncios de ventas de coches')
    fig = go.Figure(data=[go.Histogram(x=car_data['odometer'])])
    st.plotly_chart(fig, use_container_width=True)

scat_button = st.button('Construir un gráfico de dispersión')

if scat_button:
    st.write('Creación de un gráfico de dispersión para un conjunto de datos de anuncios de ventas de coches')
    fig = go.Figure(data=[go.Scatter(x=car_data['odometer'], y=car_data['price'], mode='markers')])
    st.plotly_chart(fig, use_container_width=True)

build_histogram = st.checkbox('Construir un histograma')
if build_histogram:
    st.write('Creación de un histograma para un conjunto de datos de anuncios de ventas de coches')
    fig = go.Figure(data=[go.Histogram(x=car_data['odometer'])])
    st.plotly_chart(fig, use_container_width=True)

build_scatter = st.checkbox('Construir un gráfico de dispersión')
if build_scatter:
    st.write('Creación de un gráfico de dispersión para un conjunto de datos de anuncios de ventas de coches')
    fig = go.Figure(data=[go.Scatter(x=car_data['odometer'], y=car_data['price'], mode='markers')])
    st.plotly_chart(fig, use_container_width=True)