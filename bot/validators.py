def validate_side(side: str) -> str:
    """Validate that the order side is either BUY or SELL."""
    side = side.upper()
    if side not in ["BUY", "SELL"]:
        raise ValueError("Side must be either 'BUY' or 'SELL'.")
    return side

def validate_order_type(order_type: str) -> str:
    """Validate that the order type is either MARKET or LIMIT."""
    order_type = order_type.upper()
    if order_type not in ["MARKET", "LIMIT"]:
        raise ValueError("Order type must be either 'MARKET' or 'LIMIT'.")
    return order_type

def validate_quantity(quantity: str) -> float:
    """Validate that the quantity is a positive number."""
    try:
        qty = float(quantity)
        if qty <= 0:
            raise ValueError()
        return qty
    except ValueError:
        raise ValueError("Quantity must be a positive number.")

def validate_price(order_type: str, price: str = None) -> float:
    """Validate that the price is provided and is positive for LIMIT orders."""
    if order_type.upper() == "LIMIT":
        if price is None:
            raise ValueError("Price is required for LIMIT orders.")
        try:
            p = float(price)
            if p <= 0:
                raise ValueError()
            return p
        except ValueError:
            raise ValueError("Price must be a positive number for LIMIT orders.")
    return None
