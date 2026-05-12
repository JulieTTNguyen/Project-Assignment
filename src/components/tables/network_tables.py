import streamlit as st
import networkx as nx
import netwulf as nw
import pandas as pd

def load_basic_network_table():
    df = pd.DataFrame({"":
                    ["Positive subreddit network","Positive subreddit network largest component","Negative subreddit network","Negative subreddit network largest component"],
                    "Nodes":["a","b ","x", "y"],
                    "Links":["c","67","x", "y"]})

    st.dataframe(df,hide_index=True)