import logging

def get_logger(name: str):
    """
    Gets a logger with the given name, and configures it if it has never been configured before.

    Args:
        name (str): The name of the logger to get.

    Returns:
        A configured logger with the given name.
    """
    logger = logging.getLogger(name)
    if not logger.handlers: 
        handler = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)
    return logger

logger = get_logger(__name__)