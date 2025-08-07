from abc import ABC, abstractmethod

class ISesionesRepository(ABC):
    @abstractmethod
    def crear_sesion(self, dto):
        pass

    @abstractmethod
    def cerrar_sesion(self, dto):
        pass

    @abstractmethod
    def listar_sesiones(self):
        pass