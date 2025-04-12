import streamlit as st
import pandas as pd
import plotly.express as px
from utils.db import get_latest_sales
from utils.cdc_simulator import simulate_cdc
import streamlit_authenticator as stauth
from yaml import safe_load

# ✅ WAJIB: Page config harus paling atas sebelum komponen lainnya
st.set_page_config(page_title="DataPulse: Real-Time CDC Dashboard", layout="wide")

# --- Auth setup
with open("config/credentials.yaml") as file:
    config = safe_load(file)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days']
)

# ✅ Fix login call
authenticator.login(location="main")

if st.session_state["authentication_status"] is False:
    st.error("Incorrect username or password")
elif st.session_state["authentication_status"] is None:
    st.warning("Please enter your username and password")
elif st.session_state["authentication_status"]:
    # --- Sidebar
    st.sidebar.title("⚙️ CDC Simulation")
    if st.sidebar.button("Simulate New Sale"):
        simulate_cdc()
        st.sidebar.success("✅ New sale inserted!")

    # --- Main title
    st.title("📈 DataPulse: Real-Time CDC Dashboard Demo")
    st.caption("Simulate CDC updates into a Snowflake-style warehouse and monitor sales metrics in real-time.")

    # --- Load and prepare data
    df = get_latest_sales()
    df['created_at'] = pd.to_datetime(df['created_at'])  # ✅ convert first

    # --- Filters
    st.sidebar.subheader("📊 Filters")
    selected_product = st.sidebar.selectbox("Filter by Product", ["All"] + df['product'].unique().tolist())
    date_range = st.sidebar.date_input("Filter by Date Range", [])

    if selected_product != "All":
        df = df[df['product'] == selected_product]
    if len(date_range) == 2:
        df = df[(df['created_at'] >= pd.to_datetime(date_range[0])) & (df['created_at'] <= pd.to_datetime(date_range[1]))]

    # --- Summary
    st.subheader("📊 Summary")
    total_revenue = df['amount'].sum()
    top_product = df.groupby('product')['amount'].sum().idxmax() if not df.empty else "-"
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Records", len(df))
    col2.metric("Total Revenue", f"${total_revenue:,.2f}")
    col3.metric("Top Product", top_product)

    # --- Charts
    st.subheader("📦 Revenue by Product")
    fig_bar = px.bar(df.groupby('product')['amount'].sum().reset_index(), x="product", y="amount", labels={'amount': 'USD'}, text_auto=True)
    st.plotly_chart(fig_bar, use_container_width=True)

    st.subheader("📈 Revenue Over Time")
    df['date'] = pd.to_datetime(df['created_at']).dt.date
    daily = df.groupby("date")["amount"].sum().reset_index()
    fig_line = px.line(daily, x="date", y="amount", markers=True)
    st.plotly_chart(fig_line, use_container_width=True)

    st.subheader("🥧 Product Contribution")
    fig_pie = px.pie(df, values="amount", names="product", title="Sales Share by Product")
    st.plotly_chart(fig_pie, use_container_width=True)

    # --- Table
    st.subheader("🧾 Latest Sales Records")
    st.dataframe(df.sort_values(by="created_at", ascending=False).reset_index(drop=True))

    # --- Export
    st.download_button("📥 Export to CSV", df.to_csv(index=False), file_name="sales_data.csv", use_container_width=True)

    # --- Logout
    authenticator.logout(location="sidebar")
