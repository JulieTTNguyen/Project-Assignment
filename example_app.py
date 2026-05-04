import streamlit as st
import pandas as pd 
import networkx as nx
import graphviz
import numpy as np
# Create a sample NetworkX graph
G = nx.Graph()
G.add_edges_from([("A", "B"), ("B", "C"), ("C", "D"), ("D", "A"), ("A", "C")])

# Convert NetworkX graph to GraphViz
def nx_to_graphviz(nx_graph):
    dot = graphviz.Graph()

    # Add nodes
    for node in nx_graph.nodes():
        dot.node(str(node))

    # Add edges
    for edge in nx_graph.edges():
        dot.edge(str(edge[0]), str(edge[1]))

    return dot

# Display the graph
st.title("NetworkX Graph Visualization")
graphviz_graph = nx_to_graphviz(G)
st.graphviz_chart(graphviz_graph)



"""
Run app cli: 

    streamlit run example_app.py

Follow this guide to deploy:

    https://docs.streamlit.io/deploy/streamlit-community-cloud/get-started/quickstart?slug=deploy&slug=streamlit-community-cloud&slug=get-started
"""

st.write("William")

#df = pd.read_csv("./data/COMBINED.csv")
#st.table(df)
number = st.slider("Pick a number", 0, 100, 0)

df = pd.DataFrame({
    'first column': [1, 2, 3, number],
    'second column': [10, 20, 30, 40]
})


st.write(df.style.highlight_max(axis=0))

st.text_input("Your name", key="name")


if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])

    chart_data

st.sidebar.write("Sup")