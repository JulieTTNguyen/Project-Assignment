import streamlit as st
import pandas as pd 
import networkx as nx
import graphviz
import numpy as np

"""
Run app cli: 

    streamlit run src/app.py

Follow this guide to deploy:

    https://docs.streamlit.io/deploy/streamlit-community-cloud/get-started/quickstart?slug=deploy&slug=streamlit-community-cloud&slug=get-started
"""

pages = {
    "Goal & Intro": [
        st.Page("pages/goal.py", title="Overview"),
        #st.Page("manage_account.py", title="Manage your account"),
    ],
    "Gathering data": [
        st.Page("pages/datasets.py", title="Dataset download and cleaning"),
        #st.Page("manage_account.py", title="Manage your account"),
    ],
    "Analysis": [
        st.Page("pages/semantic.py", title="Semantic analysis"),
        #st.Page("trial.py", title="Try it out"),
    ],
}

pg = st.navigation(pages)
pg.run()