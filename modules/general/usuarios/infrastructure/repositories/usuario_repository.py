from modules.general.usuarios.infrastructure.model.usuario_model import UsuarioModel
from modules.database import SessionLocal
from sqlalchemy.exc import NoResultFound

class UsuarioRepository:
    def __init__(self, db_session=None):
        self.db = db_session or SessionLocal()

    def get_all(self):
        try:
            return self.db.query(UsuarioModel).all()
        finally:
            self.db.close()

    def crear_usuario_web(self, nombre, email, rol_id, registro_key=None):
        usuario = UsuarioModel(
            nombre=nombre,
            email=email,
            rol_id=rol_id,
            registro_key=registro_key
        )
        self.db.add(usuario)
        self.db.commit()
        self.db.refresh(usuario)
        return usuario

    def completar_registro(self, registro_key, email, password_hash):
        try:
            usuario = (
                self.db.query(UsuarioModel)
                .filter(
                    UsuarioModel.registro_key == registro_key,
                    (UsuarioModel.password_hash == None) | (UsuarioModel.password_hash == "")
                )
                .first()
            )
            if not usuario:
                return None
            usuario.email = email
            usuario.password_hash = password_hash
            # Cambia el rol a cliente (3) si era invitado (1)
            if usuario.rol_id == 1:
                usuario.rol_id = 3
            self.db.commit()
            self.db.refresh(usuario)
            return usuario
        finally:
            self.db.close()

            
    def crear_usuario(self, nombre, registro_key, rol_id):
        usuario = UsuarioModel(
            nombre=nombre,
            registro_key=registro_key,
            rol_id=rol_id
        )
        self.db.add(usuario)
        self.db.commit()
        self.db.refresh(usuario)
        return usuario