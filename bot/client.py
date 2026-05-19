import os
from binance.client import Client
from dotenv import load_dotenv
from bot.logging_config import logger

def get_binance_client() -> Client:
    """Initialize and return the Binance client for Futures Testnet."""
    load_dotenv()
    
    api_key = os.getenv("BINANCE_API_KEY")
    api_secret = os.getenv("BINANCE_API_SECRET")
    
    if not api_key or not api_secret:
        logger.error("API keys missing from environment variables.")
        raise ValueError("BINANCE_API_KEY and BINANCE_API_SECRET must be set in .env")

    logger.info("Initializing Binance Testnet Client...")
    
    # Initialize client with testnet=True to use the Binance Testnet
    client = Client(api_key, api_secret)
    client.FUTURES_URL = 'https://testnet.binancefuture.com/fapi'
    
    return client
