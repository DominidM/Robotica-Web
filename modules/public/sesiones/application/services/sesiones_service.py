from modules.public.sesiones.domain.repositories.lsesiones_repository import ISesionesRepository
from modules.public.sesiones.application.dto.sesiones_dto import SesionCreateDTO, SesionCloseDTO

class SesionesService:
    def __init__(self, repository: ISesionesRepository):
        self.repository = repository

    def crear_sesion(self, dto: SesionCreateDTO):
        return self.repository.crear_sesion(dto)

    def cerrar_sesion(self, dto: SesionCloseDTO):
        return self.repository.cerrar_sesion(dto)

    def listar_sesiones(self):
        return self.repository.listar_sesiones()