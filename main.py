# Imports
# -----------------------------------------------------------
import cv2
import base64
import streamlit as st
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns

# -----------------------------------------------------------
# Helper functions
# -----------------------------------------------------------
def run_kmeans(df, n_clusters=2):
    kmeans = KMeans(n_clusters, random_state=0).fit(df[["Age", "Income"]])

    fig, ax = plt.subplots(figsize=(16, 9))

    #Create scatterplot
    ax = sns.scatterplot(
        ax=ax,
        x=df.Age,
        y=df.Income,
        hue=kmeans.labels_,
        palette=sns.color_palette("colorblind", n_colors=n_clusters),
        legend=None,
    )

    return fig

# Load data from external source
# df = pd.read_csv(".csv")
img1 = "image1.gif"
img2 = cv2.imread("image2.jpg")
img3 = cv2.imread("image3.jpg")

# -----------------------------------------------------------
# SIDEBAR
# -----------------------------------------------------------
sidebar = st.sidebar
sidebar.title("Dashboard")
sidebar.write("List of Completed Projects:")

df_display_1 = sidebar.checkbox("1. T22 SV Weld AI Vision", value=True)
df_display_2 = sidebar.checkbox("2. Missing Cell Check by YOLO", value=True)
df_display_3 = sidebar.checkbox("3. Missing Washer Detection by YOLO", value=True)

# -----------------------------------------------------------
# Main
# -----------------------------------------------------------
# Create a title for your app
st.title("AI Projects")
# A description
st.write("Here is the list of all completed AI vision projects")

if df_display_1:
    # A title 
    st.title("1. T22 SV Weld AI Vision")
    # A description
    st.write("Automated Safety Vent (SV) weld condition check")   
    file_ = open("image1.gif", "rb")
    contents = file_.read()
    data_url = base64.b64encode(contents).decode("utf-8")
    file_.close()
    st.markdown(f'<img src="data:image/gif;base64,{data_url}" alt="cat gif">', unsafe_allow_html=True,)


if df_display_2:
    # A title 
    st.title("2. Missing Cell Check by YOLO")
    # A description
    st.write("Automated cell quantity checker for shipping tray")    
    file_ = open("image2.gif", "rb")
    contents = file_.read()
    data_url = base64.b64encode(contents).decode("utf-8")
    file_.close()
    st.markdown(f'<img src="data:image/gif;base64,{data_url}" alt="cat gif">', unsafe_allow_html=True,)

   
if df_display_3:
    # Create a title for your app
    st.title("3. Missing Washer Detection by YOLO")
    # A description
    st.write("Automated defect inspection system for missing washer check")
    #st.image(img3, width=None)
    file_ = open("image3.gif", "rb")
    contents = file_.read()
    data_url = base64.b64encode(contents).decode("utf-8")
    file_.close()
    st.markdown(f'<img src="data:image/gif;base64,{data_url}" alt="cat gif">', unsafe_allow_html=True,)



# -----------------------------------------------------------
