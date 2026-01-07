from fastapi import FastAPI
from backend.api.projects import router as projects_router
from backend.api.uploads import router as uploads_router
from backend.api.templates import router as templates_router

app = FastAPI(title="DMS")

@app.get("/")
def root():
    return {
        "name": "DMS API",
        "docs": "/docs",
        "health": "ok"
    }

app.include_router(projects_router)                 # /projects
app.include_router(uploads_router, prefix="/upload")# /upload/{project_id}
app.include_router(templates_router, prefix="/templates")