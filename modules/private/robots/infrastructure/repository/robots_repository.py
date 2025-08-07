from modules.private.robots.domain.repositories.Irobots_repository import IRobotsRepository
from modules.private.robots.domain.entities.robots import Robot
from modules.private.robots.infrastructure.model.robot_model import RobotModel

class RobotsRepository(IRobotsRepository):
    def __init__(self, db_session):
        self.db_session = db_session

    def get_all(self):
        robots_db = self.db_session.query(RobotModel).all()
        return [
            Robot(
                id=r.id,
                nombre=r.nombre,
                identificador_unico=r.identificador_unico,
                ip_actual=r.ip_actual,
                estado=r.estado,
                descripcion=r.descripcion,
                fecha_registro=r.fecha_registro
            )
            for r in robots_db
        ]

    def get_by_id(self, robot_id: int):
        r = self.db_session.query(RobotModel).filter_by(id=robot_id).first()
        if r:
            return Robot(
                id=r.id,
                nombre=r.nombre,
                identificador_unico=r.identificador_unico,
                ip_actual=r.ip_actual,
                estado=r.estado,
                descripcion=r.descripcion,
                fecha_registro=r.fecha_registro
            )
        return None

    def get_by_identificador_unico(self, identificador_unico: str):
        r = self.db_session.query(RobotModel).filter_by(identificador_unico=identificador_unico).first()
        if r:
            return Robot(
                id=r.id,
                nombre=r.nombre,
                identificador_unico=r.identificador_unico,
                ip_actual=r.ip_actual,
                estado=r.estado,
                descripcion=r.descripcion,
                fecha_registro=r.fecha_registro
            )
        return None

    def add(self, robot: Robot):
        robot_model = RobotModel(
            nombre=robot.nombre,
            identificador_unico=robot.identificador_unico,
            ip_actual=robot.ip_actual,
            estado=robot.estado,
            descripcion=robot.descripcion,
            fecha_registro=robot.fecha_registro
        )
        self.db_session.add(robot_model)
        self.db_session.commit()
        self.db_session.refresh(robot_model)
        return robot_model.id

    def add_and_return(self, robot: Robot):
        robot_model = RobotModel(
            nombre=robot.nombre,
            identificador_unico=robot.identificador_unico,
            ip_actual=robot.ip_actual,
            estado=robot.estado,
            descripcion=robot.descripcion,
            fecha_registro=robot.fecha_registro
        )
        self.db_session.add(robot_model)
        self.db_session.commit()
        self.db_session.refresh(robot_model)
        return Robot(
            id=robot_model.id,
            nombre=robot_model.nombre,
            identificador_unico=robot_model.identificador_unico,
            ip_actual=robot_model.ip_actual,
            estado=robot_model.estado,
            descripcion=robot_model.descripcion,
            fecha_registro=robot_model.fecha_registro
        )

    def update(self, robot: Robot):
        r = self.db_session.query(RobotModel).filter_by(id=robot.id).first()
        if r:
            r.nombre = robot.nombre
            r.identificador_unico = robot.identificador_unico
            r.ip_actual = robot.ip_actual
            r.estado = robot.estado
            r.descripcion = robot.descripcion
            r.fecha_registro = robot.fecha_registro
            self.db_session.commit()
            return True
        return False

    def delete(self, robot_id: int):
        r = self.db_session.query(RobotModel).filter_by(id=robot_id).first()
        if r:
            self.db_session.delete(r)
            self.db_session.commit()
            return True
        return False