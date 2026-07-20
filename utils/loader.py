import pandas as pd
import streamlit as st


@st.cache_data
def load_data():

    df = pd.read_excel(
        "data/sales_data_clean.xlsx",
        sheet_name="sales_data_clean"
    )

    df["ORDERDATE"] = pd.to_datetime(df["ORDERDATE"])

    return df
