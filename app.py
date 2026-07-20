import streamlit as st
from pathlib import Path
import pandas as pd
import streamlit as st

@st.cache_data
def load_data():
    file_path = Path(__file__).parent.parent / "data" / "sales_data_clean.csv"

    df = pd.read_csv(
        file_path,
        sheet_name="sales_data_clean"
    )

from utils.loader import load_data
from utils.metrics import calculate_metrics
from utils.charts import (
    monthly_sales,
    sales_by_country,
    product_sales
)

st.set_page_config(
    page_title="Sales Dashboard",
    layout="wide"
)

st.title("📊 Executive Sales Dashboard")

df = load_data()

# -----------------------------
# Sidebar Filters
# -----------------------------

st.sidebar.header("Filters")

year = st.sidebar.multiselect(
    "Year",
    sorted(df["YEAR_ID"].unique()),
    default=sorted(df["YEAR_ID"].unique())
)

country = st.sidebar.multiselect(
    "Country",
    sorted(df["COUNTRY"].unique()),
    default=sorted(df["COUNTRY"].unique())
)

product = st.sidebar.multiselect(
    "Product Line",
    sorted(df["PRODUCTLINE"].unique()),
    default=sorted(df["PRODUCTLINE"].unique())
)

status = st.sidebar.multiselect(
    "Order Status",
    sorted(df["STATUS"].unique()),
    default=sorted(df["STATUS"].unique())
)

filtered = df[
    (df["YEAR_ID"].isin(year))
    &
    (df["COUNTRY"].isin(country))
    &
    (df["PRODUCTLINE"].isin(product))
    &
    (df["STATUS"].isin(status))
]

metrics = calculate_metrics(filtered)

# -----------------------------
# KPI Cards
# -----------------------------

c1, c2, c3, c4, c5, c6 = st.columns(6)

c1.metric(
    "Sales",
    f"${metrics['Total Sales']:,.2f}"
)

c2.metric(
    "Orders",
    metrics["Total Orders"]
)

c3.metric(
    "Customers",
    metrics["Customers"]
)

c4.metric(
    "Quantity",
    metrics["Quantity"]
)

c5.metric(
    "Average Order",
    f"${metrics['Average Order']:,.2f}"
)

c6.metric(
    "Average Price",
    f"${metrics['Average Price']:,.2f}"
)

st.divider()

# -----------------------------
# Charts
# -----------------------------

left, right = st.columns(2)

with left:
    st.plotly_chart(
        monthly_sales(filtered),
        use_container_width=True
    )

with right:
    st.plotly_chart(
        sales_by_country(filtered),
        use_container_width=True
    )

st.plotly_chart(
    product_sales(filtered),
    use_container_width=True
)

st.divider()

# -----------------------------
# Data Table
# -----------------------------

st.subheader("Sales Data")

st.dataframe(
    filtered,
    use_container_width=True
)

csv = filtered.to_csv(index=False).encode("utf-8")

st.download_button(
    "Download Filtered Data",
    csv,
    "sales.csv",
    "text/csv"
)
