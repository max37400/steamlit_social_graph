import pandas as pd
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from pyvis.network import Network

def loader(data,html_filename = 'test.html'): 
  data = data[['to','from','amount','ben_info','ord_info']]
  data = data[data.amount>bias]
  data = data.groupby(['to','from','ben_info','ord_info'],as_index=False).agg(amount_sum=('amount','sum'),amount_count=('amount','count'))
  data.index = np.arange(0,data.shape[0])
  graph = nx.from_pandas_edgelist(data,source='from',target='to',edge_key='amount',create_using=nx.DiGraph())
  from operator import itemgetter
  node_and_degree = graph.degree()
  (largest_hub,degree) = sorted(node_and_degree, key=itemgetter(1))[-1]
  hub_ego = nx.ego_graph(graph,largest_hub,radius=2)
  G = hub_ego
  G = graph

  net = Network(notebook=True,directed=True)

  for node in G.nodes():
     net.add_node(node,title=str(node),label='')
  
  for edge in G.edges():
    user_1, user_2 = edge
    weight = data[(data[' from ' ]==user_1)&(data[ 'to']==user_2)]. amount_sum.values[0]
    ben_pos = data[(data['from']==user_1)&(data ['to']==user_2)]['ben_info'].values[0]
    ord_pos = data[(data['from']==user_1)&(data ['to'] ==user_2)]['ord_info'].values[0] 
    counter = data[(data['from']==user_1)&(data['to']==user_2)]. amount_count.values[0]
    trans = 'transaction' * (counter==1)+'transactions' *(counter>1)
    net.add_edge(user_1, user_2, title=f'Amount: {weight} with {counter} {trans} from {user_1} ({ord_pos}) \n to {user_2}({ben_pos})', arrow_straight=True, arrow_curve=0.3)
  
  net.options.maxVelocity=0.01
  net.show_buttons(filter_=['physics'])
  return net.show(html_filename)