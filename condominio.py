import streamlit as st #Streamlit
import numpy as np #Numpy
import pandas as pd #Pandas
import matplotlib.pyplot as plt #Matplotlib
from sklearn.linear_model import LinearRegression #Regressão linear
from sklearn import metrics #Cálculo do erro

st.title('Condominio')

aptos = pd.read_csv('https://raw.githubusercontent.com/mvinoba/notebooks-for-binder/master/dados.csv')

bairro = st.selectbox('Qual Bairro que você procura?',['Botafogo','Copacabana','Gávea','Grajaú','Ipanema','Leblon','Tijuca'])
st.write('Bairro Escolhido',bairro)

quartos = st.slider('Quantos quarto você deseja?', 1, 3, 1)
st.write('Números de quartos: ',quartos)

area = st.slider('Quanto de espaço você deseja?(m2)', 19, 475, 200)
st.write('Área: ',area)

rl = LinearRegression

t = aptos[aptos['bairro']=='Tijuca']
a = t[aptos['area']]
st.write(a)
st.write(t)

#if bairro == 'Tijuca':
