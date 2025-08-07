from modules.public.emociones.domain.repositories.Iemociones_repository import IEmocionesRepository
from modules.public.emociones.infrastructure.model.emociones_model import EmocionModel
from sqlalchemy.orm import Session
from datetime import datetime 
from modules.public.emociones.application.dto.emociones_dto import EmocionCreateDTO, EmocionOutDTO

class EmocionesRepository(IEmocionesRepository):
    def __init__(self, db: Session):
        self.db = db

    def crear_emocion(self, dto: EmocionCreateDTO):
        emocion = EmocionModel(
            session_id=dto.session_id,
            emocion=dto.emocion,
            confianza=dto.confianza,
            imagen_url=dto.imagen_url,
            timestamp=datetime.utcnow()
        )
        self.db.add(emocion)
        self.db.commit()
        self.db.refresh(emocion)
        return EmocionOutDTO.model_validate(emocion)

    def listar_emociones(self):
        emociones = self.db.query(EmocionModel).all()
        return [EmocionOutDTO.model_validate(e) for e in emociones]