import streamlit as st
import pandas as pd 
import networkx as nx
import graphviz
import numpy as np
import streamlit as st


st.header("Subreddit Hyperlink Network Analysis")

st.write("This website purpose is visualize and explain which subreddit communities attack or support each other and what characterizes them. " \
"It will explore the following topics: \n" \
"- Can communities be inferred from hyperlinks in subreddit posts. \n" \
"- Do the found communities make sense and what characteries them. \n" \
"- Are there similar language patterns within the communities"
)





st.subheader("Implementation")
st.write("""
    Networks setup: \n
1) Link the subreddit description as a node attribute for each subreddit in the network.
2) Make two networks with positive and negative links 
3) Edge weights equal the number of links between the two subreddits.
4) Obtain the largest strongly connected component of each network

Network analysis:\n
5) Identify communities of subreddits using louvain community detection.
6) Examine degree distribution of the networks (weighted and unweighted)
7) Visualize graphs

Text analysis: \n
8) Examine the difference in language in the descriptions of positive and negative networks. 
9) Extract the most common tokens

Topic Analysis: \n
10) Extract topics using TF-IDF
11) Visualize the most common topics

MAYBE: \n
- Analyze the networks over time (since the network contains the time_stamps)

""")

st.subheader("Work and code")


# give this url to nbviewer to update when done https://nbviewer.org/github/JulieTTNguyen/Project-Assignment/blob/main/src/explainer_notebook.ipynb
with st.container(border=True):
    st.markdown("""
    **Explainer Notebook**  
    This notebook covers the full analysis pipeline including data preprocessing, graph and text analysis as well as all graphs.
    """)
    st.link_button("Open explainer notebook", 
                   "https://nbviewer.org/github/JulieTTNguyen/Project-Assignment/blob/main/src/explainer_notebook.ipynb")
    
