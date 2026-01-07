from fastapi import APIRouter
from backend.models.project import ProjectCreate
from backend.services.project_service import create_project

router = APIRouter()

@router.post("/projects")
def create_project_endpoint(project: ProjectCreate):
    return create_project(project)