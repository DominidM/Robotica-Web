from modules.private.robots.infrastructure.model.robot_model import RobotModel
from modules.public.sesiones.infrastructure.model.sesiones_model import SesionModel
from modules.public.emparejamientos.infrastructure.model.emparejamiento_model import EmparejamientoModel
from modules.general.rol.infrastructure.model.rol_model import RolModel
from modules.general.usuarios.infrastructure.model.usuario_model import UsuarioModel
from modules.public.emociones.infrastructure.model.emociones_model import EmocionModel
from modules.public.mensajes.infrastructure.model.mensajes_model import MensajeModel

# Esto garantiza que todos los modelos estén registrados
__all__ = [
    'UsuarioModel',
    'RobotModel',
    'SesionModel',
    'RolModel',
    'EmparejamientoModel',
    'EmocionModel',
    'MensajeModel'
]