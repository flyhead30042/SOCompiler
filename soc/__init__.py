

import logging
import sys
from pathlib import Path
import os


# logging.basicConfig(stream=sys.stdout, level=logging.INFO, format="%(asctime)s - %(levelname)s - (message)s")
logging.basicConfig(
    level=logging.DEBUG,  # Set the logging level
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',  # Log message format
    datefmt='%Y-%m-%d %H:%M:%S',  # Date format
    handlers=[logging.StreamHandler(sys.stdout)]  # Output to standard output
)


ELI_API_KEY = "eli-9c81e82f-1e98-4439-a169-a820c30e2fa8"
# ELI_API_URL = "https://gateway.eli.gaia.gic.ericsson.se" 
ELI_API_URL = "https://gateway.language-intelligence.internal.ericsson.com"

ROOT_DIR = Path(os.path.dirname(os.path.abspath(__file__))).parent.absolute()
RES_DIR = os.path.join(ROOT_DIR, "resources")