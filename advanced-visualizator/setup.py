from setuptools import setup, find_packages

setup(
    name="advanced-visualizator",
    version="0.1",
    packages=find_packages(),

    entry_points = {
        'core.visualizators':['advanced_visualizator=advanced_visualizator.services.AdvencedVisualizator:AdvencedVisualizator']
    },
    
    package_data={'advanced_visualizator': ['static/advanced_visualizator/styles/*.css', 'static/advanced_visualizator/scripts/*.js', 'templates/advanced_visualizator/*.html']},

    zip_safe=False
)
