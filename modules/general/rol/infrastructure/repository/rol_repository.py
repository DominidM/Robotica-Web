from modules.general.rol.infrastructure.model.rol_model import RolModel
from modules.database import SessionLocal

class RolRepository:
    def __init__(self, db_session=None):
        self.db = db_session or SessionLocal()

    def get_all(self):
        return self.db.query(RolModel).all()

    def create(self, nombre, descripcion):
        nuevo_rol = RolModel(nombre=nombre, descripcion=descripcion)
        self.db.add(nuevo_rol)
        self.db.commit()
        self.db.refresh(nuevo_rol)
        return nuevo_rol