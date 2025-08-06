from modules.private.robots.application.dto.robots_dto import RobotDTO

class RobotsService:
    def __init__(self, robots_repository):
        self.robots_repository = robots_repository

    def listar_robots(self):
        robots = self.robots_repository.get_all()
        return [RobotDTO.from_entity(r) for r in robots]