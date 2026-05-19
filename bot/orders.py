from binance.exceptions import BinanceAPIException
from .client import get_binance_client
from .logging_config import logger

def place_order(symbol: str, side: str, order_type: str, quantity: float, price: float = None) -> dict:
    """
    Place a futures order on the Binance Testnet.
    
    Args:
        symbol: Trading pair symbol (e.g., BTCUSDT)
        side: Order side (BUY or SELL)
        order_type: Order type (MARKET or LIMIT)
        quantity: Amount to trade
        price: Limit price (required for LIMIT orders)
        
    Returns:
        dict: The order response from Binance API.
    """
    try:
        client = get_binance_client()
        logger.info(f"Placing {order_type} {side} order for {quantity} {symbol}...")
        
        # Base order params
        order_params = {
            "symbol": symbol.upper(),
            "side": side.upper(),
            "type": order_type.upper(),
            "quantity": quantity
        }
        
        # Add limit specific params
        if order_type.upper() == "LIMIT":
            order_params["timeInForce"] = "GTC"  # Good Till Cancel
            order_params["price"] = price

        # Execute futures order using python-binance's futures method
        response = client.futures_create_order(**order_params)
        logger.info(f"Order successfully placed. Response: {response}")
        return response

    except BinanceAPIException as e:
        logger.error(f"Binance API Error: {e.message} (Code: {e.code})")
        raise e
    except Exception as e:
        logger.error(f"Unexpected Error: {str(e)}")
        raise e
