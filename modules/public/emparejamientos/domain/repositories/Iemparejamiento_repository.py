from abc import ABC, abstractmethod

class IEmparejamientoRepository(ABC):
    @abstractmethod
    def crear_emparejamiento(self, dto):
        pass

    @abstractmethod
    def actualizar_emparejamiento(self, dto):
        pass

    @abstractmethod
    def listar_emparejamientos(self):
        pass