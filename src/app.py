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
        st.Page("pages/main.py", title="Overview"),
        #st.Page("manage_account.py", title="Manage your account"),
    ],
    "Gathering data": [
        st.Page("pages/datasets.py", title="Dataset download and cleaning"),
        #st.Page("manage_account.py", title="Manage your account"),
    ],
    "Analysis": [
        st.Page("pages/analysis/network.py", title="Network analysis"),
        st.Page("pages/analysis/text.py", title="Text analysis"),
        #st.Page("trial.py", title="Try it out"),
    ],
     "Concluding Remarks": [
        st.Page("pages/concluding_remarks/conclusion.py", title="Conclusion"),
        st.Page("pages/concluding_remarks/discussion.py", title="Discussion"),
        #st.Page("trial.py", title="Try it out"),
    ],
}

pg = st.navigation(pages)
pg.run()