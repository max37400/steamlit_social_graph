"""The main script for streamlit application"""
import os
import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
from utils.data_loader import transform_data_to_graph

st.set_page_config('max37400')
st.session_state.file_loaded = False
st.write("Привет!\nДанное приложение позволит тебе построить граф по входному файлу.")
bias = int(
    st.number_input('Введите сумму, ниже которой не будет вестись учет транзакций',\
                    min_value=0,max_value=100000000,value=5000,help='введите число больше 0',step=1)
                    )
html = st.text_input('Введите название для выходного html файла',value='test')
html = html+'.html'
st.write(f'Вы выбрали значение {bias}')
st.write('## Загрузите файл с данными ниже')
st.write('### Помните, что нужны колонки с названиями ВНЕСТИ НАЗВАНИЯ')
filename = st.file_uploader(label='trans data',type=['csv','xlsx'])
if filename:
    st.write(f'You uploaded {filename.name}')
    if filename.name.endswith('csv'):
        data = pd.read_csv(filename)
    elif filename.name.endswith('xlsx'):
        data = pd.read_excel(filename)
    else:
        data = pd.DataFrame(columns=['to','from','amount','ben_info','ord_info'])# pylint: disable=C0103
    #st.dataframe(data)
    try:
        transform_data_to_graph(data,html,bias)
        st.session_state.file_loaded = True
    except KeyError:
        st.subheader(":red[Убедитесь, что файл содержит нужные колонки]")

if filename and os.path.exists('./html_files/'+html) and st.session_state.file_loaded:
    with open('./html_files/'+html, 'r', encoding='utf-8') as HtmlFile:
        source_code = HtmlFile.read()
        components.html(source_code, height = 900,width=900,scrolling=True)
        st.download_button(label='download graph',
                           data = source_code, file_name=html,mime='text/html')
