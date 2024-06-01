import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
from pyvis.network import Network

st.set_page_config('max37400')
st.write("Привет!\nДанное приложение позволит тебе построить граф по входному файлу.")
bias = st.number_input('Введите сумму, ниже которой не будет вестись учет тразакций',min_value=0,max_value=100000000,value=5000,help='введите число больше 0')
st.write(f'Вы выбрали значение {bias}')
st.write('## Загрузите файл с данными ниже')
st.write('### Помните, что нужны колонки с названиями ВНЕСТИ НАЗВАНИЯ')
filename = st.file_uploader(label='trans data',type=['csv','xlsx','xls'])
st.write(f'You uploaded {filename}')
if filename:
    data = pd.read_csv(filename)
    st.dataframe(data)
#st.progress()

def simple_func(): 
  nx_graph = nx.cycle_graph(10)
  nx_graph.nodes[1]['title'] = 'Number 1'
  nx_graph.nodes[1]['group'] = 1
  nx_graph.nodes[3]['title'] = 'I belong to a different group!'
  nx_graph.nodes[3]['group'] = 10
  nx_graph.add_node(20, size=20, title='couple', group=2)
  nx_graph.add_node(21, size=15, title='couple', group=2)
  nx_graph.add_edge(20, 21, weight=5, title='test title')
  nx_graph.add_node(25, size=25, label='lonely', title='lonely node', group=3)


  nt = Network("600px", "600px",notebook=True,heading='')
  nt.from_nx(nx_graph)
  nt.show_buttons(filter_=['physics'])
  #physics=st.sidebar.checkbox('add physics interactivity?')
  return nt.show('test.html')

simple_func()
HtmlFile = open("test.html", 'r', encoding='utf-8')
source_code = HtmlFile.read() 
components.html(source_code, height = 900,width=900,scrolling=True)
st.download_button(label='download graph',data = source_code, file_name='test.html',mime='text/html')