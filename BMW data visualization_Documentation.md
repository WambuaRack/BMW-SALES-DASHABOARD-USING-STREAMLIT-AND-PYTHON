### 📄 c:\Users\Administrator\Desktop\BMW data visualization\app.py
*Saved at: 11/18/2025, 1:26:30 PM*

**[REMOVED]**
```
(from line ~108)
st.write("### 📊 Sales Analytics")

```
**[ADDED]**
```
108   st.write("#### Sales Analytics")
```

---

### 📄 c:\Users\Administrator\Desktop\BMW data visualization\app.py
*Saved at: 11/18/2025, 1:23:33 PM*

**[REMOVED]**
```
(from line ~19)
    .stApp {background-color: #f9f9f9;}

```
**[ADDED]**
```
19        .stApp {background-color: #140A6B;}
```

---

### 📄 c:\Users\Administrator\Desktop\BMW data visualization\app.py
*Saved at: 11/18/2025, 1:20:10 PM*

**[REMOVED]**
```
(from line ~153)
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

```

---

### 📄 c:\Users\Administrator\Desktop\BMW data visualization\app.py
*Saved at: 11/18/2025, 1:09:58 PM*

**[REMOVED]**
```
(from line ~1)
import streamlit as st    
import pandas as pd 
import plotly.express as px 
import numpy as np 

```
**[ADDED]**
```
1     import streamlit as st
2     import pandas as pd
3     import plotly.express as px
```
**[ADDED]**
```
5     # --- PAGE CONFIG ---
```
**[REMOVED]**
```
(from line ~7)
    page_title="Dashboard",

```
**[ADDED]**
```
7         page_title="BMW Sales Dashboard",
```
**[ADDED]**
```
12    # --- CUSTOM STYLING ---
```
**[REMOVED]**
```
(from line ~16)
    /* Hide hamburger menu and footer */

```
**[ADDED]**
```
19        .stApp {background-color: #f9f9f9;}
```
**[REMOVED]**
```
(from line ~25)
st.title("BMW Sales From 2010 - 2024 ")
st.write("Welcome to the Rack Visuals")

```
**[ADDED]**
```
25    st.title("BMW Sales Dashboard (2010 - 2024)")
26    st.write("Welcome to the interactive BMW Sales Analytics Dashboard!")
```
**[REMOVED]**
```
(from line ~28)
##caching data 


```
**[ADDED]**
```
28    # --- DATA LOADING ---
```
**[REMOVED]**
```
(from line ~31)
    df =pd.read_csv(path)
    return df 

```
**[ADDED]**
```
31        df = pd.read_csv(path)
32        return df
```
**[ADDED]**
```
34    df = load_data("BMW_Sales.csv")
```
**[REMOVED]**
```
(from line ~36)
df =load_data("BMW_Sales.csv")

```
**[ADDED]**
```
36    # --- SIDEBAR FILTERS ---
37    st.sidebar.header("Filter Options")
38    model_list = ["ALL"] + sorted(df['Model'].dropna().unique().tolist())
39    selected_model = st.sidebar.selectbox("Model", model_list)
```
**[ADDED]**
```
41    year_list = ["ALL"] + sorted(df['Year'].dropna().unique().tolist())
42    selected_year = st.sidebar.selectbox("Year", year_list)
```
**[REMOVED]**
```
(from line ~44)
##side bar stuff

```
**[ADDED]**
```
44    color_list = ["ALL"] + sorted(df['Color'].dropna().unique().tolist())
45    selected_color = st.sidebar.selectbox("Color", color_list)
```
**[REMOVED]**
```
(from line ~47)
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

```
**[ADDED]**
```
47    trans_list = ["ALL"] + sorted(df['Transmission'].dropna().unique().tolist())
48    selected_transmission = st.sidebar.selectbox("Transmission", trans_list)
```
**[REMOVED]**
```
(from line ~50)
min_mileage, max_mileage=int(df["Mileage_KM"].min()), int(df["Mileage_KM"].max())
mileage_range =st.sidebar.slider("Mileage Range",min_mileage,max_mileage,(min_mileage,max_mileage))
Sales =["ALL"] +sorted(df['Sales_Classification'].dropna().unique().tolist())
selected_Sales=st.sidebar.selectbox(" Sales_Classification", Sales)

```
**[ADDED]**
```
50    region_list = ["ALL"] + sorted(df['Region'].dropna().unique().tolist())
51    selected_region = st.sidebar.selectbox("Region", region_list)
```
**[ADDED]**
```
53    fuel_list = ["ALL"] + sorted(df['Fuel_Type'].dropna().unique().tolist())
54    selected_fuel = st.sidebar.selectbox("Fuel Type", fuel_list)
```
**[REMOVED]**
```
(from line ~56)
##Applying filters

```
**[ADDED]**
```
56    sales_list = ["ALL"] + sorted(df['Sales_Classification'].dropna().unique().tolist())
57    selected_sales = st.sidebar.selectbox("Sales Classification", sales_list)
```
**[REMOVED]**
```
(from line ~59)
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

```
**[ADDED]**
```
59    min_mileage, max_mileage = int(df["Mileage_KM"].min()), int(df["Mileage_KM"].max())
60    mileage_range = st.sidebar.slider("Mileage Range (KM)", min_mileage, max_mileage, (min_mileage, max_mileage))
```
**[REMOVED]**
```
(from line ~62)
st.write("#### KPIs")
avg_sales_v=filtered["Sales_Volume"].mean()
avg_price =filtered["Price_USD"].mean()
mx_price =filtered["Price_USD"].max()

```
**[ADDED]**
```
62    # --- APPLY FILTERS ---
63    filtered = df.copy()
64    if selected_model != "ALL": filtered = filtered[filtered['Model'] == selected_model]
65    if selected_year != "ALL": filtered = filtered[filtered['Year'] == selected_year]
66    if selected_color != "ALL": filtered = filtered[filtered['Color'] == selected_color]
67    if selected_transmission != "ALL": filtered = filtered[filtered['Transmission'] == selected_transmission]
68    if selected_region != "ALL": filtered = filtered[filtered['Region'] == selected_region]
69    if selected_fuel != "ALL": filtered = filtered[filtered['Fuel_Type'] == selected_fuel]
70    if selected_sales != "ALL": filtered = filtered[filtered['Sales_Classification'] == selected_sales]
71    filtered = filtered[(filtered['Mileage_KM'] >= mileage_range[0]) & (filtered['Mileage_KM'] <= mileage_range[1])]
72    
73    # --- KPIs ---
74    avg_sales_v = filtered["Sales_Volume"].mean()
75    avg_price = filtered["Price_USD"].mean()
76    mx_price = filtered["Price_USD"].max()
```
**[REMOVED]**
```
(from line ~80)


```
**[REMOVED]**
```
(from line ~83)


```
**[REMOVED]**
```
(from line ~84)
region_counts = filtered["Region"].value_counts()



```
**[ADDED]**
```
85    
```
**[REMOVED]**
```
(from line ~87)
# --- Row 1: Financial and Volume KPIs (3 columns) ---

```
**[REMOVED]**
```
(from line ~88)


```
**[REMOVED]**
```
(from line ~89)
    st.metric(
        label="Average Sales Price (USD)",
        value=f"${avg_price:,.0f}", 
        delta=f"Max: ${mx_price:,.0f}" # Using delta to show the maximum price
    )


```
**[ADDED]**
```
89        st.metric("Avg Sales Price (USD)", f"${avg_price:,.0f}", delta=f"Max: ${mx_price:,.0f}")
```
**[REMOVED]**
```
(from line ~91)
    st.metric(
        label="Average Sales Volume",
        value=f"{avg_sales_v:.1f} units",
        delta="Per Listing"
    )


```
**[ADDED]**
```
91        st.metric("Avg Sales Volume", f"{avg_sales_v:.1f} units", delta="Per Listing")
```
**[REMOVED]**
```
(from line ~93)
    st.metric(
        label="Top Selling Model",
        # Access the index of the top_models Series to get the name
        value=top_models.index[0] if not top_models.empty else "N/A", 
        delta=f"In {top_region}"
    )

```
**[ADDED]**
```
93        st.metric("Top Selling Model", top_models.index[0] if not top_models.empty else "N/A", delta=f"In {top_region}")
```
**[REMOVED]**
```
(from line ~95)
st.markdown("---") # Separator line for visual clarity

# --- Row 2: Vehicle Condition and Technical Specs (4 columns) ---
st.write("#### 🚗 Vehicle Condition and Specs")

```
**[REMOVED]**
```
(from line ~96)


```
**[REMOVED]**
```
(from line ~97)
    st.metric(
        label="Avg. Mileage (KM)",
        value=f"{avg_mileage:,.0f}", 
        delta=f"Min: {min_mileage:,.0f} KM"
    )


```
**[ADDED]**
```
97        st.metric("Avg Mileage (KM)", f"{avg_mileage:,.0f}", delta=f"Min: {min_mileage:,.0f}")
```
**[REMOVED]**
```
(from line ~99)
    st.metric(
        label="Max Mileage (KM)",
        value=f"{max_mileage:,.0f}"
    )


```
**[ADDED]**
```
99        st.metric("Max Mileage (KM)", f"{max_mileage:,.0f}")
```
**[REMOVED]**
```
(from line ~101)
    st.metric(
        label="Avg. Engine Size (L)",
        value=f"{avg_engine_size:.2f} L"
    )


```
**[ADDED]**
```
101       st.metric("Avg Engine Size (L)", f"{avg_engine_size:.2f}")
```
**[REMOVED]**
```
(from line ~103)
    st.metric(
        label="Unique Engine Sizes",
        value=unique_engine_sizes,
        delta=f"Top Color: {top_colors.index[0] if not top_colors.empty else 'N/A'}"
    )
    
    
    ##charts
fig1= px.bar(filtered,x='Year', y='Sales_Volume')
st.write("### Sales VVolume  per Year")
st.plotly_chart(fig1,use_container_width=True)

```
**[ADDED]**
```
103       st.metric("Unique Engine Sizes", unique_engine_sizes, delta=f"Top Color: {top_colors.index[0] if not top_colors.empty else 'N/A'}")
```
**[REMOVED]**
```
(from line ~105)
fig2 =px.histogram(filtered,x="Price_USD",nbins=30, title=f"Price distribution in {selected_Region}")
st.write("### Price distribution per Region")
st.plotly_chart(fig2,use_container_width=True)

```
**[ADDED]**
```
105   st.markdown("---")
```
**[REMOVED]**
```
(from line ~107)
avg_price_year = filtered.groupby('Year')['Price_USD'].mean().reset_index()
fig = px.line(avg_price_year, x='Year', y='Price_USD', 
    title="Average Price Over Years", markers=True)
st.plotly_chart(fig, use_container_width=True)

```
**[ADDED]**
```
107   # --- CHARTS ---
108   st.write("### 📊 Sales Analytics")
109   
110   # Row 1: Sales Trends
111   c1, c2 = st.columns(2)
112   with c1:
113       sales_year = filtered.groupby('Year')['Sales_Volume'].sum().reset_index()
114       fig1 = px.line(sales_year, x='Year', y='Sales_Volume', markers=True, title="Total Sales Volume Over Years")
115       fig1.update_traces(line=dict(color="blue", width=3))
116       st.plotly_chart(fig1, use_container_width=True)
117   with c2:
118       price_year = filtered.groupby('Year')['Price_USD'].mean().reset_index()
119       fig2 = px.line(price_year, x='Year', y='Price_USD', markers=True, title="Average Price Over Years")
120       fig2.update_traces(line=dict(color="green", width=3))
121       st.plotly_chart(fig2, use_container_width=True)
122   
123   # Row 2: Distribution Charts
124   c3, c4 = st.columns(2)
125   with c3:
126       fig3 = px.histogram(filtered, x="Price_USD", nbins=30, color="Fuel_Type", title="Price Distribution by Fuel Type")
127       st.plotly_chart(fig3, use_container_width=True)
128   with c4:
129       fig4 = px.histogram(filtered, x="Mileage_KM", nbins=30, color="Transmission", title="Mileage Distribution by Transmission")
130       st.plotly_chart(fig4, use_container_width=True)
131   
132   # Row 3: Categorical Charts
133   c5, c6 = st.columns(2)
134   with c5:
135       region_sales = filtered.groupby("Region")["Sales_Volume"].sum().reset_index()
136       fig5 = px.bar(region_sales, x="Region", y="Sales_Volume", color="Region", title="Sales Volume by Region")
137       st.plotly_chart(fig5, use_container_width=True)
138   with c6:
139       color_sales = filtered.groupby("Color")["Sales_Volume"].sum().reset_index()
140       fig6 = px.pie(color_sales, names="Color", values="Sales_Volume", title="Sales by Car Color")
141       st.plotly_chart(fig6, use_container_width=True)
142   
143   # Row 4: Technical Specs
144   c7, c8 = st.columns(2)
145   with c7:
146       fig7 = px.box(filtered, x="Model", y="Price_USD", color="Model", title="Price Distribution per Model")
147       st.plotly_chart(fig7, use_container_width=True)
148   with c8:
149       fig8 = px.violin(filtered, x="Transmission", y="Mileage_KM", color="Transmission", box=True, points="all",
150                        title="Mileage Distribution by Transmission")
151       st.plotly_chart(fig8, use_container_width=True)
152   
153   # Row 5: Scatter Analysis
154   c9, c10 = st.columns(2)
155   with c9:
156       fig9 = px.scatter(filtered, x="Mileage_KM", y="Price_USD", color="Fuel_Type", size="Engine_Size_L",
157                         hover_data=["Model", "Year", "Region"], title="Price vs Mileage")
158       st.plotly_chart(fig9, use_container_width=True)
159   with c10:
160       fig10 = px.scatter(filtered, x="Price_USD", y="Sales_Volume", color="Region", size="Engine_Size_L",
161                          hover_data=["Model"], title="Sales Volume vs Price")
162       st.plotly_chart(fig10, use_container_width=True)
```

---

### 📄 c:\Users\Administrator\Desktop\BMW data visualization\app.py
*Saved at: 11/18/2025, 1:07:54 PM*

**[REMOVED]**
```
(from line ~167)
st.plotly_chart(fig2,use_container_width=True)
```
**[ADDED]**
```
167   st.plotly_chart(fig2,use_container_width=True)
168   
169   avg_price_year = filtered.groupby('Year')['Price_USD'].mean().reset_index()
170   fig = px.line(avg_price_year, x='Year', y='Price_USD', 
171       title="Average Price Over Years", markers=True)
172   st.plotly_chart(fig, use_container_width=True)
```

---

### 📄 c:\Users\Administrator\Desktop\BMW data visualization\app.py
*Saved at: 11/18/2025, 1:06:30 PM*

**[ADDED]**
```
162   st.write("### Sales VVolume  per Year")
```

---

### 📄 c:\Users\Administrator\Desktop\BMW data visualization\app.py
*Saved at: 11/18/2025, 1:05:43 PM*

**[ADDED]**
```
165   st.write("### Price distribution per Region")
```

---

### 📄 c:\Users\Administrator\Desktop\BMW data visualization\app.py
*Saved at: 11/18/2025, 1:04:30 PM*

**[REMOVED]**
```
(from line ~164)
fig2 =px.histogram(filtered,x="Price_USD",nbins=30, title=f"Price distribution in {Region   }")

```
**[ADDED]**
```
164   fig2 =px.histogram(filtered,x="Price_USD",nbins=30, title=f"Price distribution in {selected_Region}")
```

---

### 📄 c:\Users\Administrator\Desktop\BMW data visualization\app.py
*Saved at: 11/18/2025, 1:03:45 PM*

**[REMOVED]**
```
(from line ~164)
fig2 =px.histogram(filtered,x="Price_USD",nbins=30, title=f"Price distribution in {USD")

```
**[ADDED]**
```
164   fig2 =px.histogram(filtered,x="Price_USD",nbins=30, title=f"Price distribution in {Region   }")
```

---

### 📄 c:\Users\Administrator\Desktop\BMW data visualization\app.py
*Saved at: 11/18/2025, 1:03:11 PM*

**[REMOVED]**
```
(from line ~164)
fig2 =px.histogram(filtered,x="Price_USD",nbins=30, title="Price distribution in USD")

```
**[ADDED]**
```
164   fig2 =px.histogram(filtered,x="Price_USD",nbins=30, title=f"Price distribution in {USD")
```

---

### 📄 c:\Users\Administrator\Desktop\BMW data visualization\app.py
*Saved at: 11/18/2025, 1:01:52 PM*

**[REMOVED]**
```
(from line ~164)
fig2 =px.histogram(filtered,x="")
```
**[ADDED]**
```
164   fig2 =px.histogram(filtered,x="Price_USD",nbins=30, title="Price distribution in USD")
165   st.plotly_chart(fig2,use_container_width=True)
```

---

### 📄 c:\Users\Administrator\Desktop\BMW data visualization\app.py
*Saved at: 11/18/2025, 1:00:27 PM*

**[REMOVED]**
```
(from line ~162)
st.plotly_chart(fig1,use_container_width=True)
```
**[ADDED]**
```
162   st.plotly_chart(fig1,use_container_width=True)
163   
164   fig2 =px.histogram(filtered,x="")
```

---

### 📄 c:\Users\Administrator\Desktop\BMW data visualization\app.py
*Saved at: 11/18/2025, 12:59:43 PM*

**[REMOVED]**
```
(from line ~161)
fig1= px.bar_polar(filtered,x='Year', y='Sales_Volume')

```
**[ADDED]**
```
161   fig1= px.bar(filtered,x='Year', y='Sales_Volume')
```

---

### 📄 c:\Users\Administrator\Desktop\BMW data visualization\app.py
*Saved at: 11/18/2025, 12:59:21 PM*

**[REMOVED]**
```
(from line ~161)
fig1= px.line(filtered,x='Year', y='Sales_Volume')

```
**[ADDED]**
```
161   fig1= px.bar_polar(filtered,x='Year', y='Sales_Volume')
```

---

### 📄 c:\Users\Administrator\Desktop\BMW data visualization\app.py
*Saved at: 11/18/2025, 12:58:34 PM*

**[REMOVED]**
```
(from line ~161)
fig1= px.line_3d(filtered,x='Year', y='Sales_Volume')

```
**[ADDED]**
```
161   fig1= px.line(filtered,x='Year', y='Sales_Volume')
```

---

### 📄 c:\Users\Administrator\Desktop\BMW data visualization\app.py
*Saved at: 11/18/2025, 12:57:45 PM*

**[REMOVED]**
```
(from line ~161)
fig1= px.bar(filtered,x='Year', y='Sales_Volume')

```
**[ADDED]**
```
161   fig1= px.line_3d(filtered,x='Year', y='Sales_Volume')
```

---

### 📄 c:\Users\Administrator\Desktop\BMW data visualization\app.py
*Saved at: 11/18/2025, 12:56:46 PM*

**[REMOVED]**
```
(from line ~161)
fig1= px.bar(filtered,x='Year', y='Price_USD')

```
**[ADDED]**
```
161   fig1= px.bar(filtered,x='Year', y='Sales_Volume')
```

---

### 📄 c:\Users\Administrator\Desktop\BMW data visualization\app.py
*Saved at: 11/18/2025, 12:56:03 PM*

**[REMOVED]**
```
(from line ~161)
    c1=st.columns(1)
    with c1:
        fig1= px.bar(filtered,x='Year', y='Price_USD')
        st.plotly_chart(fig1,use_container_width=True)
```
**[ADDED]**
```
161   fig1= px.bar(filtered,x='Year', y='Price_USD')
162   st.plotly_chart(fig1,use_container_width=True)
```

---

### 📄 c:\Users\Administrator\Desktop\BMW data visualization\app.py
*Saved at: 11/18/2025, 12:55:37 PM*

**[REMOVED]**
```
(from line ~161)
    c1,c2,=st.columns(2)

```
**[ADDED]**
```
161       c1=st.columns(1)
```

---

### 📄 c:\Users\Administrator\Desktop\BMW data visualization\app.py
*Saved at: 11/18/2025, 12:55:13 PM*

**[REMOVED]**
```
(from line ~161)
    c1,c2,c3,c4,c5=st.columns(5)

```
**[ADDED]**
```
161       c1,c2,=st.columns(2)
```

---

### 📄 c:\Users\Administrator\Desktop\BMW data visualization\app.py
*Saved at: 11/18/2025, 12:54:31 PM*

**[REMOVED]**
```
(from line ~164)
        st.plotly_chart(fig1)
```
**[ADDED]**
```
164           st.plotly_chart(fig1,use_container_width=True)
```

---

### 📄 c:\Users\Administrator\Desktop\BMW data visualization\app.py
*Saved at: 11/18/2025, 12:52:32 PM*

**[REMOVED]**
```
(from line ~163)
        fig1= px.line(filtered,x='Year', y='Price_USD')

```
**[ADDED]**
```
163           fig1= px.bar(filtered,x='Year', y='Price_USD')
```

---

### 📄 c:\Users\Administrator\Desktop\BMW data visualization\app.py
*Saved at: 11/18/2025, 12:51:49 PM*

**[REMOVED]**
```
(from line ~163)
        fig1= px.line(filtered,x='Year', y='Price_USD', Color="red")

```
**[ADDED]**
```
163           fig1= px.line(filtered,x='Year', y='Price_USD')
```

---

### 📄 c:\Users\Administrator\Desktop\BMW data visualization\app.py
*Saved at: 11/18/2025, 12:51:29 PM*

**[REMOVED]**
```
(from line ~163)
        px.line(filtered,x='Year', y='Price_USD', Color="red")
        st.plotly_chart(c1)
```
**[ADDED]**
```
163           fig1= px.line(filtered,x='Year', y='Price_USD', Color="red")
164           st.plotly_chart(fig1)
```

---

### 📄 c:\Users\Administrator\Desktop\BMW data visualization\app.py
*Saved at: 11/18/2025, 12:51:08 PM*

**[REMOVED]**
```
(from line ~163)
        px.line(filtered,x='Year', y='' Color="red")
```
**[ADDED]**
```
163           px.line(filtered,x='Year', y='Price_USD', Color="red")
164           st.plotly_chart(c1)
```

---

### 📄 c:\Users\Administrator\Desktop\BMW data visualization\app.py
*Saved at: 11/18/2025, 12:50:39 PM*

**[REMOVED]**
```
(from line ~163)
        px.line(filtered,x='Price_USD', y= Color="red")
```
**[ADDED]**
```
163           px.line(filtered,x='Year', y='' Color="red")
```

---

### 📄 c:\Users\Administrator\Desktop\BMW data visualization\app.py
*Saved at: 11/18/2025, 12:50:07 PM*

**[REMOVED]**
```
(from line ~163)
        px.line(filtered,x= y= Color="red")
```
**[ADDED]**
```
163           px.line(filtered,x='Price_USD', y= Color="red")
```

---

### 📄 c:\Users\Administrator\Desktop\BMW data visualization\app.py
*Saved at: 11/18/2025, 12:49:23 PM*

**[REMOVED]**
```
(from line ~163)
        
```
**[ADDED]**
```
163           px.line(filtered,x= y= Color="red")
```

---

### 📄 c:\Users\Administrator\Desktop\BMW data visualization\app.py
*Saved at: 11/18/2025, 12:48:20 PM*

**[REMOVED]**
```
(from line ~161)
    c1,c2,c3,c4,c5
```
**[ADDED]**
```
161       c1,c2,c3,c4,c5=st.columns(5)
162       with c1:
163           
```

---

### 📄 c:\Users\Administrator\Desktop\BMW data visualization\app.py
*Saved at: 11/18/2025, 12:47:54 PM*

**[REMOVED]**
```
(from line ~161)
    
```
**[ADDED]**
```
161       c1,c2,c3,c4,c5
```

---

### 📄 c:\Users\Administrator\Desktop\BMW data visualization\app.py
*Saved at: 11/18/2025, 12:47:25 PM*

**[REMOVED]**
```
(from line ~157)
    )
```
**[ADDED]**
```
157       )
158       
159       
160       ##charts
161       
```

---

### 📄 c:\Users\Administrator\Desktop\BMW data visualization\app.py
*Saved at: 11/18/2025, 12:44:32 PM*

**[REMOVED]**
```
(from line ~87)
mx_price =filtered[Price_USD].max()

```
**[ADDED]**
```
87    mx_price =filtered["Price_USD"].max()
```

---

### 📄 c:\Users\Administrator\Desktop\BMW data visualization\app.py
*Saved at: 11/18/2025, 12:43:27 PM*

**[REMOVED]**
```
(from line ~100)
top_colors = filtered["Color"].value_counts().nlargest(3)
```
**[ADDED]**
```
100   top_colors = filtered["Color"].value_counts().nlargest(3)
101   st.write("#### 🔑 Key Performance Indicators")
102   # --- Row 1: Financial and Volume KPIs (3 columns) ---
103   col1, col2, col3 = st.columns(3)
104   
105   with col1:
106       st.metric(
107           label="Average Sales Price (USD)",
108           value=f"${avg_price:,.0f}", 
109           delta=f"Max: ${mx_price:,.0f}" # Using delta to show the maximum price
110       )
111   
112   with col2:
113       st.metric(
114           label="Average Sales Volume",
115           value=f"{avg_sales_v:.1f} units",
116           delta="Per Listing"
117       )
118   
119   with col3:
120       st.metric(
121           label="Top Selling Model",
122           # Access the index of the top_models Series to get the name
123           value=top_models.index[0] if not top_models.empty else "N/A", 
124           delta=f"In {top_region}"
125       )
126   
127   st.markdown("---") # Separator line for visual clarity
128   
129   # --- Row 2: Vehicle Condition and Technical Specs (4 columns) ---
130   st.write("#### 🚗 Vehicle Condition and Specs")
131   col4, col5, col6, col7 = st.columns(4)
132   
133   with col4:
134       st.metric(
135           label="Avg. Mileage (KM)",
136           value=f"{avg_mileage:,.0f}", 
137           delta=f"Min: {min_mileage:,.0f} KM"
138       )
139   
140   with col5:
141       st.metric(
142           label="Max Mileage (KM)",
143           value=f"{max_mileage:,.0f}"
144       )
145   
146   with col6:
147       st.metric(
148           label="Avg. Engine Size (L)",
149           value=f"{avg_engine_size:.2f} L"
150       )
151   
152   with col7:
153       st.metric(
154           label="Unique Engine Sizes",
155           value=unique_engine_sizes,
156           delta=f"Top Color: {top_colors.index[0] if not top_colors.empty else 'N/A'}"
157       )
```

---

### 📄 c:\Users\Administrator\Desktop\BMW data visualization\app.py
*Saved at: 11/18/2025, 12:42:53 PM*

**[REMOVED]**
```
(from line ~92)
# 2. Engine_Size_L Statistics

```
**[REMOVED]**
```
(from line ~96)
# B. Region Analysis
# Get the region with the highest sales volume

```
**[REMOVED]**
```
(from line ~99)
# C. Color Analysis
# Get the top 3 most popular colors

```
**[ADDED]**
```
99    
```

---

### 📄 c:\Users\Administrator\Desktop\BMW data visualization\app.py
*Saved at: 11/18/2025, 12:42:13 PM*

**[REMOVED]**
```
(from line ~94)
unique_engine_sizes = filtered["Engine_Size_L"].nunique()
```
**[ADDED]**
```
94    unique_engine_sizes = filtered["Engine_Size_L"].nunique()
95    top_models = filtered["Model"].value_counts().nlargest(5)
96    
97    # B. Region Analysis
98    # Get the region with the highest sales volume
99    top_region = filtered["Region"].value_counts().idxmax()
100   region_counts = filtered["Region"].value_counts()
101   
102   # C. Color Analysis
103   # Get the top 3 most popular colors
104   top_colors = filtered["Color"].value_counts().nlargest(3)
```

---

### 📄 c:\Users\Administrator\Desktop\BMW data visualization\app.py
*Saved at: 11/18/2025, 12:41:58 PM*

**[REMOVED]**
```
(from line ~87)
mx_price =filtered[Price_USD].max()
```
**[ADDED]**
```
87    mx_price =filtered[Price_USD].max()
88    avg_mileage = filtered["Mileage_KM"].mean()
89    min_mileage = filtered["Mileage_KM"].min()
90    max_mileage = filtered["Mileage_KM"].max()
91    
92    # 2. Engine_Size_L Statistics
93    avg_engine_size = filtered["Engine_Size_L"].mean()
94    unique_engine_sizes = filtered["Engine_Size_L"].nunique()
```

---

### 📄 c:\Users\Administrator\Desktop\BMW data visualization\app.py
*Saved at: 11/18/2025, 12:39:22 PM*

**[REMOVED]**
```
(from line ~86)
avg_price =filtered[""]
```
**[ADDED]**
```
86    avg_price =filtered["Price_USD"].mean()
87    mx_price =filtered[Price_USD].max()
```

---

### 📄 c:\Users\Administrator\Desktop\BMW data visualization\app.py
*Saved at: 11/18/2025, 12:38:28 PM*

**[ADDED]**
```
86    avg_price =filtered[""]
```

---

### 📄 c:\Users\Administrator\Desktop\BMW data visualization\app.py
*Saved at: 11/18/2025, 12:37:54 PM*

**[REMOVED]**
```
(from line ~85)
avg_sales_v=filtered["Sales_Volume"].mean()
```
**[ADDED]**
```
85    avg_sales_v=filtered["Sales_Volume"].mean()
```

---

### 📄 c:\Users\Administrator\Desktop\BMW data visualization\app.py
*Saved at: 11/18/2025, 12:37:41 PM*

**[REMOVED]**
```
(from line ~85)
avg_sales =filtered[""]
```
**[ADDED]**
```
85    avg_sales_v=filtered["Sales_Volume"].mean()
```

---

### 📄 c:\Users\Administrator\Desktop\BMW data visualization\app.py
*Saved at: 11/18/2025, 12:37:11 PM*

**[REMOVED]**
```
(from line ~84)
st.write("#### KPIs")
```
**[ADDED]**
```
84    st.write("#### KPIs")
85    avg_sales =filtered[""]
```

---

### 📄 c:\Users\Administrator\Desktop\BMW data visualization\app.py
*Saved at: 11/18/2025, 12:36:37 PM*

**[REMOVED]**
```
(from line ~82)
filtered =filtered[(filtered['Mileage_KM'] >=mileage_range[0]) & (filtered['Mileage_KM'] >=mileage_range[0]) ]
```
**[ADDED]**
```
82    filtered =filtered[(filtered['Mileage_KM'] >=mileage_range[0]) & (filtered['Mileage_KM'] >=mileage_range[0]) ]
83    
84    st.write("#### KPIs")
```

---

### 📄 c:\Users\Administrator\Desktop\BMW data visualization\app.py
*Saved at: 11/18/2025, 12:35:15 PM*

**[REMOVED]**
```
(from line ~74)
if selected_Regionr !="ALL":

```
**[ADDED]**
```
74    if selected_Region!="ALL":
```

---

### 📄 c:\Users\Administrator\Desktop\BMW data visualization\app.py
*Saved at: 11/18/2025, 12:34:59 PM*

**[REMOVED]**
```
(from line ~82)
filtered =filtered[(filtered['Mileage_KM'] >=mileage_range[0]) & ]
```
**[ADDED]**
```
82    filtered =filtered[(filtered['Mileage_KM'] >=mileage_range[0]) & (filtered['Mileage_KM'] >=mileage_range[0]) ]
```

---

### 📄 c:\Users\Administrator\Desktop\BMW data visualization\app.py
*Saved at: 11/18/2025, 12:34:08 PM*

**[REMOVED]**
```
(from line ~80)
    filtered =filtered[filtered['Sales_Classification']== selected_Sales]
```
**[ADDED]**
```
80        filtered =filtered[filtered['Sales_Classification']== selected_Sales]
81        
82    filtered =filtered[(filtered['Mileage_KM'] >=mileage_range[0]) & ]
```

---

### 📄 c:\Users\Administrator\Desktop\BMW data visualization\app.py
*Saved at: 11/18/2025, 12:32:40 PM*

**[REMOVED]**
```
(from line ~57)
selected_Sales=st.sidebar.selectbox(" Sales_Classification", Sales)
```
**[ADDED]**
```
57    selected_Sales=st.sidebar.selectbox(" Sales_Classification", Sales)
58    
59    
60    ##Applying filters
61    
62    filtered =df.copy()
63    if selected_model !="ALL":
64        filtered =filtered[filtered['Model']== selected_model]
65        
66    if selected_year !="ALL":
67        filtered =filtered[filtered['Year']== selected_year]
68        
69    if selected_Color !="ALL":
70        filtered =filtered[filtered['Color']== selected_Color]
71        
72    if selected_Transmission !="ALL":
73        filtered =filtered[filtered['Transmission']== selected_Transmission]
74    if selected_Regionr !="ALL":
75        filtered =filtered[filtered['Region']== selected_Region]
76        
77    if selected_Fuel_Type!="ALL":
78        filtered =filtered[filtered['Fuel_Type']== selected_Fuel_Type]
79    if selected_Sales!="ALL":
80        filtered =filtered[filtered['Sales_Classification']== selected_Sales]
```

---

### 📄 c:\Users\Administrator\Desktop\BMW data visualization\app.py
*Saved at: 11/18/2025, 12:25:30 PM*

**[REMOVED]**
```
(from line ~56)
Fuel_Type =["ALL"] +sorted(df['Fuel_Type'].dropna().unique().tolist())
selected_Fuel_Type=st.sidebar.selectbox(" Sales_Classification", Fuel_Type)
```
**[ADDED]**
```
56    Sales =["ALL"] +sorted(df['Sales_Classification'].dropna().unique().tolist())
57    selected_Sales=st.sidebar.selectbox(" Sales_Classification", Sales)
```

---

### 📄 c:\Users\Administrator\Desktop\BMW data visualization\app.py
*Saved at: 11/18/2025, 12:24:54 PM*

**[REMOVED]**
```
(from line ~57)
selected_Fuel_Type=st.sidebar.selectbox(" Fuel_Type", Fuel_Type)
```
**[ADDED]**
```
57    selected_Fuel_Type=st.sidebar.selectbox(" Sales_Classification", Fuel_Type)
```

---

### 📄 c:\Users\Administrator\Desktop\BMW data visualization\app.py
*Saved at: 11/18/2025, 12:24:38 PM*

**[REMOVED]**
```
(from line ~55)
mileage_range =st.sidebar.slider("Mileage Range",min_mileage,max_mileage,(min_mileage,max_mileage))
```
**[ADDED]**
```
55    mileage_range =st.sidebar.slider("Mileage Range",min_mileage,max_mileage,(min_mileage,max_mileage))
56    Fuel_Type =["ALL"] +sorted(df['Fuel_Type'].dropna().unique().tolist())
57    selected_Fuel_Type=st.sidebar.selectbox(" Fuel_Type", Fuel_Type)
```

---

### 📄 c:\Users\Administrator\Desktop\BMW data visualization\app.py
*Saved at: 11/18/2025, 12:23:30 PM*

**[REMOVED]**
```
(from line ~52)
selected_Fuel_Type=st.sidebar.selectbox(" Fuel_Type", Fuel_Type)
```
**[ADDED]**
```
52    selected_Fuel_Type=st.sidebar.selectbox(" Fuel_Type", Fuel_Type)
53    
54    min_mileage, max_mileage=int(df["Mileage_KM"].min()), int(df["Mileage_KM"].max())
55    mileage_range =st.sidebar.slider("Mileage Range",min_mileage,max_mileage,(min_mileage,max_mileage))
```

---

### 📄 c:\Users\Administrator\Desktop\BMW data visualization\app.py
*Saved at: 11/18/2025, 12:20:21 PM*

**[REMOVED]**
```
(from line ~51)
Region =["ALL"] +sorted(df['Region'].dropna().unique().tolist())
selected_Region=st.sidebar.selectbox(" Region", Region)
```
**[ADDED]**
```
51    Fuel_Type =["ALL"] +sorted(df['Fuel_Type'].dropna().unique().tolist())
52    selected_Fuel_Type=st.sidebar.selectbox(" Fuel_Type", Fuel_Type)
```

---

### 📄 c:\Users\Administrator\Desktop\BMW data visualization\app.py
*Saved at: 11/18/2025, 12:19:52 PM*

**[ADDED]**
```
50    selected_Region=st.sidebar.selectbox(" Region", Region)
51    Region =["ALL"] +sorted(df['Region'].dropna().unique().tolist())
```

---

### 📄 c:\Users\Administrator\Desktop\BMW data visualization\app.py
*Saved at: 11/18/2025, 12:19:40 PM*

**[REMOVED]**
```
(from line ~49)
Transmission =["ALL"] +sorted(df['Transmission'].dropna().unique().tolist())
selected_Transmission =st.sidebar.selectbox(" Transmission", Transmission)
```
**[ADDED]**
```
49    Region =["ALL"] +sorted(df['Region'].dropna().unique().tolist())
50    selected_Region=st.sidebar.selectbox(" Region", Region)
```

---

### 📄 c:\Users\Administrator\Desktop\BMW data visualization\app.py
*Saved at: 11/18/2025, 12:19:11 PM*

**[ADDED]**
```
49    Transmission =["ALL"] +sorted(df['Transmission'].dropna().unique().tolist())
50    selected_Transmission =st.sidebar.selectbox(" Transmission", Transmission)
```

---

### 📄 c:\Users\Administrator\Desktop\BMW data visualization\app.py
*Saved at: 11/18/2025, 12:19:06 PM*

**[REMOVED]**
```
(from line ~48)
selected_Color =st.sidebar.selectbox(" Transmission", Transmission)

```
**[ADDED]**
```
48    selected_Transmission =st.sidebar.selectbox(" Transmission", Transmission)
```

---

### 📄 c:\Users\Administrator\Desktop\BMW data visualization\app.py
*Saved at: 11/18/2025, 12:18:58 PM*

**[REMOVED]**
```
(from line ~47)
Color =["ALL"] +sorted(df['Color'].dropna().unique().tolist())
selected_Color =st.sidebar.selectbox(" Color", Color)

```
**[ADDED]**
```
47    Transmission =["ALL"] +sorted(df['Transmission'].dropna().unique().tolist())
48    selected_Color =st.sidebar.selectbox(" Transmission", Transmission)
```

---

### 📄 c:\Users\Administrator\Desktop\BMW data visualization\app.py
*Saved at: 11/18/2025, 12:18:38 PM*

**[REMOVED]**
```
(from line ~46)
selected_Color =st.sidebar.selectbox("BMW Color", Color)

```
**[ADDED]**
```
46    selected_Color =st.sidebar.selectbox(" Color", Color)
47    Color =["ALL"] +sorted(df['Color'].dropna().unique().tolist())
48    selected_Color =st.sidebar.selectbox(" Color", Color)
```

---

### 📄 c:\Users\Administrator\Desktop\BMW data visualization\app.py
*Saved at: 11/18/2025, 12:18:14 PM*

**[REMOVED]**
```
(from line ~46)
selected_Color =st.sidebar.selectbox("BMW Models", Color)

```
**[ADDED]**
```
46    selected_Color =st.sidebar.selectbox("BMW Color", Color)
```

---

### 📄 c:\Users\Administrator\Desktop\BMW data visualization\app.py
*Saved at: 11/18/2025, 12:18:00 PM*

**[REMOVED]**
```
(from line ~45)
model =["ALL"] +sorted(df['Model'].dropna().unique().tolist())
selected_model =st.sidebar.selectbox("BMW Models", model)

```
**[ADDED]**
```
45    Color =["ALL"] +sorted(df['Color'].dropna().unique().tolist())
46    selected_Color =st.sidebar.selectbox("BMW Models", Color)
```

---

### 📄 c:\Users\Administrator\Desktop\BMW data visualization\app.py
*Saved at: 11/18/2025, 12:17:33 PM*

**[ADDED]**
```
45    model =["ALL"] +sorted(df['Model'].dropna().unique().tolist())
46    selected_model =st.sidebar.selectbox("BMW Models", model)
```

---

### 📄 c:\Users\Administrator\Desktop\BMW data visualization\app.py
*Saved at: 11/18/2025, 12:17:10 PM*

**[REMOVED]**
```
(from line ~42)
selected_model =st.sidebar.selectbox("BMW Models", model)

```
**[ADDED]**
```
42    selected_model =st.sidebar.selectbox("BMW MODEL", model)
43    year =["ALL"] +sorted(df['Year'].dropna().unique().tolist())
44    selected_year =st.sidebar.selectbox("YEAR", year)
```

---

### 📄 c:\Users\Administrator\Desktop\BMW data visualization\app.py
*Saved at: 11/18/2025, 12:15:35 PM*

**[REMOVED]**
```
(from line ~40)
st.sidebar.header("Filter Section")

```
**[ADDED]**
```
40    st.sidebar.header("BMW Filter Section")
```
**[REMOVED]**
```
(from line ~42)
selected_model =st.sidebar.selectbox("Models", model)

```
**[ADDED]**
```
42    selected_model =st.sidebar.selectbox("BMW Models", model)
```

---

### 📄 c:\Users\Administrator\Desktop\BMW data visualization\app.py
*Saved at: 11/18/2025, 12:14:57 PM*

**[ADDED]**
```
42    selected_model =st.sidebar.selectbox("Models", model)
```

---

### 📄 c:\Users\Administrator\Desktop\BMW data visualization\app.py
*Saved at: 11/18/2025, 12:13:45 PM*

**[REMOVED]**
```
(from line ~41)
model =["ALL"] +sorted(df[''])

```
**[ADDED]**
```
41    model =["ALL"] +sorted(df['Model'].dropna().unique().tolist())
```

---

### 📄 c:\Users\Administrator\Desktop\BMW data visualization\app.py
*Saved at: 11/18/2025, 12:13:12 PM*

**[REMOVED]**
```
(from line ~41)


```
**[ADDED]**
```
41    model =["ALL"] +sorted(df[''])
```

---

### 📄 c:\Users\Administrator\Desktop\BMW data visualization\app.py
*Saved at: 11/18/2025, 12:12:14 PM*

**[ADDED]**
```
41    
```

---

### 📄 c:\Users\Administrator\Desktop\BMW data visualization\app.py
*Saved at: 11/18/2025, 12:11:53 PM*

**[REMOVED]**
```
(from line ~6)
st.set_page_config(page_title="BMW SALES", layout="wide")

```
**[ADDED]**
```
6     st.set_page_config(
7         page_title="Dashboard",
8         layout="wide",
9         initial_sidebar_state="expanded"
10    )
11    
12    st.markdown(
13        """
14        <style>
15        /* Hide hamburger menu and footer */
16        header {visibility: hidden;}
17        footer {visibility: hidden;}
18        button[title="Toggle sidebar"] {display: none;}
19        </style>
20        """,
21        unsafe_allow_html=True
22    )
23    
```

---

### 📄 c:\Users\Administrator\Desktop\BMW data visualization\app.py
*Saved at: 11/18/2025, 12:10:50 PM*

**[REMOVED]**
```
(from line ~18)
df =load_data("BMW_Sales.csv")
```
**[ADDED]**
```
18    df =load_data("BMW_Sales.csv")
19    
20    
21    ##side bar stuff
22    
23    st.sidebar.header("Filter Section")
```

---

### 📄 c:\Users\Administrator\Desktop\BMW data visualization\app.py
*Saved at: 11/18/2025, 12:09:56 PM*

**[REMOVED]**
```
(from line ~14)
    df =pd_read_csv(path)

```
**[ADDED]**
```
14        df =pd.read_csv(path)
```

---

### 📄 c:\Users\Administrator\Desktop\BMW data visualization\app.py
*Saved at: 11/18/2025, 12:09:42 PM*

**[REMOVED]**
```
(from line ~18)
df =pd.load_data("BMW_Sales.csv")
```
**[ADDED]**
```
18    df =load_data("BMW_Sales.csv")
```

---

### 📄 c:\Users\Administrator\Desktop\BMW data visualization\app.py
*Saved at: 11/18/2025, 12:08:51 PM*

**[REMOVED]**
```
(from line ~18)

df =load_data("BMW")
```
**[ADDED]**
```
18    df =pd.load_data("BMW_Sales.csv")
```

---

### 📄 c:\Users\Administrator\Desktop\BMW data visualization\app.py
*Saved at: 11/18/2025, 12:08:28 PM*

**[ADDED]**
```
10    ##caching data 
11    
12    @st.cache_data
13    def load_data(path):
14        df =pd_read_csv(path)
15        return df 
16    
17    
18    
19    df =load_data("BMW")
```

---

### 📄 c:\Users\Administrator\Desktop\BMW data visualization\app.py
*Saved at: 11/18/2025, 12:06:56 PM*

**[REMOVED]**
```
(from line ~8)
St.write("Welcome to the Rack Visuals")

```
**[ADDED]**
```
8     st.write("Welcome to the Rack Visuals")
```

---

### 📄 c:\Users\Administrator\Desktop\BMW data visualization\app.py
*Saved at: 11/18/2025, 12:06:23 PM*

**[REMOVED]**
```
(from line ~6)
st.set_page_config(page_title="BMW SALES")
```
**[ADDED]**
```
6     st.set_page_config(page_title="BMW SALES", layout="wide")
7     st.title("BMW Sales From 2010 - 2024 ")
8     St.write("Welcome to the Rack Visuals")
9     
```

---

### 📄 c:\Users\Administrator\Desktop\BMW data visualization\app.py
*Saved at: 11/18/2025, 11:58:59 AM*

**[ADDED]**
```
1     import streamlit as st    
2     import pandas as pd 
3     import plotly.express as px 
4     import numpy as np 
5     
6     st.set_page_config(page_title="BMW SALES")
```

---

