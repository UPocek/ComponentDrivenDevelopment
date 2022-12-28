from core.services.Providers import Provider

class NeuralNetworkProvider(Provider):
    def identifier(self):
        return "ml_provider"

    def name(self):
        return "Neural network provider"

    def load(self):
        pass