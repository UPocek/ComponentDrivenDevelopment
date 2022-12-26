from django.apps import apps
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="index")
]

provider_plugins = apps.get_app_config("core").provider_plugins

for p in provider_plugins:
    plugin_path = path(f'plugin/data/{p.identifier()}/', include(f"{p.identifier()}.urls"))
    urlpatterns.append(plugin_path)