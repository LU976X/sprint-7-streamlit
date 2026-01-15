import streamlit as st
import pandas as pd
import plotly.express as px
st.write("¡Streamlit ya funciona!")
st.title("Análisis de autos usados 🚗")

df = pd.read_csv("vehicles_us.csv")

st.subheader("Vista previa del dataset")
st.dataframe(df.head())

st.subheader("Distribución de precios")
fig1 = px.histogram(df, x="price", nbins=50, title="Distribución de precios")
st.plotly_chart(fig1, use_container_width=True)

st.subheader("Precio por tipo de vehículo")
fig2 = px.box(df, x="type", y="price", title="Precio por tipo de vehículo")
st.plotly_chart(fig2, use_container_width=True)

st.subheader("Precio vs Kilometraje")
fig3 = px.scatter(df, x="odometer", y="price", opacity=0.4, title="Precio vs Kilometraje")
st.plotly_chart(fig3, use_container_width=True)