import streamlit as st    
import pandas as pd 
import plotly.express as px 
import numpy as np 

st.set_page_config(page_title="BMW SALES", layout="wide")
st.title("BMW Sales From 2010 - 2024 ")
st.write("Welcome to the Rack Visuals")

##caching data 

@st.cache_data
def load_data(path):
    df =pd_read_csv(path)
    return df 


df =pd.load_data("BMW_Sales.csv")