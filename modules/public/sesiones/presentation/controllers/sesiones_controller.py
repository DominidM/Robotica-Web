from modules.public.sesiones.application.services.sesiones_service import SesionesService
from modules.public.sesiones.application.dto.sesiones_dto import SesionCreateDTO, SesionCloseDTO

class SesionesController:
    def __init__(self, service: SesionesService):
        self.service = service

    def crear_sesion(self, dto: SesionCreateDTO):
        return self.service.crear_sesion(dto)

    def cerrar_sesion(self, dto: SesionCloseDTO):
        return self.service.cerrar_sesion(dto)

    def listar_sesiones(self):
        return self.service.listar_sesiones()