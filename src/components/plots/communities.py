
import streamlit as st
import networkx as nx
import netwulf as nw
import numpy as np

def plot_communities(G):

    st.image("./images/netwulf_positive_network.png", "positive network visualization")
    if st.button("Launch netwulf visualization", key = np.random.rand()):
        graph_data = nx.json_graph.node_link_data(G)
        graph_data['links'] = graph_data.pop('edges')
        nw.visualize(graph_data)