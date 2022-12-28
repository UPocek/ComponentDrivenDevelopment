from setuptools import setup, find_packages

setup(
    name="ml-provider",
    version="0.1",
    packages=find_packages(),
    # entry_points={
    #     'core.django_apps':
    #         ['name=core.apps.CoreConfig']
    # },
    entry_points={
        'core.providers':['ml_provider=ml_provider.services.NeuralNetworkProvider:NeuralNetworkProvider']
    },

    package_data={'ml_provider': ['static/ml_provider/styles/*.css', 'static/ml_provider/scripts/*.js', 'templates/ml_provider/*.html']},
    zip_safe=False
)
