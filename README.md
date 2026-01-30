# car-auction-web-scraper

Python web scraper that constantly monitors popular Australian car listing and auction sites and sends Telegram alerts based on specific search criteria. Requires Telegram bot token and chat API to receive notifications.

## Currently set up to search the following sites

- **Slattery Auctions** – https://slatteryauctions.com.au/  
- **Pickles Auctions** – https://www.pickles.com.au/  
- **Grays Auction** – https://www.grays.com/  
- **CARBIDS (online car auctions)** – https://www.carbids.com.au/  
- **Manheim Australia** – https://www.manheim.com.au/  
- **Carsales (vehicle marketplace)** – https://www.carsales.com.au/

## Currently set up to search for the following models:

- BMW Z4 Manual (2.5L engine or larger)
- Nissan Z32 300zx Manual
- Toyota MR2/MR-S Manual
- -BMW S1000rr 2018+ Manual

## Installation

1. Clone the repository
```bash
git clone https://github.com/your-username/car-auction-web-scraper.git
cd car-auction-web-scraper
```
2. Create a virtual environment
```bash
python -m venv venv
```
Activate it:
```bash
# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```
4. Add in your telegram bot token and chat id

Create a .env file in the root directory and add:
```bash
TELEGRAM_BOT_TOKEN=your_telegram_bot_token
TELEGRAM_CHAT_ID=your_telegram_chat_id
```

Note: The .env file is ignored by Git and should never be committed for security/privacy reasons.

5. Run the scraper
```bash
python car_monitor.py
```
6. Output

The scraper will now search for car auction listings based on the configured criteria in the code.

Matching listings are printed to the console.

Notifications are sent to the configured Telegram chat when matching listings are found.


