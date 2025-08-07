from modules.public.mensajes.application.services.mensajes_service import MensajesService
from modules.public.mensajes.application.dto.mensajes_dto import MensajeCreateDTO

class MensajesController:
    def __init__(self, service: MensajesService):
        self.service = service

    def crear_mensaje(self, dto: MensajeCreateDTO):
        return self.service.crear_mensaje(dto)

    def listar_mensajes(self):
        return self.service.listar_mensajes()