# 📚 BookPulse Analytics

A Streamlit-based unified analytics UI for real-time multi-platform ebook price aggregation, ETL processing, and dashboard visualization.

---

## 🚀 Overview

BookPulse Analytics is an end-to-end data pipeline application that:

- Scrapes book prices from multiple platforms
- Cleans and transforms raw data using an ETL pipeline
- Stores processed data into a database
- Displays interactive analytics dashboards via Streamlit

---

## 🧠 Architecture

### 🔄 Pipeline Flow

1. Extract

- Fetch book pricing data from multiple sources
- Function: `fetch_all_prices(book_title)`

1. Transform

- Clean and normalize dataset using Pandas
- Function: `clean_data(raw_data)`

1. Load

- Store processed results in database
- Function: `log_to_database(cleaned_df)`

1. Visualize

- Render interactive dashboard UI
- Function: `render_dashboard(df)`

---

## 🖥️ Application Features

- Sidebar book search input
- One-click “Search & Analyze” execution
- Session-state based data persistence
- Interactive analytics dashboard
- Streamlit runtime detection (auto-launch support)
- Robust error handling across pipeline stages

---

## 📁 Project Structure

```text
project/
│
├── main.py               # Main Streamlit entrypoint (run with `streamlit run main.py`)
├── src/
│   ├── scraper.py        # fetch_all_prices()
│   ├── pipeline.py       # clean_data(), log_to_database()
│   ├── dashboard.py      # render_dashboard()
│
└── README.md
```

---

## ⚙️ Installation

```bash
git clone https://github.com/your-username/bookpulse-analytics.git
cd bookpulse-analytics
python -m venv venv
source venv/bin/activate  # Mac/Linux
pip install -r requirements.txt
```

---

## ▶️ Running the App

```bash
streamlit run main.py
```

---

## 🧪 Core Pipeline Logic

```python
if search_button:
    raw_data = fetch_all_prices(book_input)
    cleaned_df = clean_data(raw_data)
    log_to_database(cleaned_df)
    st.session_state.current_df = cleaned_df
```

---

## ⚠️ Error Handling

Handles gracefully:

- Empty book input
- Scraping failures
- Empty datasets after cleaning
- Pipeline execution errors

---

## 🛠️ Tech Stack

- Streamlit (UI)
- Pandas (data processing)
- BeautifulSoup (scraping - assumed)
- SQLite (database logging - assumed)
- Matplotlib / Seaborn (visualization - assumed)

---

## 📄 License

MIT License (or your preferred license)


live at:https://bookpulse.streamlit.app/
