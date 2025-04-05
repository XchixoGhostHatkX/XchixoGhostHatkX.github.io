import argparse
import sqlite3
import requests
import os
import logging
from urllib.parse import urljoin

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

# Constants
DATABASE_FILE = "apk_search.db"

# Database Initialization
def create_database():
    """Create a database to store site information and search logs."""
    if not os.path.exists(DATABASE_FILE):
        conn = sqlite3.connect(DATABASE_FILE)
        cursor = conn.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS sites (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                site_name TEXT NOT NULL,
                site_url TEXT NOT NULL
            )
            """
        )
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS search_logs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                apk_name TEXT NOT NULL,
                site_url TEXT NOT NULL,
                apk_url TEXT NOT NULL
            )
            """
        )
        conn.commit()
        conn.close()
        logging.info("Database initialized successfully.")
    else:
        logging.info("Database already exists.")

# Helper Functions
def find_site_urls(site_names):
    """
    Map site names to URLs. This function assumes standard `.com` domains.
    """
    urls = []
    for name in site_names:
        url = f"https://{name}.com"
        urls.append(url)
    return urls

def search_apks(apk_name, site_urls):
    """
    Search for APKs on the given site URLs.
    This is a placeholder implementation that performs a simulated search.
    """
    apk_urls = []
    for site_url in site_urls:
        # Simulate APK URL construction
        apk_url = urljoin(site_url, f"download/{apk_name}.apk")
        apk_urls.append(apk_url)
    return apk_urls

def log_search_results(apk_name, site_urls, apk_urls):
    """
    Log search results into the database.
    """
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    for site_url, apk_url in zip(site_urls, apk_urls):
        cursor.execute(
            """
            INSERT INTO search_logs (apk_name, site_url, apk_url)
            VALUES (?, ?, ?)
            """,
            (apk_name, site_url, apk_url),
        )
    conn.commit()
    conn.close()
    logging.info("Search results logged to the database.")

# Main Function
def main():
    parser = argparse.ArgumentParser(description="Modded APK Search Tool")
    parser.add_argument(
        "-f", "--file", help="File containing site names (one per line)"
    )
    parser.add_argument(
        "-s", "--search", help="Search for APK by name"
    )
    args = parser.parse_args()

    # Initialize database
    create_database()

    if args.file:
        # Load site names from file
        if not os.path.exists(args.file):
            logging.error(f"File '{args.file}' not found.")
            return

        with open(args.file, "r") as file:
            site_names = [line.strip() for line in file.readlines()]

        site_urls = find_site_urls(site_names)
        logging.info("Site URLs:")
        for url in site_urls:
            logging.info(url)

    elif args.search:
        # Search for APK
        apk_name = args.search
        default_sites = ["modapk", "apkmodders", "darkmod"]
        site_urls = find_site_urls(default_sites)
        apk_urls = search_apks(apk_name, site_urls)

        logging.info("APK URLs:")
        for apk_url in apk_urls:
            logging.info(apk_url)

        # Log search results to the database
        log_search_results(apk_name, site_urls, apk_urls)

    else:
        logging.error("No valid arguments provided. Use -f or -s.")
        parser.print_help()

if __name__ == "__main__":
    main()