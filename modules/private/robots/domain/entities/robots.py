from datetime import datetime

class Robot:
    def __init__(self, id, nombre, identificador_unico, ip_actual=None, estado=None, descripcion=None, fecha_registro=None):
        self.id = id
        self.nombre = nombre
        self.identificador_unico = identificador_unico
        self.ip_actual = ip_actual
        self.estado = estado
        self.descripcion = descripcion
        self.fecha_registro = fecha_registro if fecha_registro else datetime.utcnow()