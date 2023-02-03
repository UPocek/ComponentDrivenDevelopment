from setuptools import setup, find_packages

setup(
    name="ar_visualizator",
    version="0.1",
    packages=find_packages(),
    # entry_points={
    #     'core.django_apps':
    #         ['name=core.apps.CoreConfig']
    # },
    entry_points={
        'core.django_apps':['name=ar_visualizator.apps.ArVisualizatorConfig'],
        'core.visualizators':
            ['ar_visualizator=ar_visualizator.services.ArVisualizator:ArVisualizator']
    },
    package_data={'ar_visualizator': ['templates/ar_visualizator/ar_visualizator.html']},
    zip_safe=False
)
