from core.services.Providers import Provider
from ml_provider.services.NeuralNetworkParserService import generate_graph

class NeuralNetworkProvider(Provider):
    def identifier(self):
        return "ml_provider"

    def name(self):
        return "Neural network provider"

    def load(self, graph_name):
        generate_graph(graph_name)