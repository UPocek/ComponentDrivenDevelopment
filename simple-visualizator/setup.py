from setuptools import setup, find_packages

setup(
    name="simple_visualizator",
    version="0.1",
    packages=find_packages(),
    entry_points={
        'core.django_apps':
            ['name=simple_visualizator.apps.SimpleVisualizatorConfig'],
        'core.visualizators':
            ['simple_visualizator=simple_visualizator.services.SimpleVisualizator:SimpleVisualizator']
    },
    package_data={'simple_visualizator': ['static/simple_visualizator/styles/*.css', 'static/simple_visualizator/scripts/*.js', 'templates/simple_visualizator/*.html']},
    zip_safe=False
)
