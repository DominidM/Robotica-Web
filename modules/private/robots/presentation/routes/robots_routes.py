from fastapi import APIRouter, Depends, HTTPException, status
from modules.database import get_db
from modules.private.robots.application.dto.robots_dto import RobotDTO, RobotCreateDTO
from modules.private.robots.application.services.robots_service import RobotsService
from modules.private.robots.infrastructure.repository.robots_repository import RobotsRepository

router = APIRouter()

@router.get("/", summary="Listar Robots")
def listar_robots(db=Depends(get_db)):
    repo = RobotsRepository(db)
    service = RobotsService(repo)
    robots = service.listar_robots()
    return [RobotDTO.from_entity(robot).dict() for robot in robots]

@router.get("", summary="Buscar por identificador_unico")
def get_robot_by_identificador_unico(identificador_unico: str, db=Depends(get_db)):
    repo = RobotsRepository(db)
    service = RobotsService(repo)
    robot = service.get_by_identificador_unico(identificador_unico)
    if robot:
        return [RobotDTO.from_entity(robot).dict()]
    else:
        return []

@router.post("/", summary="Crear Robot", status_code=status.HTTP_201_CREATED)
def crear_robot(robot: RobotCreateDTO, db=Depends(get_db)):
    repo = RobotsRepository(db)
    service = RobotsService(repo)
    existente = service.get_by_identificador_unico(robot.identificador_unico)
    if existente:
        raise HTTPException(status_code=409, detail="Robot ya registrado con ese identificador.")
    nuevo_robot = service.crear_robot(robot)
    return RobotDTO.from_entity(nuevo_robot).dict()