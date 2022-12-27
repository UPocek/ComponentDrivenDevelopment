from abc import ABC, abstractmethod


class Provider(ABC):
    @abstractmethod
    def identifier(self):
        pass

    @abstractmethod
    def name(self):
        pass

    @abstractmethod
    def load(self):
        pass