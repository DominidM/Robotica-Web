from modules.general.usuarios.application.services.usuario_service import UsuarioService
from modules.general.usuarios.application.dto.completar_usuario_dto import CompletarUsuarioDTO
from modules.general.usuarios.application.dto.ingresar_usuario_dto import UsuarioCreateRobotDTO
from modules.general.usuarios.application.dto.usuario_create_web_dto import UsuarioCreateWebDTO

class UsuarioController:
    def __init__(self):
        self.service = UsuarioService()

    def listar_usuarios(self):
        return self.service.listar_usuarios()
    
    def completar_registro(self, dto: CompletarUsuarioDTO):
        return self.service.completar_registro(dto)
    
    def crear_usuario_robot(self, dto: UsuarioCreateRobotDTO):
        return self.service.crear_usuario_robot(dto)
    
    def crear_usuario_web(self, dto: UsuarioCreateWebDTO):
        return self.service.crear_usuario_web(dto)
    
    def buscar_por_registro_key(self, registro_key: str):
        return self.service.buscar_por_registro_key(registro_key)