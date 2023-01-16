# from core.core.services.Providers import Provider
from core.services.Providers import Provider


class WikiProvider(Provider):
    def identifier(self):
        return "wiki"

    def name(self):
        return "Wikipedia provider"

    def load(self):
        pass