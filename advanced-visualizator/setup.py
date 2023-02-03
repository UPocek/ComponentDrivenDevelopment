from setuptools import setup, find_packages

setup(
    name="advanced_visualizator",
    version="0.1",
    packages=find_packages(),
    entry_points={
        'core.django_apps':
            ['name=advanced_visualizator.apps.AdvancedVisualizatorConfig'],
        'core.visualizators':
            ['advanced_visualizator=advanced_visualizator.services.AdvencedVisualizator:AdvencedVisualizator']
    },
    package_data={'advanced_visualizator': ['templates/advanced_visualizator/advanced_visualizator.html']},
    zip_safe=False
)
