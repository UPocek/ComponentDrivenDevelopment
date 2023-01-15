from django.apps.registry import apps
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from .form import JsonNeuralNetworkForm


def handle_uploaded_file(file):
    with open('..\ml-provider\ml_provider\examples\example.json', 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)

def neural_network_parsing(request):
    if request.method == 'POST':
        form = JsonNeuralNetworkForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file_content'])
            provider_plugins = apps.get_app_config("core").provider_plugins
            for plugin in provider_plugins:
                if plugin.identifier() == "ml_provider":
                    plugin.load(graph_name="Tasa")
                    break
            else:
                print("Neural network provider is not installed")
            return HttpResponseRedirect(reverse("index"))
    else:
        form = JsonNeuralNetworkForm()
    return render(request, 'ml_provider/index.html', {'form': form})