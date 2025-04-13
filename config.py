import logging
import os

from dotenv import load_dotenv

load_dotenv()
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

# --------------------------- Setup --------------------------- #

headers = {
    "Authorization": f"token {GITHUB_TOKEN}" if GITHUB_TOKEN else None
}
owner = "gaurav-321"
debug = False
logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(message)s')
blacklist_file = ["prompts.py", "README.md"]
