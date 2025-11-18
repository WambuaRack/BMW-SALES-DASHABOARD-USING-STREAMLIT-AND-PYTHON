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

