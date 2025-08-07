from modules.public.mensajes.domain.repositories.Imensajes_repository import IMensajesRepository
from modules.public.mensajes.infrastructure.model.mensajes_model import MensajeModel, RemitenteEnum
from sqlalchemy.orm import Session
from modules.public.mensajes.application.dto.mensajes_dto import MensajeCreateDTO, MensajeOutDTO
from datetime import datetime

class MensajesRepository(IMensajesRepository):
    def __init__(self, db: Session):
        self.db = db

    def crear_mensaje(self, dto: MensajeCreateDTO):
        mensaje = MensajeModel(
            # CAMBIADO: usar sesion_id en lugar de session_id
            sesion_id=dto.sesion_id,
            remitente=RemitenteEnum(dto.remitente),
            mensaje=dto.mensaje,
            timestamp=datetime.utcnow()
        )
        self.db.add(mensaje)
        self.db.commit()
        self.db.refresh(mensaje)
        # Convertir Enum a string para el DTO
        data = {
            "id": mensaje.id,
            "sesion_id": mensaje.sesion_id,  # CAMBIADO
            "remitente": mensaje.remitente.value,
            "mensaje": mensaje.mensaje,
            "timestamp": mensaje.timestamp
        }
        return MensajeOutDTO.model_validate(data)

    def listar_mensajes(self):
        mensajes = self.db.query(MensajeModel).all()
        result = []
        for m in mensajes:
            data = {
                "id": m.id,
                "sesion_id": m.sesion_id,  # CAMBIADO
                "remitente": m.remitente.value if m.remitente else None,
                "mensaje": m.mensaje,
                "timestamp": m.timestamp
            }
            result.append(MensajeOutDTO.model_validate(data))
        return result