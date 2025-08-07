from abc import ABC, abstractmethod

class IEmocionesRepository(ABC):
    @abstractmethod
    def crear_emocion(self, dto):
        pass

    @abstractmethod
    def listar_emociones(self):
        pass