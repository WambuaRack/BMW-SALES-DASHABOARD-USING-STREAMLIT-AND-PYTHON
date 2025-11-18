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

st.sidebar.header("BMW Filter Section")
model =["ALL"] +sorted(df['Model'].dropna().unique().tolist())
selected_model =st.sidebar.selectbox("BMW MODEL", model)
year =["ALL"] +sorted(df['Year'].dropna().unique().tolist())
selected_year =st.sidebar.selectbox("YEAR", year)
Color =["ALL"] +sorted(df['Color'].dropna().unique().tolist())
selected_Color =st.sidebar.selectbox(" Color", Color)
Transmission =["ALL"] +sorted(df['Transmission'].dropna().unique().tolist())
selected_Transmission =st.sidebar.selectbox(" Transmission", Transmission)
Region =["ALL"] +sorted(df['Region'].dropna().unique().tolist())
selected_Region=st.sidebar.selectbox(" Region", Region)
Fuel_Type =["ALL"] +sorted(df['Fuel_Type'].dropna().unique().tolist())
selected_Fuel_Type=st.sidebar.selectbox(" Fuel_Type", Fuel_Type)

min_mileage, max_mileage=int(df["Mileage_KM"].min()), int(df["Mileage_KM"].max())
mileage_range =st.sidebar.slider("Mileage Range",min_mileage,max_mileage,(min_mileage,max_mileage))
Sales =["ALL"] +sorted(df['Sales_Classification'].dropna().unique().tolist())
selected_Sales=st.sidebar.selectbox(" Sales_Classification", Sales)


##Applying filters

filtered =df.copy()
if selected_model !="ALL":
    filtered =filtered[filtered['Model']== selected_model]
    
if selected_year !="ALL":
    filtered =filtered[filtered['Year']== selected_year]
    
if selected_Color !="ALL":
    filtered =filtered[filtered['Color']== selected_Color]
    
if selected_Transmission !="ALL":
    filtered =filtered[filtered['Transmission']== selected_Transmission]
if selected_Region!="ALL":
    filtered =filtered[filtered['Region']== selected_Region]
    
if selected_Fuel_Type!="ALL":
    filtered =filtered[filtered['Fuel_Type']== selected_Fuel_Type]
if selected_Sales!="ALL":
    filtered =filtered[filtered['Sales_Classification']== selected_Sales]
    
filtered =filtered[(filtered['Mileage_KM'] >=mileage_range[0]) & (filtered['Mileage_KM'] >=mileage_range[0]) ]

st.write("#### KPIs")
avg_sales_v=filtered["Sales_Volume"].mean()
avg_price =filtered["Price_USD"].mean()
mx_price =filtered["Price_USD"].max()
avg_mileage = filtered["Mileage_KM"].mean()
min_mileage = filtered["Mileage_KM"].min()
max_mileage = filtered["Mileage_KM"].max()

avg_engine_size = filtered["Engine_Size_L"].mean()
unique_engine_sizes = filtered["Engine_Size_L"].nunique()
top_models = filtered["Model"].value_counts().nlargest(5)

top_region = filtered["Region"].value_counts().idxmax()
region_counts = filtered["Region"].value_counts()


top_colors = filtered["Color"].value_counts().nlargest(3)
st.write("#### 🔑 Key Performance Indicators")
# --- Row 1: Financial and Volume KPIs (3 columns) ---
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        label="Average Sales Price (USD)",
        value=f"${avg_price:,.0f}", 
        delta=f"Max: ${mx_price:,.0f}" # Using delta to show the maximum price
    )

with col2:
    st.metric(
        label="Average Sales Volume",
        value=f"{avg_sales_v:.1f} units",
        delta="Per Listing"
    )

with col3:
    st.metric(
        label="Top Selling Model",
        # Access the index of the top_models Series to get the name
        value=top_models.index[0] if not top_models.empty else "N/A", 
        delta=f"In {top_region}"
    )

st.markdown("---") # Separator line for visual clarity

# --- Row 2: Vehicle Condition and Technical Specs (4 columns) ---
st.write("#### 🚗 Vehicle Condition and Specs")
col4, col5, col6, col7 = st.columns(4)

with col4:
    st.metric(
        label="Avg. Mileage (KM)",
        value=f"{avg_mileage:,.0f}", 
        delta=f"Min: {min_mileage:,.0f} KM"
    )

with col5:
    st.metric(
        label="Max Mileage (KM)",
        value=f"{max_mileage:,.0f}"
    )

with col6:
    st.metric(
        label="Avg. Engine Size (L)",
        value=f"{avg_engine_size:.2f} L"
    )

with col7:
    st.metric(
        label="Unique Engine Sizes",
        value=unique_engine_sizes,
        delta=f"Top Color: {top_colors.index[0] if not top_colors.empty else 'N/A'}"
    )
    
    
    ##charts
fig1= px.bar(filtered,x='Year', y='Sales_Volume')
st.write("### Sales VVolume  per Year")
st.plotly_chart(fig1,use_container_width=True)

fig2 =px.histogram(filtered,x="Price_USD",nbins=30, title=f"Price distribution in {selected_Region}")
st.write("### Price distribution per Region")
st.plotly_chart(fig2,use_container_width=True)