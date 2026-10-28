# """
# FastAPI entrypoint for Vercel deployment.
# Exports the FastAPI app instance from app/main.py.
# """
# import sys
# import os

# # Ensure the backend directory itself is on sys.path
# # so that 'app' package imports (e.g. app.config, app.routers) resolve correctly.
# _backend_dir = os.path.dirname(__file__)
# if _backend_dir not in sys.path:
#     sys.path.insert(0, _backend_dir)

# from app.main import app

# # Ensure 'app', 'application', and 'handler' are all exported at top-level
# # These are the names Vercel's Python runtime looks for.
# application = app
# handler = app
import sys
from pathlib import Path

# Backend folder ko Python path me add karein
BASE_DIR = Path(__file__).resolve().parent
BACKEND_DIR = BASE_DIR / "backend"

if str(BACKEND_DIR) not in sys.path:
    sys.path.insert(0, str(BACKEND_DIR))

# Backend ke app folder se main FastAPI instance import karein
from app.main import app

application = app
handler = app