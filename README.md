# Binance Futures Trading Bot

A complete, production-ready Python 3 trading bot for placing orders on the Binance Futures Testnet (USDT-M). This project demonstrates how to structure a clean, modular Python application utilizing `python-binance`.

## Features
- Place **MARKET** and **LIMIT** orders on Binance Futures.
- Supports both **BUY** (Long) and **SELL** (Short) sides.
- Fully validated CLI interface built with `argparse`.
- Enhanced User Experience with colored CLI outputs using `colorama`.
- Clean separation of concerns (API layer, validation layer, CLI layer).
- Robust exception handling and file logging (`logs/trading_bot.log`).
- Directly runs on the **Binance Futures Testnet** so you don't risk real funds.

## Project Structure
```
trading_bot/
│
├── bot/
│   ├── __init__.py        # Package initialization
│   ├── client.py          # Binance API client setup
│   ├── orders.py          # Core logic for executing futures orders
│   ├── validators.py      # Input validation logic
│   ├── logging_config.py  # Centralized file and console logger
│
├── cli.py                 # Command Line Interface entrypoint
├── README.md              # Documentation
├── requirements.txt       # Python dependencies
├── .env.example           # Example environment variables
└── logs/                  # Log files will be generated here
```

## Setup & Installation

**1. Create a Virtual Environment (Optional but recommended)**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

**2. Install Dependencies**
```bash
pip install -r requirements.txt
```

**3. Configure Environment Variables**
Copy the example environment file to `.env` and add your Binance Testnet API credentials.
```bash
cp .env.example .env
```
*You can get your testnet keys from: https://testnet.binancefuture.com/*

Edit the `.env` file:
```env
BINANCE_API_KEY=your_actual_testnet_api_key_here
BINANCE_API_SECRET=your_actual_testnet_api_secret_here
```

## Usage

You can interact with the bot through the CLI script `cli.py`.

### Help Menu
View all available options:
```bash
python cli.py --help
```

### Place a MARKET Order
Places a market order at the current market price.
```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.01
```

### Place a LIMIT Order
Places a limit order which requires a specific price.
```bash
python cli.py --symbol ETHUSDT --side SELL --type LIMIT --quantity 0.5 --price 3500.00
```

## Logging
Logs are automatically written to `logs/trading_bot.log`. The log file rotates automatically at 5MB, maintaining up to 2 backups.

## Error Handling
The bot will catch and cleanly display:
- Invalid inputs (e.g. negative quantities, missing prices for limit orders)
- Missing environment variables
- Network failures and specific `BinanceAPIException` errors (e.g. invalid symbol, insufficient margin)
