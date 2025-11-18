import streamlit as st    
import pandas as pd 
import plotly.express as px 
import numpy as np 

st.set_page_config(
    page_title="Dashboard",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown(
    """
    <style>
    /* Hide hamburger menu and footer */
    header {visibility: hidden;}
    footer {visibility: hidden;}
    button[title="Toggle sidebar"] {display: none;}
    </style>
    """,
    unsafe_allow_html=True
)

st.title("BMW Sales From 2010 - 2024 ")
st.write("Welcome to the Rack Visuals")

##caching data 

@st.cache_data
def load_data(path):
    df =pd.read_csv(path)
    return df 


df =load_data("BMW_Sales.csv")


##side bar stuff

st.sidebar.header("Filter Section")
model =["ALL"] +sorted(df['Model'].dropna().unique().tolist())
