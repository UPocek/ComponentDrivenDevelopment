from django.apps.registry import apps
from django.shortcuts import render

# Create your views here.


def index(request):
    visualizators = apps.get_app_config("core").visualizator_plugins
    print(visualizators)
    providers = apps.get_app_config("core").provider_plugins
    print(providers)
    context = {
        'visualizators': visualizators,
        'providers': providers
    }
    return render(request, 'core/index.html', context=context)

