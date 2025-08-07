from abc import ABC, abstractmethod

class IMensajesRepository(ABC):
    @abstractmethod
    def crear_mensaje(self, dto):
        pass

    @abstractmethod
    def listar_mensajes(self):
        pass