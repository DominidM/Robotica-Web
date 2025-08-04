from abc import ABC, abstractmethod

class IRolRepository(ABC):
    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def create(self, nombre: str, descripcion: str):
        pass