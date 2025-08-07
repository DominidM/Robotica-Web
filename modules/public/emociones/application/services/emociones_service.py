from modules.public.emociones.domain.repositories.Iemociones_repository import IEmocionesRepository
from modules.public.emociones.application.dto.emociones_dto import EmocionCreateDTO

class EmocionesService:
    def __init__(self, repository: IEmocionesRepository):
        self.repository = repository

    def crear_emocion(self, dto: EmocionCreateDTO):
        return self.repository.crear_emocion(dto)

    def listar_emociones(self):
        return self.repository.listar_emociones()