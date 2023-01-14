from django.apps.registry import apps
from django.http import HttpResponseRedirect
from django.urls import reverse

def neural_network_parsing(request):
    provider_plugins = apps.get_app_config("core").provider_plugins
    for plugin in provider_plugins:
        if plugin.identifier() == "ml_provider":
            plugin.load(graph_name="Tasa")
            break
    else:
        print("Nije instaliran plagin ml_provider")
    return HttpResponseRedirect(reverse("index"))
