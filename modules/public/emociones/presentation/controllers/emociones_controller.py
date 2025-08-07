from modules.public.emociones.application.services.emociones_service import EmocionesService
from modules.public.emociones.application.dto.emociones_dto import EmocionCreateDTO

class EmocionesController:
    def __init__(self, service: EmocionesService):
        self.service = service

    def crear_emocion(self, dto: EmocionCreateDTO):
        return self.service.crear_emocion(dto)

    def listar_emociones(self):
        return self.service.listar_emociones()