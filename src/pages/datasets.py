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
        - **Post Properties**: A vector of linguistic post properties computed by the creators of the dataset.
        """)

    st.write("The post propererties contained no descriptive text about the subreddits or posts, " \
    "so we choose to remove the features from the dataset. " \
    "The first rows of the dataset can be seen below:")

    SNAP = pd.read_csv("data/SNAP.csv")
    st.dataframe(SNAP.head())



    

    st.link_button("Download dataset here", "https://snap.stanford.edu/data/soc-redditHyperlinks-body.tsv")
    st.link_button("Dataset description here", "https://snap.stanford.edu/data/soc-RedditHyperlinks.html")


st.markdown("We quickly realised that the Hyperlink dataset did not provide enought text description" \
" for properly characterising the subreddits. This meant that we needed to find new data" \
"with descriptions of the subreddits. We first tried to find them by using the reddit API, " \
"but our requests were denied and we were not able to pursue this path. " \
"We then decided to find data on subreddits elsewhere. " \
"In this search, we found datasets on Academic Torrents as seen below:")


with st.expander("Reddit Subreddit Dataset"):
    st.write("We have created our own dataset by combining two subreddit scraped datasets from " \
    "Academic Torrents. The first one is from January 2025 and the second one is from January 2024." \
    "They both had one .zst file, which included a heap of information about the subreddits.)")

    st.write("The datasets contained the following features: ")
    with st.expander("Features in the subreddit dataset"):
        st.dataframe(['_meta', 'accept_followers','accounts_active','accounts_active_is_fuzzed','active_user_count','advertiser_category','all_original_content', 'allow_discovery', 'allow_galleries','allow_images', 'allow_polls','allow_prediction_contributors', 'allow_predictions','allow_predictions_tournament', 'allow_talks','allow_videogifs', 'allow_videos','allowed_media_in_comments',
 'banner_background_color', 'banner_background_image', 'banner_img', 'banner_size', 'can_assign_link_flair', 'can_assign_user_flair', 'collapse_deleted_comments', 'comment_contribution_settings', 'comment_score_hide_mins', 'community_icon', 'community_reviewed', 'created', 'created_utc', 'description', 'disable_contributor_requests', 'display_name', 'display_name_prefixed', 'emojis_custom_size', 'emojis_enabled', 'free_form_reports', 'has_menu_widget', 'header_img', 'header_size',
 'header_title', 'hide_ads', 'icon_img', 'icon_size', 'id', 'is_crosspostable_subreddit', 'is_default_banner', 'is_default_icon', 'is_enrolled_in_new_modmail', 'key_color', 'lang', 'link_flair_enabled', 'link_flair_position', 'mobile_banner_image', 'name', 'notification_level', 'original_content_tag_enabled', 'over18', 'prediction_leaderboard_entry_type', 'primary_color', 'public_description', 'public_traffic', 'quarantine', 'restrict_commenting', 'restrict_posting', 'retrieved_on', 'should_archive_posts', 'should_show_media_in_comments_setting',
 'show_media', 'show_media_preview', 'spoilers_enabled', 'submission_type','submit_link_label', 'submit_text', 'submit_text_html', 'submit_text_label','subreddit_type', 'subscribers', 'suggested_comment_sort', 'title', 'url', 'user_can_flair_in_sr', 'user_flair_background_color', 'user_flair_css_class', 'user_flair_enabled_in_sr', 'user_flair_position', 'user_flair_richtext', 'user_flair_template_id',
 'user_flair_text', 'user_flair_text_color', 'user_flair_type', 'user_has_favorited', 'user_is_banned', 'user_is_contributor', 'user_is_moderator', 'user_is_muted', 'user_is_subscriber', 'user_sr_flair_enabled', 'user_sr_theme_enabled', 'videostream_links_count', 'wiki_enabled', 'wls', 'whitelist_status',
 'interstitial_warning_message', 'quarantine_message', 'quarantine_message_html', 'quarantine_permissions', 'content_category'])
    
    st.write("This is way too much information, and we decided to only keep the description, " \
    "the title, the display name and the url. We then filtered the datasets away that did not have a description.")

    st.write("The 2025 dataset had 22 million subreddits at first and 908.790 with a description, "  
             "while the 2024 dataset had 18 million subreddits and 610 369 with a description. "
             "We then merged the two datasets and removed duplicates, which left us with 925 958 subreddits"
             "in total. The first rows of the dataset can be seen below:")



    # df = pd.read_csv("data/subreddits/big_subreddit_dataframe.csv")

    # st.dataframe(df.head())

    st.write("Each dataset is quite large (several GB), so we do not recommed dowloading it below.")
    st.link_button("Download 2025 dataset here", "https://academictorrents.com/download/5d0bf258a025a5b802572ddc29cde89bf093185c.torrent")
    st.link_button("Download 2024 dataset here", "https://academictorrents.com/download/c902f4b65f0e82a5e37db205c3405f02a028ecdf.torrent")

    st.write("The dataset description can be found here: ")
    st.link_button("Link to 2025 dataset description", "https://academictorrents.com/details/5d0bf258a025a5b802572ddc29cde89bf093185c")
    st.link_button("Link to 2024 dataset description", "https://academictorrents.com/details/c902f4b65f0e82a5e37db205c3405f02a028ecdf")


st.title("Combining the datasets")

st.write("We then modified the two datasets by only including subreddits that were present in both datasets. " \
"This was done by creating a list of subreddits in each dataset and finding the union of this. " \
"We then subsampled both the SNAP dataset and the subreddit descriptions dataset to only include subreddits in this union. " \
"This left us with a total of 11 239 subreddits and 68 856 hyperlinks/posts between them.")

st.markdown("""**Dataset sizes before and after merging** """)

df= pd.DataFrame({"":["Subreddits in descriptions dataset","Subreddits in SNAP dataset","Hyperlinks in SNAP dataset"],"Before":["925 958","35 776","286 561"],"After":["11 239","11 239","68 856"]})
st.dataframe(df,hide_index=True)