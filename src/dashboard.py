import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def render_dashboard(current_df):
    st.title("📊 BookPulse Analytics")
    st.subheader("Real-Time Multi-Platform E-Book Price Aggregator")

    if current_df.empty:
        st.warning("Koi data available nahi hai. Pehle main.py se search chalao.")
        return

    # Metric Display (Har platform ki live details dikhane ke liye)
    st.markdown("### Today's Deals")
    cols = st.columns(len(current_df))
    for idx, row in current_df.iterrows():
        with cols[idx]:
            st.metric(
                label=f"{row['platform']}", 
                value=f"₹{row['current_price']}", 
                delta=f"{row['discount_pct']}% Off"
            )

    # Seaborn Bar Chart (Live data ka graphical representation)
    st.markdown("### Price Comparison Across Platforms")
    fig, ax = plt.subplots(figsize=(6, 3.5))
    sns.barplot(x='platform', y='current_price', data=current_df, palette='Blues_d', ax=ax)
    ax.set_ylabel("Price (₹)")
    ax.set_xlabel("Platform")
    st.pyplot(fig)