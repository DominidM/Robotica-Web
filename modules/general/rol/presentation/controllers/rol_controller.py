from modules.general.rol.application.services.rol_service import RolService
from modules.general.rol.application.dto.rol_dto import RolCreateDTO

class RolController:
    def __init__(self):
        self.service = RolService()

    def listar_roles(self):
        return self.service.listar_roles()

    def crear_rol(self, rol_create_dto: RolCreateDTO):
        return self.service.crear_rol(rol_create_dto)