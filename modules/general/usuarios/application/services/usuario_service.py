from modules.general.usuarios.infrastructure.repositories.usuario_repository import UsuarioRepository
from modules.general.usuarios.application.dto.usuario_dto import UsuarioOutDTO
from modules.general.rol.infrastructure.repository.rol_repository import RolRepository
from modules.general.usuarios.application.dto.completar_usuario_dto import CompletarUsuarioDTO
from modules.general.usuarios.application.dto.ingresar_usuario_dto import UsuarioCreateRobotDTO
from modules.general.usuarios.application.dto.usuario_create_web_dto import UsuarioCreateWebDTO

import hashlib

class UsuarioService:
    def __init__(self, usuario_repository=None, rol_repository=None):
        self.usuario_repository = usuario_repository or UsuarioRepository()
        self.rol_repository = rol_repository or RolRepository()

    def listar_usuarios(self):
        usuarios = self.usuario_repository.get_all()
        roles = {rol.id: rol.nombre for rol in self.rol_repository.get_all()}
        usuarios_dto = []
        for usuario in usuarios:
            dto = UsuarioOutDTO.from_orm(usuario)
            dto.rol_nombre = roles.get(usuario.rol_id, None)
            usuarios_dto.append(dto)
        return usuarios_dto
    
    def crear_usuario_web(self, dto: UsuarioCreateWebDTO):
        usuario = self.usuario_repository.crear_usuario_web(
            nombre=dto.nombre,
            email=dto.email,
            rol_id=dto.rol_id,
            registro_key=dto.registro_key
        )
        return UsuarioOutDTO.from_orm(usuario)


    def completar_registro(self, dto: CompletarUsuarioDTO):
        # Hashear el password
        password_hash = hashlib.sha256(dto.password.encode()).hexdigest()
        usuario = self.usuario_repository.completar_registro(dto.registro_key, dto.email, password_hash)
        if usuario:
            return UsuarioOutDTO.from_orm(usuario)
        return None

    def crear_usuario_robot(self, dto: UsuarioCreateRobotDTO):
        return self.usuario_repository.crear_usuario(
            nombre=dto.nombre,
            registro_key=dto.registro_key,
            rol_id=dto.rol_id
        )