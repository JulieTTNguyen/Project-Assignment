import streamlit as st
import pandas as pd 
import networkx as nx
import graphviz
import numpy as np
import streamlit as st



#5. Website
#Your project should be understandable to someone outside the course. - 
#Are the visualizations informative and well chosen? - 
# Are explanations clear and accessible to a broad audience? - 
# Is the website easy to navigate and pleasant to use?
st.title("Subreddit Hyperlink Network Analysis")

st.write(
    "Reddit subreddits have been one of the loudest voices of the internet in recent decades. "
    "They facilitate discussions on almost any imaginable topic, whether positive or hateful. "
    "Depending on the topics they cover, their activity levels, guidelines, and communities vary significantly. "
    "This sparked our interest in deepening our understanding of this modern essential social structure.\n\n"

    "Our project began with the question:\n"
    "\"Can meaningful patterns be inferred from the social and antisocial behaviour of subreddits?\"\n\n"

    "This led us through many interesting analyses and raised even more questions that we wanted to answer:\n\n"

    "- How can we understand inter-subreddit attacks by examining the degree distribution? "
    "More specifically, how can we understand antisocial subreddit behaviour through the ratio of in-degree and out-degree?\n\n"

    "- What meaningful communities can be identified in the positive hyperlink network? "
    "What characterises the largest communities in the positive network based on text analysis of their descriptions?\n\n"

    "- What characterises the top and bottom 10 subreddits by out-degree in the negative network, "
    "based on text analysis of their descriptions?\n\n"

    "The purpose of this website is to present and visualise our research findings. Enjoy"
)

st.subheader("Overview")

st.write(
    """
    To make the website easy to navigate, we divided our research into five pages that chronologically present our workflow.

    - **Data Gathering** explains how we downloaded and merged the SNAP and subreddit datasets.
    - **Analysis Pages** present the results of our network and text analysis.
    - **Conclusion** provides a brief summary of our findings.
    - **Discussion** places our analysis into a broader perspective.
    """
)

#st.subheader("Work and Code")

# Give this URL to nbviewer to update when done:
# https://nbviewer.org/github/JulieTTNguyen/Project-Assignment/blob/main/src/explainer_notebook.ipynb

#with st.container(border=True):
st.markdown(
    """
    ### Explainer Notebook

    This notebook covers the complete analysis pipeline, including:

    - Data preprocessing
    - Graph analysis
    - Text analysis
    - Visualisations and figures
    """
)

st.link_button(
    "Open Explainer Notebook",
    "https://nbviewer.org/github/JulieTTNguyen/Project-Assignment/blob/main/src/explainer_notebook.ipynb",
)