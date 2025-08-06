from abc import ABC, abstractmethod
from modules.private.robots.domain.entities.robots import Robot

class IRobotsRepository(ABC):
    @abstractmethod
    def get_all(self):
        """Devuelve una lista de robots."""
        pass

    @abstractmethod
    def get_by_id(self, robot_id: int) -> Robot:
        """Devuelve un robot por su id."""
        pass

    @abstractmethod
    def add(self, robot: Robot):
        """Agrega un robot."""
        pass

    @abstractmethod
    def update(self, robot: Robot):
        """Actualiza un robot."""
        pass

    @abstractmethod
    def delete(self, robot_id: int):
        """Elimina un robot por su id."""
        pass