from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas, services
from .database import get_db

router = APIRouter()

@router.post("/projects/", response_model=schemas.ProjectResponse)
def create_project(project: schemas.ProjectCreate, db: Session = Depends(get_db)):
    # Generate tasks using Gemini
    tasks = services.generate_tasks(project.project_name, project.location)
    
    # Create project
    db_project = models.Project(
        project_name=project.project_name,
        location=project.location
    )
    db.add(db_project)
    db.commit()
    db.refresh(db_project)
    
    # Create tasks
    for task_name in tasks:
        db_task = models.Task(
            name=task_name,
            project_id=db_project.id
        )
        db.add(db_task)
    db.commit()
    
    return db_project

@router.get("/projects/{project_id}", response_model=schemas.ProjectResponse)
def get_project(project_id: int, db: Session = Depends(get_db)):
    project = db.query(models.Project).filter(models.Project.id == project_id).first()
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    return project