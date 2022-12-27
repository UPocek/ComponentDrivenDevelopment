from abc import ABC, abstractmethod


class Visualizator(ABC):
    @abstractmethod
    def identifier(self):
        pass

    @abstractmethod
    def name(self):
        pass

    @abstractmethod
    def show(self):
        pass