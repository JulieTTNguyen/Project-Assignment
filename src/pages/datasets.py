import streamlit as st
import pandas as pd 
import networkx as nx
import graphviz
import numpy as np


st.title("How we gathered our data")

st.markdown("We started to explore our idea by researching the properties of the reddit hyperlink dataset. The most relevant information can be found below")

with st.expander("Reddit Hyperlink Network"):
    st.write("The dataset is made up of posts from one subreddit that contain hyperlinks to another subreddit")

    st.markdown("""
        Each row contains the features below:

        - **Source Subreddit**: Subreddit that sent the post  
        - **Target Subreddit**: Subreddit linked to  
        - **Post ID**: Reddit ID of the post  
        - **Timestamp**: Timestamp for the post  
        - **Post Label**: Explicitly negative/positive toward target subreddit  
        - **Post Properties**: Linguistic analysis for each post
        """)

    st.write("The post propererties contained no describe text about the subreddits or posts, so we choose to remove the feature. This left us with the following datafram.")

    # df = pd.read_csv("../data/subreddits/big_dataframe.csv")

    # st.dataframe(df)

    

    st.link_button("Download dataset here", "https://snap.stanford.edu/data/soc-redditHyperlinks-body.tsv")


st.markdown("We quickly realised that the Hyperlink dataset did not provide enought text description for properly characterising the subreddits. We first tried to find them by using the reddit API, but realised that they do not care about student projects, so they denied our three request. We then decided to use the Reddit Subreddit Information by Torrent, seen below")


with st.expander("Reddit information Network"):
    st.write("This dataset is made up of 4 .zst files about 22 million subreddits in January 2025")

    st.link_button("Download dataset here", "https://snap.stanford.edu/data/soc-redditHyperlinks-body.tsv")


