import os
import subprocess
import sys

def launch_local_server():
    print("====================================================")
    print("📚 BookPulse Analytics: Launching Unified UI...")
    print("====================================================")
    current_script = __file__
    try:
        print("🚀 Starting Streamlit Server... Browser window open ho rahi hai.")
        subprocess.run([sys.executable, "-m", "streamlit", "run", current_script], check=True)
    except KeyboardInterrupt:
        print("\n👋 BookPulse Analytics Server stopped by user. See you again!")
    except Exception as e:
        print(f"❌ Error while launching the UI: {e}")
    sys.exit(0)


# =========================================================================
# 🔄 MAIN EXECUTION ROUTER (Fixes the Session State Warning)
# =========================================================================
import streamlit as st

if not st.runtime.exists():
    # Agar bina 'streamlit run' ke chal raha hai, toh pehle server launch karo aur script roko
    launch_local_server()
else:
    # Agar Streamlit server ke andar chal raha hai, tabhi baaki code execute hoga
    import pandas as pd

    # System paths configure karna
    sys.path.append(os.path.dirname(os.path.abspath(__file__)))

    try:
        from src.scraper import fetch_all_prices
        from src.pipeline import clean_data, log_to_database
        from src.dashboard import render_dashboard
    except ImportError:
        pass

    # 1. Page Configuration
    st.set_page_config(
        page_title="BookPulse Analytics", 
        page_icon="📚", 
        layout="wide"
    )

    # 2. Session State Initialization
    if "current_df" not in st.session_state:
        st.session_state.current_df = pd.DataFrame()

    # 3. Sidebar Setup for User Input
    st.sidebar.header("🔍 Search Settings")
    book_input = st.sidebar.text_input(
        "Enter Book Title:", 
        placeholder="e.g., Rich Dad Poor Dad"
    )
    search_button = st.sidebar.button("⚡ Search & Analyze")

    # 4. Trigger Pipeline on Button Click
    if search_button:
        if not book_input.strip():
            st.sidebar.error("Bhai, pehle kisi book ka naam toh daalo!")
        else:
            with st.spinner(f"🚨 '{book_input}' ko platforms par scan kiya jaa raha hai... Please wait!"):
                try:
                    # Step A: Extract
                    raw_data = fetch_all_prices(book_input)
                    
                    if not raw_data:
                        st.error("Kisi bhi platform se data fetch nahi ho paya. Ek baar network check karo.")
                    else:
                        # Step B: Transform
                        cleaned_df = clean_data(raw_data)
                        
                        if cleaned_df.empty:
                            st.warning("Data extract toh hua par cleaning ke baad khali mila!")
                        else:
                            # Step C: Load
                            log_to_database(cleaned_df)
                            
                            st.session_state.current_df = cleaned_df
                            st.sidebar.success("✨ Data successfully processed!")
                            
                except Exception as e:
                    st.error(f"Pipeline Execution Breakdown: {e}")

    # 5. Core Layout Routing
    if not st.session_state.current_df.empty:
        render_dashboard(st.session_state.current_df)
    else:
        st.title("📚 BookPulse Analytics")
        st.markdown("### Real-Time Multi-Platform E-Book Price Aggregator & Analytics Pipeline")
        st.markdown("---")
        st.info("👈 Left sidebar mein book ka naam daal kar **Search & Analyze** par click karo live prices aur dashboard dekhne ke liye!")
        
        st.markdown("""
        #### ⚙️ Pipeline Features Loaded:
        * **Web Scraping Engine:** Live multi-source HTML parser via BeautifulSoup.
        * **ETL Pipeline:** Structured cleaning, token handling, and discount normalization via Pandas.
        * **SQL Logging Database:** Native search and optimization tracking with SQLite.
        * **Analytical Insights:** Interactive presentation layer powered by Seaborn and Matplotlib.
        """)