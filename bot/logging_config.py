import logging
import os
from logging.handlers import RotatingFileHandler

def setup_logger():
    """Configure logging for the bot."""
    # Ensure logs directory exists
    log_dir = "logs"
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    log_file = os.path.join(log_dir, "trading_bot.log")

    logger = logging.getLogger("trading_bot")
    
    # Avoid duplicate logs if logger is already configured
    if logger.hasHandlers():
        return logger
        
    logger.setLevel(logging.DEBUG)

    # File Handler
    file_handler = RotatingFileHandler(
        log_file, maxBytes=5 * 1024 * 1024, backupCount=2
    )
    file_handler.setLevel(logging.DEBUG)

    # Formatter
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    file_handler.setFormatter(formatter)

    # Add handler to logger
    logger.addHandler(file_handler)

    return logger

logger = setup_logger()
