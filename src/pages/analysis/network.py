import streamlit as st
import pandas as pd 
import networkx as nx
import graphviz
import numpy as np
from components.plots.communities import plot_communities
from components.tables.network_tables import load_basic_network_table
import json
from environment import FILTER_THRESSHOLD 


st.title("Creating the graphs")

st.write("In this section, we will outline our analysis of the subreddits networks with the use of python packages networks and netwulf. " \
"The foundation for this analysis is the updated SNAP dataset that we extracted in the dataset download and cleaning sektion. " \
"It contained the following columns" )

with st.expander("Columns in combined dataframe"):
        st.dataframe(["SOURCE_SUBREDDIT", "TARGET_SUBREDDIT", "TIMESTAMP", "LINK_SENTIMENT", "DESCRIPTION"])

st.write("We chosse to create two seperate network graph, one for the positive link sentiment and one for the negative." \
"In each graph, the subreddits were the nodes, the amount of posts between two subreddits were the weight of the links, and the descriptions set to attributes to each node. " \
"We then found the biggest component for each graph. The networks had the following sizes")



load_basic_network_table()


st.title("Visualization")

st.write("We split the positive graph into communities using the louvain communities. - MAYBE WRITE HOW IT DOES IT ")

st.info("Eventhough both graph seems similar, it only made sense to split the positive graph into communities. " \
"This decision was base on our assumptions about hate and love. " \
"One would assume, that if you like two friends, they would also like each other, since they most likely share the same personality traits or interrest." \
"However, if one hates two different people, then they might be from the same group, and therefore do not hate each other.")

st.write("We visualized the communities using the netwulf package, but quickly realised the network contained to many notes to make a meaningful analysis.")


with open("./data/positive_communities.json", 'r') as file:
    data = json.load(file)
G_positive_communities = nx.node_link_graph(data)

plot_communities(G_positive_communities)

st.subheader("Filtering")


st.write(f"To overcome this obstacle, we decided to filter our all links with weights under {FILTER_THRESSHOLD}. " \
"This helped us to avoid isolate subreddit pairs and more random connections. " \
"Our netork now consist of 1599 nodes and 142 links. Which allowed us to visalize it agian")


with open("./data/filtered_positiv_communities.json", 'r') as file:
    data = json.load(file)
filtered_G_positive_communities = nx.node_link_graph(data)

plot_communities(filtered_G_positive_communities)

st.write("Several interresting observations can be made from the graph. The religious and gay communities have a lot of connections")

st.title("Degree distribution analysis")

st.write(""" We want to analyze the out- and in-degrees for the negative and positive network.

There is a difference between analyzing the unweighted and weighted degree distribution:
- Without considering edge weighting, we only analyze how many distinct subreddits each subreddit attacks/sends love to.
- Considering weighted edge weighting, we analyze how many times each subreddit attacks/sends love to other subreddits.""")


st.subheader("Unweighted degree")
















