from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pathlib import Path

from backend.api.projects import router as projects_router
from backend.api.uploads import router as uploads_router
from backend.api.templates import router as templates_router

app.mount("/assets", StaticFiles(directory=str(FRONTEND_DIR / "assets")), name="assets")

app = FastAPI(title="DMS")

ROOT = Path(__file__).resolve().parents[1]          # repo root (…/dms)
FRONTEND_DIR = ROOT / "frontend"
INDEX_HTML = FRONTEND_DIR / "index.html"

app.mount("/static", StaticFiles(directory=str(FRONTEND_DIR)), name="static")

@app.get("/")
def home():
    return FileResponse(str(INDEX_HTML))

app.include_router(projects_router)
app.include_router(uploads_router, prefix="/upload")
app.include_router(templates_router, prefix="/templates")