class Usuario:
    def __init__(self, id, nombre, email, password_hash, fecha_registro, rol_id, registro_key):
        self.id = id
        self.nombre = nombre
        self.email = email
        self.password_hash = password_hash
        self.fecha_registro = fecha_registro
        self.rol_id = rol_id
        self.registro_key = registro_key