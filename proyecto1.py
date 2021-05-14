import streamlit as st
from PIL import Image #PIL es una librería de imagen
import pandas as pd #pandas sirve para leer base de datos
import altair as alt 
import plotly.express as px
import math 
st.title("Proyecto 1")
st.sidebar.title("parámetros")
st.header("Inicio")
st.write("Esta es mi primera aplicación")
opciones=st.selectbox("Seleccione una opción",("opción 1","opción 2"))
if opciones == "opción 1":
	st.write("Usted selecciono la opción 1")
if opciones == "opción 2":
	st.write("Usted selecciono la opción 2")
st.radio("Seleccione una opción",("opción 1","opción 2"))
st.multiselect("Seleccione una opción",("opción 1","opción 2"))
st.slider("Seleccione un valor",1.0,60.0,30.0,step=1.1) #python puede leer o bien decimales o bien enteros
st.number_input("Ingrese un valor")
imagen1 = Image.open("NIKE.jpg")
st.image(imagen1) #El lenguaje HTML se puede utilizar mezclado con python
Titulo = """  
<head> 
  <style>
    h1 { color: red; }
  </style>
</head>
<body>
  <center><h1> parámetros</h1><center>
</body>
"""
st.markdown(Titulo, unsafe_allow_html=True)
data = pd.read_excel("data.xls",sheet_name="Sheet1")
st.write(data)
datapozo = pd.read_excel("limeconomicoOSO.xls",sheet_name="Hoja1")
st.write(datapozo)
estadisticas = datapozo.describe()
st.write(estadisticas)
columnas = datapozo.columns
st.write(columnas)
selectbox_columnas= st.selectbox("Seleccione la columna",columnas)
filtro = datapozo[['POZO',selectbox_columnas]]
st.write(filtro)
grafico1 = alt.Chart(datapozo).mark_point().encode(
	x="POZO",
	y= selectbox_columnas).interactive()
st.altair_chart(grafico1)
#Elaboración de listas
l1 = [1,2,3,4,5]
l2 = ["a","b","c","d","e"]
l3 = [math.log(n) for n in l1]
listas = {"numeros":l1,
		  "letras":l2,
		  "l12":l3}
df = pd.DataFrame(listas)
st.write(df)
df["suma"] = df.numeros + df.l12
st.write(df)
i = st.slider("Seleccione un valor",1,1000,400,step=10)
ly = list(range(-i,0))
ly = reversed(ly)
lx = [0] * i 
lz = [0] * i
ejes = {"Eje x":lx,
		"Eje y":ly,
		"Eje z":lz}
df2= pd.DataFrame(ejes)
st.write(df2)
fig = px.line_3d(df2, x="Eje z", y="Eje x", z="Eje y")
st.write(fig)
