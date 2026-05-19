import argparse
import sys
from colorama import init, Fore, Style
from bot.validators import validate_side, validate_order_type, validate_quantity, validate_price
from bot.orders import place_order
from bot.logging_config import logger

# Initialize colorama for cross-platform colored output
init(autoreset=True)

def print_success(message: str):
    """Print success message in green."""
    print(Fore.GREEN + Style.BRIGHT + "SUCCESS: " + message)

def print_error(message: str):
    """Print error message in red."""
    print(Fore.RED + Style.BRIGHT + "ERROR: " + message)

def print_info(message: str):
    """Print info message in cyan."""
    print(Fore.CYAN + message)

def print_warning(message: str):
    """Print warning message in yellow."""
    print(Fore.YELLOW + message)

def main():
    parser = argparse.ArgumentParser(
        description="Binance Futures Testnet Trading Bot CLI",
        formatter_class=argparse.RawTextHelpFormatter
    )
    
    parser.add_argument("--symbol", type=str, required=True, help="Trading pair symbol (e.g., BTCUSDT)")
    parser.add_argument("--side", type=str, required=True, help="Order side: BUY or SELL")
    parser.add_argument("--type", type=str, required=True, dest="order_type", help="Order type: MARKET or LIMIT")
    parser.add_argument("--quantity", type=str, required=True, help="Amount to trade")
    parser.add_argument("--price", type=str, required=False, help="Limit price (required if type is LIMIT)")

    # Display help if no arguments provided
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)

    args = parser.parse_args()

    print_info("\n--- Order Request Summary ---")
    print_info(f"Symbol:     {args.symbol.upper()}")
    print_info(f"Side:       {args.side.upper()}")
    print_info(f"Type:       {args.order_type.upper()}")
    print_info(f"Quantity:   {args.quantity}")
    if args.order_type.upper() == "LIMIT":
        print_info(f"Price:      {args.price if args.price else 'N/A'}")
    print_info("-----------------------------\n")

    try:
        # Validate inputs
        side = validate_side(args.side)
        order_type = validate_order_type(args.order_type)
        quantity = validate_quantity(args.quantity)
        price = validate_price(order_type, args.price)

        # Place the order
        print_warning("Connecting to Binance Futures Testnet and placing order...")
        response = place_order(
            symbol=args.symbol,
            side=side,
            order_type=order_type,
            quantity=quantity,
            price=price
        )
        
        # Display Success Output
        print("")
        print_success("Order placed successfully!")
        print_info("\n--- Order Response Details ---")
        print_info(f"Order ID:   {response.get('orderId')}")
        print_info(f"Status:     {response.get('status')}")
        print_info(f"Price:      {response.get('price')}")
        print_info(f"Orig Qty:   {response.get('origQty')}")
        print_info(f"Client ID:  {response.get('clientOrderId')}")
        print_info("------------------------------\n")
        
    except ValueError as e:
        print_error(f"Validation Error - {str(e)}")
        logger.warning(f"CLI Validation Error: {str(e)}")
        sys.exit(1)
    except Exception as e:
        print_error(f"Failed to place order - {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print_error("\nOperation cancelled by user.")
        sys.exit(1)
