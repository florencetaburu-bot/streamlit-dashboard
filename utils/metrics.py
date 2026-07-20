import pandas as pd


def calculate_metrics(df):
    metrics = {
        "Total Sales": df["SALES"].sum(),
        "Total Orders": df["ORDERNUMBER"].nunique(),
        "Customers": df["CUSTOMERNAME"].nunique(),
        "Quantity": df["QUANTITYORDERED"].sum(),
        "Average Order":
            df.groupby("ORDERNUMBER")["SALES"].sum().mean(),
        "Average Price":
            df["PRICEEACH"].mean()
    }

    return metrics
