from abc import ABC, abstractmethod
from core.models import Node, Graph


class Visualizator(ABC):
    @abstractmethod
    def identifier(self):
        pass

    @abstractmethod
    def name(self):
        pass

    @abstractmethod
    def show(self, grapg:Graph):
        pass