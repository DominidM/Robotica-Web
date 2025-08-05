from modules.general.rol.infrastructure.repository.rol_repository import RolRepository
from modules.general.rol.application.dto.rol_dto import RolCreateDTO, RolOutDTO

class RolService:
    def __init__(self, rol_repository=None):
        self.rol_repository = rol_repository or RolRepository()

    def listar_roles(self):
        roles = self.rol_repository.get_all()
        return [RolOutDTO.from_orm(rol) for rol in roles]

    def crear_rol(self, rol_create_dto: RolCreateDTO):
        nuevo_rol = self.rol_repository.create(rol_create_dto.nombre, rol_create_dto.descripcion)
        return RolOutDTO.from_orm(nuevo_rol)