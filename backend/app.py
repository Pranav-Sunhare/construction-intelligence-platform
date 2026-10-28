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
import os
import sys
from pathlib import Path

# Paths calculate karein
BASE_DIR = Path(__file__).resolve().parent
BACKEND_DIR = BASE_DIR / "backend"

# sys.path me backend directory ko pehle number par inject karein
if str(BACKEND_DIR) not in sys.path:
    sys.path.insert(0, str(BACKEND_DIR))
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

# Direct backend.app.main se import karein taaki name conflict na ho
try:
    from backend.app.main import app
except ModuleNotFoundError:
    # Fallback agar backend root me ho
    import importlib
    main_mod = importlib.import_module("app.main")
    app = getattr(main_mod, "app")

application = app
handler = app