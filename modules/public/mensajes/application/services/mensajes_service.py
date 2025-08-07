from modules.public.mensajes.domain.repositories.Imensajes_repository import IMensajesRepository
from modules.public.mensajes.application.dto.mensajes_dto import MensajeCreateDTO

class MensajesService:
    def __init__(self, repository: IMensajesRepository):
        self.repository = repository

    def crear_mensaje(self, dto: MensajeCreateDTO):
        return self.repository.crear_mensaje(dto)

    def listar_mensajes(self):
        return self.repository.listar_mensajes()