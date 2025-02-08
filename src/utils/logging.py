import logging
from rich.logging import RichHandler
from rich.console import Console

def configure_logging():
    """
    Configure logging to output to the console with rich formatting.
    """
    console = Console()
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(message)s",
        datefmt="[%X]",
        handlers=[RichHandler(console=console)]
    )
