import streamlit as st
import pandas as pd
import plotly.express as px

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="BMW Sales Dashboard",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- CUSTOM STYLING ---
st.markdown(
    """
    <style>
    header {visibility: hidden;}
    footer {visibility: hidden;}
    button[title="Toggle sidebar"] {display: none;}
    .stApp {background-color: #f9f9f9;}
    </style>
    """,
    unsafe_allow_html=True
)

st.title("BMW Sales Dashboard (2010 - 2024)")
st.write("Welcome to the interactive BMW Sales Analytics Dashboard!")

# --- DATA LOADING ---
@st.cache_data
def load_data(path):
    df = pd.read_csv(path)
    return df

df = load_data("BMW_Sales.csv")

# --- SIDEBAR FILTERS ---
st.sidebar.header("Filter Options")
model_list = ["ALL"] + sorted(df['Model'].dropna().unique().tolist())
selected_model = st.sidebar.selectbox("Model", model_list)

year_list = ["ALL"] + sorted(df['Year'].dropna().unique().tolist())
selected_year = st.sidebar.selectbox("Year", year_list)

color_list = ["ALL"] + sorted(df['Color'].dropna().unique().tolist())
selected_color = st.sidebar.selectbox("Color", color_list)

trans_list = ["ALL"] + sorted(df['Transmission'].dropna().unique().tolist())
selected_transmission = st.sidebar.selectbox("Transmission", trans_list)

region_list = ["ALL"] + sorted(df['Region'].dropna().unique().tolist())
selected_region = st.sidebar.selectbox("Region", region_list)

fuel_list = ["ALL"] + sorted(df['Fuel_Type'].dropna().unique().tolist())
selected_fuel = st.sidebar.selectbox("Fuel Type", fuel_list)

sales_list = ["ALL"] + sorted(df['Sales_Classification'].dropna().unique().tolist())
selected_sales = st.sidebar.selectbox("Sales Classification", sales_list)

min_mileage, max_mileage = int(df["Mileage_KM"].min()), int(df["Mileage_KM"].max())
mileage_range = st.sidebar.slider("Mileage Range (KM)", min_mileage, max_mileage, (min_mileage, max_mileage))

# --- APPLY FILTERS ---
filtered = df.copy()
if selected_model != "ALL": filtered = filtered[filtered['Model'] == selected_model]
if selected_year != "ALL": filtered = filtered[filtered['Year'] == selected_year]
if selected_color != "ALL": filtered = filtered[filtered['Color'] == selected_color]
if selected_transmission != "ALL": filtered = filtered[filtered['Transmission'] == selected_transmission]
if selected_region != "ALL": filtered = filtered[filtered['Region'] == selected_region]
if selected_fuel != "ALL": filtered = filtered[filtered['Fuel_Type'] == selected_fuel]
if selected_sales != "ALL": filtered = filtered[filtered['Sales_Classification'] == selected_sales]
filtered = filtered[(filtered['Mileage_KM'] >= mileage_range[0]) & (filtered['Mileage_KM'] <= mileage_range[1])]

# --- KPIs ---
avg_sales_v = filtered["Sales_Volume"].mean()
avg_price = filtered["Price_USD"].mean()
mx_price = filtered["Price_USD"].max()
avg_mileage = filtered["Mileage_KM"].mean()
min_mileage = filtered["Mileage_KM"].min()
max_mileage = filtered["Mileage_KM"].max()
avg_engine_size = filtered["Engine_Size_L"].mean()
unique_engine_sizes = filtered["Engine_Size_L"].nunique()
top_models = filtered["Model"].value_counts().nlargest(5)
top_region = filtered["Region"].value_counts().idxmax()
top_colors = filtered["Color"].value_counts().nlargest(3)

st.write("#### 🔑 Key Performance Indicators")
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Avg Sales Price (USD)", f"${avg_price:,.0f}", delta=f"Max: ${mx_price:,.0f}")
with col2:
    st.metric("Avg Sales Volume", f"{avg_sales_v:.1f} units", delta="Per Listing")
with col3:
    st.metric("Top Selling Model", top_models.index[0] if not top_models.empty else "N/A", delta=f"In {top_region}")

col4, col5, col6, col7 = st.columns(4)
with col4:
    st.metric("Avg Mileage (KM)", f"{avg_mileage:,.0f}", delta=f"Min: {min_mileage:,.0f}")
with col5:
    st.metric("Max Mileage (KM)", f"{max_mileage:,.0f}")
with col6:
    st.metric("Avg Engine Size (L)", f"{avg_engine_size:.2f}")
with col7:
    st.metric("Unique Engine Sizes", unique_engine_sizes, delta=f"Top Color: {top_colors.index[0] if not top_colors.empty else 'N/A'}")

st.markdown("---")

# --- CHARTS ---
st.write("### 📊 Sales Analytics")

# Row 1: Sales Trends
c1, c2 = st.columns(2)
with c1:
    sales_year = filtered.groupby('Year')['Sales_Volume'].sum().reset_index()
    fig1 = px.line(sales_year, x='Year', y='Sales_Volume', markers=True, title="Total Sales Volume Over Years")
    fig1.update_traces(line=dict(color="blue", width=3))
    st.plotly_chart(fig1, use_container_width=True)
with c2:
    price_year = filtered.groupby('Year')['Price_USD'].mean().reset_index()
    fig2 = px.line(price_year, x='Year', y='Price_USD', markers=True, title="Average Price Over Years")
    fig2.update_traces(line=dict(color="green", width=3))
    st.plotly_chart(fig2, use_container_width=True)

# Row 2: Distribution Charts
c3, c4 = st.columns(2)
with c3:
    fig3 = px.histogram(filtered, x="Price_USD", nbins=30, color="Fuel_Type", title="Price Distribution by Fuel Type")
    st.plotly_chart(fig3, use_container_width=True)
with c4:
    fig4 = px.histogram(filtered, x="Mileage_KM", nbins=30, color="Transmission", title="Mileage Distribution by Transmission")
    st.plotly_chart(fig4, use_container_width=True)

# Row 3: Categorical Charts
c5, c6 = st.columns(2)
with c5:
    region_sales = filtered.groupby("Region")["Sales_Volume"].sum().reset_index()
    fig5 = px.bar(region_sales, x="Region", y="Sales_Volume", color="Region", title="Sales Volume by Region")
    st.plotly_chart(fig5, use_container_width=True)
with c6:
    color_sales = filtered.groupby("Color")["Sales_Volume"].sum().reset_index()
    fig6 = px.pie(color_sales, names="Color", values="Sales_Volume", title="Sales by Car Color")
    st.plotly_chart(fig6, use_container_width=True)

# Row 4: Technical Specs
c7, c8 = st.columns(2)
with c7:
    fig7 = px.box(filtered, x="Model", y="Price_USD", color="Model", title="Price Distribution per Model")
    st.plotly_chart(fig7, use_container_width=True)
with c8:
    fig8 = px.violin(filtered, x="Transmission", y="Mileage_KM", color="Transmission", box=True, points="all",
                     title="Mileage Distribution by Transmission")
    st.plotly_chart(fig8, use_container_width=True)

# Row 5: Scatter Analysis
c9, c10 = st.columns(2)
with c9:
    fig9 = px.scatter(filtered, x="Mileage_KM", y="Price_USD", color="Fuel_Type", size="Engine_Size_L",
                      hover_data=["Model", "Year", "Region"], title="Price vs Mileage")
    st.plotly_chart(fig9, use_container_width=True)
with c10:
    fig10 = px.scatter(filtered, x="Price_USD", y="Sales_Volume", color="Region", size="Engine_Size_L",
                       hover_data=["Model"], title="Sales Volume vs Price")
    st.plotly_chart(fig10, use_container_width=True)
