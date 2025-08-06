from fastapi import APIRouter, Depends
from modules.database import get_db
from modules.private.robots.application.services.robots_service import RobotsService
from modules.private.robots.infrastructure.repository.robots_repository import RobotsRepository

router = APIRouter()

@router.get("/", summary="Listar Robots")
def listar_robots(db=Depends(get_db)):
    repo = RobotsRepository(db)
    service = RobotsService(repo)
    robots = service.listar_robots()
    return [robot.__dict__ for robot in robots]