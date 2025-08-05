from modules.general.rol.infrastructure.model.rol_model import RolModel
from modules.database import SessionLocal
from modules.general.rol.domain.repositories.Irol_repository import IRolRepository

class RolRepository(IRolRepository):
    def __init__(self, db_session=None):
        self.db = db_session or SessionLocal()

    def get_all(self):
        try:
            return self.db.query(RolModel).all()
        finally:
            self.db.close()

    def create(self, nombre, descripcion):
        try:
            nuevo_rol = RolModel(nombre=nombre, descripcion=descripcion)
            self.db.add(nuevo_rol)
            self.db.commit()
            self.db.refresh(nuevo_rol)
            return nuevo_rol
        finally:
            self.db.close()