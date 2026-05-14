import streamlit as st
import networkx as nx
import netwulf as nw
import pandas as pd

def load_basic_network_table():
    df = pd.DataFrame({"":
                    ["Positive subreddit network","Negative subreddit network"],
                    "Nodes":["a","b "],
                    "Links":["c","d"]})

    st.dataframe(df,hide_index=True)