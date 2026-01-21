import os
import json
import time
import re
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# ================= USER SETTINGS =================
CHECK_INTERVAL = 180  # seconds (3 minutes)

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

SEEN_FILE = "seen.json"

SITES = {
    "Carsales": "https://www.carsales.com.au/cars/",
    "Pickles": "https://www.pickles.com.au/cars/",
    "Greys": "https://www.greys.com.au/automotive",
    "Slattery": "https://www.slatteryauctions.com.au/",
    "Carbids": "https://www.carbids.com.au/",
    "Manheim": "https://www.manheim.com.au/"
}

TARGET_CARS = [
    {"model": "z4", "min_engine": 2.5},
    {"model": "300zx"},
    {"model": "mr2"},
    {"model": "mr-s"}
]
# =================================================

# ------------------ Helper Functions ------------------

def load_seen():
    try:
        with open(SEEN_FILE, "r") as f:
            return set(json.load(f))
    except:
        return set()


def save_seen(seen):
    with open(SEEN_FILE, "w") as f:
        json.dump(list(seen), f)


def send_telegram(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    try:
        requests.post(url, json={
            "chat_id": TELEGRAM_CHAT_ID,
            "text": message
        })
    except Exception as e:
        print(f"Telegram error: {e}")


def is_manual(text):
    return "manual" in text


def extract_engine(text):
    match = re.search(r"(\d\.\d)", text)
    return float(match.group(1)) if match else None


def matches_target(title):
    text = title.lower()
    if not is_manual(text):
        return False

    for car in TARGET_CARS:
        if car["model"] in text:
            # Engine size check
            if "min_engine" in car:
                engine = extract_engine(text)
                if engine and engine < car["min_engine"]:
                    return False

            # Year check
            if "min_year" in car:
                year = extract_year(text)
                if year and year < car["min_year"]:
                    return False

            return True

    return False


# ------------------ Browser Setup ------------------

def setup_browser():
    options = webdriver.ChromeOptions()
    options.binary_location = "/usr/bin/google-chrome"
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--ignore-certificate-errors")
    
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    return driver

# ------------------ Scraping ------------------

def scrape_site(driver, site, url, seen):
    try:
        driver.get(url)
        time.sleep(5)  # wait for page to load

        links = driver.find_elements(By.TAG_NAME, "a")
        for link in links:
            try:
                title = link.text.strip()
                href = link.get_attribute("href")
                if not title or not href:
                    continue

                uid = f"{site}:{href}"
                if uid in seen:
                    continue

                if matches_target(title):
                    seen.add(uid)
                    send_telegram(
                        f"🚗 NEW MATCH FOUND!\n\n"
                        f"{title}\n\n"
                        f"Site: {site}\n"
                        f"{href}"
                    )
            except:
                continue
    except Exception as e:
        print(f"Error scraping {site}: {type(e).__name__} - {e}")

# ------------------ Main Loop ------------------

def main():
    seen = load_seen()
    driver = setup_browser()

    send_telegram("✅ Car scraper started successfully")
    print("Scraper started...")

    while True:
        for site, url in SITES.items():
            print(f"Checking {site}...")
            scrape_site(driver, site, url, seen)
        save_seen(seen)
        time.sleep(CHECK_INTERVAL)

# ------------------ Entry Point ------------------

if __name__ == "__main__":
    main()
