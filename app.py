# import os
# from fastapi import FastAPI, Request, Response
# import httpx

# # Top-level ASGI application instances for Vercel
# app = FastAPI(title="Construction Intelligence Platform Gateway")
# application = app
# handler = app

# @app.get("/")
# def root():
#     backend_url = os.environ.get("BACKEND_URL", "")
#     return {
#         "service": "app",
#         "backend_url_configured": bool(backend_url),
#         "status": "online"
#     }

# @app.api_route("/api/{path:path}", methods=["GET", "POST", "PUT", "DELETE"])
# async def proxy_to_backend(path: str, request: Request):
#     backend_url = os.environ.get("BACKEND_URL", "http://127.0.0.1:8000")
#     target_url = f"{backend_url.rstrip('/')}/api/{path}"
#     headers = dict(request.headers)
#     headers.pop("host", None)
#     body = await request.body()
#     async with httpx.AsyncClient(timeout=35.0) as client:
#         res = await client.request(
#             method=request.method,
#             url=target_url,
#             headers=headers,
#             content=body,
#             params=dict(request.query_params)
#         )
#         return Response(content=res.content, status_code=res.status_code, headers=dict(res.headers))

import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent
BACKEND_DIR = ROOT_DIR / "backend"

if str(BACKEND_DIR) not in sys.path:
    sys.path.insert(0, str(BACKEND_DIR))
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from backend.app.main import app, application, handler
