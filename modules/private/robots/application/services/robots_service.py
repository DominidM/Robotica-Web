from modules.private.robots.domain.entities.robots import Robot

class RobotsService:
    def __init__(self, repo):
        self.repo = repo

    def listar_robots(self):
        return self.repo.get_all()

    def crear_robot(self, robot_dto):
        existente = self.repo.get_by_identificador_unico(robot_dto.identificador_unico)
        if existente:
            # Devuelve el existente si ya está registrado
            return existente
        robot = Robot(
            id=None,
            nombre=robot_dto.nombre,
            identificador_unico=robot_dto.identificador_unico,
            ip_actual=robot_dto.ip_actual,
            estado=robot_dto.estado,
            descripcion=robot_dto.descripcion,
            fecha_registro=None
        )
        return self.repo.add_and_return(robot)
    
    def get_by_identificador_unico(self, identificador_unico):
        return self.repo.get_by_identificador_unico(identificador_unico)