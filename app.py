import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from pyvis.network import Network
import os
from utils.data_loader import loader

st.set_page_config('max37400')
st.write("Привет!\nДанное приложение позволит тебе построить граф по входному файлу.")
bias = st.number_input('Введите сумму, ниже которой не будет вестись учет транзакций',min_value=0,max_value=100000000,value=5000,help='введите число больше 0')
html = st.text_input('Введите название для выходного html файла',value='test')
html = html+'.html'
st.write(f'Вы выбрали значение {bias}')
st.write('## Загрузите файл с данными ниже')
st.write('### Помните, что нужны колонки с названиями ВНЕСТИ НАЗВАНИЯ')
filename = st.file_uploader(label='trans data',type=['csv','xlsx','xls'])
if filename:
    st.write(f'You uploaded {filename.name}')
    if filename.name.endswith('csv'):
       data = pd.read_csv(filename)
    elif filename.name.endswith('xlsx'):
       data = pd.read_excel(filename)
    st.dataframe(data)
    loader(data,html,bias)
#st.progress()

if filename and os.path.exists('./html_files/'+html):
   HtmlFile = open('./html_files/'+html, 'r', encoding='utf-8')
   source_code = HtmlFile.read() 
   components.html(source_code, height = 900,width=900,scrolling=True)
   st.download_button(label='download graph',data = source_code, file_name='./html_files/'+html,mime='text/html')