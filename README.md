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

## Installation

```bash
git clone https://github.com/1shlba/car-auction-web-scraper.git
cd car-auction-web-scraper
pip install -r requirements.txt
