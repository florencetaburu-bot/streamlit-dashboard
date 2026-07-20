import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Sales Dashboard",layout="wide")
@st.cache_data
def load():
    return pd.read_csv("data/sales_data_clean.csv",parse_dates=["ORDERDATE"])
df=load()

st.sidebar.header("Filters")
years=sorted(df["YEAR_ID"].unique())
sel=st.sidebar.multiselect("Year",years,default=years)
df=df[df["YEAR_ID"].isin(sel)]

rev=df["SALES"].sum()
orders=df["ORDERNUMBER"].nunique()
cust=df["CUSTOMERNAME"].nunique()
qty=df["QUANTITYORDERED"].sum()
aov=rev/orders if orders else 0

c1,c2,c3,c4,c5=st.columns(5)
for c,t,v in [(c1,"Revenue",f"${rev:,.0f}"),(c2,"Orders",orders),(c3,"Customers",cust),(c4,"Qty",qty),(c5,"Avg Order",f"${aov:,.2f}")]:
    c.metric(t,v)

m=df.groupby("MONTH_ID",as_index=False)["SALES"].sum()
st.plotly_chart(px.line(m,x="MONTH_ID",y="SALES",title="Monthly Sales"),use_container_width=True)
col1,col2=st.columns(2)
pl=df.groupby("PRODUCTLINE",as_index=False)["SALES"].sum().sort_values("SALES")
col1.plotly_chart(px.bar(pl,x="SALES",y="PRODUCTLINE",orientation="h",title="Sales by Product Line"),use_container_width=True)
ct=df.groupby("COUNTRY",as_index=False)["SALES"].sum().sort_values("SALES")
col2.plotly_chart(px.bar(ct,x="SALES",y="COUNTRY",orientation="h",title="Sales by Country"),use_container_width=True)
