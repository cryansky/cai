# utils.py

def load_env_variables():
    """Load environment variables from a .env file."""
    from dotenv import load_dotenv
    import os

    load_dotenv()

def log_message(message, level="INFO"):
    """Log messages with different severity levels."""
    import logging

    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    if level == "INFO":
        logging.info(message)
    elif level == "ERROR":
        logging.error(message)
    elif level == "WARNING":
        logging.warning(message)

def handle_error(error):
    """Handle errors by logging them."""
    log_message(f"An error occurred: {str(error)}", level="ERROR")