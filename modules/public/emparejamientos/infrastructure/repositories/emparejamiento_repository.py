from modules.public.emparejamientos.domain.repositories.Iemparejamiento_repository import IEmparejamientoRepository
from modules.public.emparejamientos.infrastructure.model.emparejamiento_model import EmparejamientoModel
from sqlalchemy.orm import Session, joinedload
from modules.public.emparejamientos.application.dto.emparejamiento_dto import EmparejamientoCreateDTO, EmparejamientoUpdateDTO, EmparejamientoOutDTO

class EmparejamientoRepository(IEmparejamientoRepository):
    def __init__(self, db: Session):
        self.db = db

    def crear_emparejamiento(self, dto: EmparejamientoCreateDTO):
        emp = EmparejamientoModel(
            usuario_id=dto.usuario_id,
            robot_id=dto.robot_id,
            fecha_inicio=dto.fecha_inicio,
            estado=dto.estado
        )
        self.db.add(emp)
        self.db.commit()
        self.db.refresh(emp)
        return self._to_out_dto(emp)

    def actualizar_emparejamiento(self, dto: EmparejamientoUpdateDTO):
        emp = self.db.query(EmparejamientoModel).filter_by(id=dto.id).first()
        if emp:
            if dto.fecha_fin:
                emp.fecha_fin = dto.fecha_fin
            if dto.estado:
                emp.estado = dto.estado
            self.db.commit()
            self.db.refresh(emp)
            return self._to_out_dto(emp)
        return None

    def listar_emparejamientos(self):
        emps = self.db.query(EmparejamientoModel).options(
            joinedload(EmparejamientoModel.usuario),
            joinedload(EmparejamientoModel.robot)
        ).all()
        return [self._to_out_dto(e) for e in emps]

    def _to_out_dto(self, emp):
        return EmparejamientoOutDTO(
            id=emp.id,
            usuario_id=emp.usuario_id,
            robot_id=emp.robot_id,
            fecha_inicio=emp.fecha_inicio,
            fecha_fin=emp.fecha_fin,
            estado=emp.estado,
            usuario_nombre=emp.usuario.nombre if emp.usuario else None,
            robot_nombre=emp.robot.nombre if emp.robot else None,
        )