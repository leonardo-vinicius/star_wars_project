from dotenv import load_dotenv
from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent
ENV_PATH = BASE_DIR / ".env"

load_dotenv(ENV_PATH)

ENV_SECRET_KEY = os.getenv("SECRET_KEY")

if not ENV_SECRET_KEY:
    raise RuntimeError("SECRET_KEY não definida no arquivo .env")
