"""Module for DataFrame modification and Network creation"""

import pandas as pd
import networkx as nx# type: ignore
from pyvis.network import Network# type: ignore

def loader(data:pd.DataFrame,html_filename:str = 'test.html' ,bias:int = 5000):
    """data transform to build Net"""
    data = data[['to','from','amount','ben_info','ord_info']]
    #data.fillna('-',inplace=True)
    data = data[data.amount>bias]
    data = data.groupby(['to','from','ben_info','ord_info'],as_index=False,dropna=False)\
      .agg(amount_sum=('amount','sum'),amount_count=('amount','count'))
    data = data.reset_index(drop=True)
    graph = nx.from_pandas_edgelist(data,source='from',target='to',
                                    edge_key='amount',create_using=nx.DiGraph())
    #from operator import itemgetter
    #node_and_degree = graph.degree()
    #(largest_hub,_) = sorted(node_and_degree, key=itemgetter(1))[-1]
    #hub_ego = nx.ego_graph(graph,largest_hub,radius=2)
    #G = hub_ego
    #G = graph

    net = Network(notebook=True,directed=True)

    for node in graph.nodes():
        net.add_node(node,title=str(node), label=' ')
    for edge in graph.edges():
        user_1, user_2 = edge
        weight = data[(data['from' ]==user_1)&(data['to']==user_2)].amount_sum.values[0]
        ben_pos = data[(data['from']==user_1)&(data ['to']==user_2)]['ben_info'].values[0]
        ord_pos = data[(data['from']==user_1)&(data ['to'] ==user_2)]['ord_info'].values[0]
        counter = data[(data['from']==user_1)&(data['to']==user_2)].amount_count.values[0]
        trans = 'transaction' * (counter==1)+'transactions' *(counter>1)
        title = f'Amount: {weight} with {counter}\
            {trans} from {user_1} ({ord_pos})\n to {user_2}({ben_pos})'
        net.add_edge(user_1, user_2,title=title,arrow_straight=True, arrow_curve=0.3)

    net.options.maxVelocity=0.01
    net.show_buttons(filter_=['physics'])
    return net.show('./html_files/'+html_filename)
