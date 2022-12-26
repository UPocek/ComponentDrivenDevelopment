import pkg_resources
from django.apps import AppConfig


class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'

    provider_plugins = []
    visualizator_plugins = []

    def ready(self):
        self.provider_plugins = load_plugins("core.providers")
        self.visualizator_plugins = load_plugins("core.visualizators")


def load_plugins(group):
    plugins = []
    for entry_point in pkg_resources.iter_entry_points(group=group):
        plugin = entry_point.load()
        plugin = plugin()
        plugins.append(plugin)
    return plugins
