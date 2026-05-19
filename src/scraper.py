import requests
from bs4 import BeautifulSoup

def get_headers():
    # Headers taaki requests block na hon
    return {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9"
    }

def scrape_flipkart(book_title):
    print(f"[Scraper] Fetching data for '{book_title}' from Flipkart...")
    # TODO: Actual Flipkart BeautifulSoup parsing logic
    # Mock data for structural setup:
    return {
        "platform": "Flipkart",
        "title": book_title + " (Paperback)",
        "current_price": "₹450",
        "original_price": "₹599",
        "rating": "4.5"
    }

def scrape_amazon(book_title):
    print(f"[Scraper] Fetching data for '{book_title}' from Amazon...")
    # TODO: Actual Amazon BeautifulSoup parsing logic
    # Mock data for structural setup:
    return {
        "platform": "Amazon",
        "title": book_title + " (Kindle Edition)",
        "current_price": "₹420",
        "original_price": "₹499",
        "rating": "4.3"
    }

def fetch_all_prices(book_title, sources_file="config/sources.txt"):
    raw_results = []
    
    # Read sources from text file
    try:
        with open(sources_file, "r") as f:
            platforms = [line.strip().lower() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"Error: {sources_file} not found. Defaulting to Flipkart.")
        platforms = ["flipkart"]

    # Call specific scraper based on text file
    for platform in platforms:
        try:
            if platform == "flipkart":
                data = scrape_flipkart(book_title)
                raw_results.append(data)
            elif platform == "amazon":
                data = scrape_amazon(book_title)
                raw_results.append(data)
        except Exception as e:
            print(f"Error scraping {platform}: {e}")
            
    return raw_results