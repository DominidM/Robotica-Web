from modules.public.sesiones.domain.repositories.lsesiones_repository import ISesionesRepository
from modules.public.sesiones.infrastructure.model.sesiones_model import SesionModel
from modules.general.usuarios.infrastructure.model.usuario_model import UsuarioModel
from modules.private.robots.infrastructure.model.robot_model import RobotModel
from sqlalchemy.orm import Session, joinedload
from modules.public.sesiones.application.dto.sesiones_dto import SesionCreateDTO, SesionCloseDTO

class SesionesRepository(ISesionesRepository):
    def __init__(self, db: Session):
        self.db = db

    def crear_sesion(self, dto: SesionCreateDTO):
        sesion = SesionModel(
            usuario_id=dto.usuario_id,
            robot_id=dto.robot_id,
            fecha_inicio=dto.fecha_inicio
        )
        self.db.add(sesion)
        self.db.commit()
        self.db.refresh(sesion)
        return self._to_out_dto(sesion)

    def cerrar_sesion(self, dto: SesionCloseDTO):
        sesion = self.db.query(SesionModel).filter_by(id=dto.sesion_id).first()
        if sesion:
            sesion.fecha_fin = dto.fecha_fin
            self.db.commit()
            self.db.refresh(sesion)
            return self._to_out_dto(sesion)
        return None

    def listar_sesiones(self):
        sesiones = self.db.query(SesionModel).options(
            joinedload(SesionModel.usuario),
            joinedload(SesionModel.robot)
        ).all()
        return [self._to_out_dto(s) for s in sesiones]

    def _to_out_dto(self, sesion):
        return {
            "id": sesion.id,
            "usuario_id": sesion.usuario_id,
            "robot_id": sesion.robot_id,
            "usuario_nombre": sesion.usuario.nombre if sesion.usuario else "",
            "robot_nombre": sesion.robot.nombre if sesion.robot else "",
            "fecha_inicio": sesion.fecha_inicio,
            "fecha_fin": sesion.fecha_fin
        }