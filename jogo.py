
import streamlit as st #Streamlit
import numpy as np #Numpy
import pandas as pd #Pandas
import matplotlib.pyplot as plt #Matplotlib
from sklearn.linear_model import LinearRegression #Regressão linear
from sklearn import metrics #Cálculo do erro

st.title('JOGO')

tempo = st.selectbox('Qual o tempo ?',['Chuvoso','Ensolarado','Nublado'])
st.write('Tempo escolhido',tempo)

vento = st.selectbox('Vai ter vento?',['Sim','Não'])
st.write('vento escolhido',vento)

st.metric(label='Umidade', value='90', delta='83')

st.metric(label='Temperatura', value='15 °C', delta='23')

