from datetime import datetime

class Sesion:
    def __init__(self, id, usuario_id, robot_id, fecha_inicio, fecha_fin=None):
        self.id = id
        self.usuario_id = usuario_id
        self.robot_id = robot_id
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin