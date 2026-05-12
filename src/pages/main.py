import streamlit as st
import pandas as pd 
import networkx as nx
import graphviz
import numpy as np
import streamlit as st






# give this url to nbviewer to update when done https://nbviewer.org/github/JulieTTNguyen/Project-Assignment/blob/main/src/explainer_notebook.ipynb
with st.container(border=True):
    st.markdown("""
    **Explainer Notebook**  
    This notebook covers the full analysis pipeline including data preprocessing, graph and text analysis as well as all graphs.
    """)
    st.link_button("Open explainer notebook", 
                   "https://nbviewer.org/github/JulieTTNguyen/Project-Assignment/blob/main/src/explainer_notebook.ipynb")