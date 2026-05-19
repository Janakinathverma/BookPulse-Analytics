import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import sqlite3

def load_historical_data():
    try:
        conn = sqlite3.connect("data_history.db")
        df = pd.read_sql_query("SELECT * FROM price_history", conn)
        conn.close()
        return df
    except Exception:
        return pd.DataFrame()

def render_dashboard(current_df):
    st.title("📊 BookPulse Analytics")
    st.subheader("Real-Time Multi-Platform E-Book Price Aggregator")

    if current_df.empty:
        st.warning("Koi data available nahi hai. Pehle main.py se search chalao.")
        return

    # Metric Display
    st.markdown("### Today's Deals")
    cols = st.columns(len(current_df))
    for idx, row in current_df.iterrows():
        with cols[idx]:
            st.metric(label=f"{row['platform']}", value=f"₹{row['current_price']}", delta=f"{row['discount_pct']}% Off")

    # Seaborn Bar Chart
    st.markdown("### Price Comparison Across Platforms")
    fig, ax = plt.subplots(figsize=(6, 3.5))
    sns.barplot(x='platform', y='current_price', data=current_df, palette='Blues_d', ax=ax)
    ax.set_ylabel("Price (₹)")
    ax.set_xlabel("Platform")
    st.pyplot(fig)

    # Historical Data Section
    st.markdown("---")
    st.markdown("### 📜 Search History Log (From SQLite)")
    history_df = load_historical_data()
    if not history_df.empty:
        st.dataframe(history_df.tail(10), use_container_width=True)