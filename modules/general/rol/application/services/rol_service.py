from modules.general.rol.infrastructure.repository.rol_repository import RolRepository

class RolService:
    def __init__(self, rol_repository=None):
        self.rol_repository = rol_repository or RolRepository()

    def listar_roles(self):
        return self.rol_repository.get_all()

    def crear_rol(self, nombre, descripcion):
        return self.rol_repository.create(nombre, descripcion)