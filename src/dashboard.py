import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def render_dashboard(current_df):
    st.title("📊 BookPulse Analytics Dashboard")
    st.subheader("Real-Time Multi-Platform E-Book Price Aggregator")
    st.markdown("---")

    if current_df.empty:
        st.warning("No data available. Please trigger a search via main.py first.")
        return

    # 1. Metric Display (Top KPI Cards)
    st.markdown("### ⚡ Today's Live Deals")
    cols = st.columns(len(current_df))
    for idx, row in current_df.iterrows():
        with cols[idx]:
            st.metric(
                label=f"📍 {row['platform'].upper()}", 
                value=f"₹{row['current_price']}", 
                delta=f"{row['discount_pct']}% Off",
                delta_color="normal"
            )
    st.markdown("---")

    # Layout Setup: 2 Columns for side-by-side charts
    col1, col2 = st.columns(2)

    with col1:
        # Chart 1: Seaborn Bar Chart (Price Comparison)
        st.markdown("#### 💵 Price Comparison Across Platforms")
        fig1, ax1 = plt.subplots(figsize=(5, 3.5))
        sns.barplot(x='platform', y='current_price', data=current_df, palette='YlGnBu_r', ax=ax1)
        ax1.set_ylabel("Price (₹)", fontsize=10)
        ax1.set_xlabel("Platform", fontsize=10)
        plt.xticks(rotation=15)
        st.pyplot(fig1)

    with col2:
        # Chart 2: Matplotlib Donut Chart (Discount Share Analysis)
        st.markdown("#### 🎯 Discount Distribution Value")
        fig2, ax2 = plt.subplots(figsize=(5, 3.5))
        
        labels = current_df['platform'].tolist()
        sizes = current_df['discount_pct'].tolist()
        
        if sum(sizes) == 0:
            sizes = [1] * len(labels)  # Equal split if no discount
        
        colors = sns.color_palette('pastel')[0:len(labels)]
        
        ax2.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, colors=colors, 
                wedgeprops=dict(width=0.4, edgecolor='w'))
        ax2.axis('equal')  
        st.pyplot(fig2)

    st.markdown("---")
    
    # 3. Chart 3: Horizontal Value Plot (Smart Savings Insight)
    st.markdown("#### 💡 Potential Savings Spectrum")
    fig3, ax3 = plt.subplots(figsize=(10, 2.5))
    
    sns.scatterplot(x='current_price', y='platform', data=current_df, hue='platform', 
                    palette='coolwarm', s=300, marker='D', ax=ax3, legend=False)
    
    min_price_row = current_df.loc[current_df['current_price'].idxmin()]
    ax3.axvline(x=min_price_row['current_price'], color='red', linestyle='--', alpha=0.6, 
                label=f"Best Deal: ₹{min_price_row['current_price']} ({min_price_row['platform']})")
    
    ax3.set_xlabel("Price (₹)")
    ax3.set_ylabel("Platform")
    ax3.legend(loc="upper right")
    st.pyplot(fig3)

    # 4. Tabular Data View
    with st.expander("🔍 View Raw Extracted Sheet"):
        st.dataframe(current_df, use_container_width=True)