# utils/charts.py
import plotly.express as px

def plot_sales_table(df):
    return df.style.format({"amount": "${:,.2f}"}).hide_index()

def plot_sales_by_product(df):
    fig = px.bar(
        df.groupby("product").amount.sum().reset_index(),
        x="product", y="amount", text_auto=True,
        title="Total Sales by Product"
    )
    fig.update_layout(xaxis_title="", yaxis_title="USD")
    return fig
