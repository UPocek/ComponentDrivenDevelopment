from core.services.Providers import Provider
from wiki_provider.services.WikiParserService import scrape

class WikiProvider(Provider):
    def identifier(self):
        return "wiki_provider"

    def name(self):
        return "Wikipedia provider"

    def load(self, **kwargs):
        scrape(kwargs['graph_name'], kwargs['wiki_link'], kwargs['depth'], kwargs['num_of_links'])