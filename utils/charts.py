import plotly.express as px


def monthly_sales(df):
    monthly = (
        df.groupby("MONTH_ID")["SALES"]
        .sum()
        .reset_index()
    )
    fig = px.line(
        monthly,
        x="MONTH_ID",
        y="SALES",
        markers=True,
        title="Monthly Sales"
    )
    return fig

def sales_by_country(df):
    country = (
        df.groupby("COUNTRY")["SALES"]
        .sum()
        .reset_index()
    )
    fig = px.bar(
        country,
        x="COUNTRY",
        y="SALES",
        color="SALES",
        title="Sales by Country"
    )
    return fig

def product_sales(df):
    product = (
        df.groupby("PRODUCTLINE")["SALES"]
        .sum()
        .reset_index()
    )

    fig = px.bar(
        product,
        x="PRODUCTLINE",
        y="SALES",
        color="PRODUCTLINE",
        title="Sales by Product Line"
    )

    return fig
