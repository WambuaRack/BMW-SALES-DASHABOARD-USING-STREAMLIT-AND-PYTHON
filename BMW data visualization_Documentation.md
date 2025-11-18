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

