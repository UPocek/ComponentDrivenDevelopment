from setuptools import setup, find_packages

setup(
    name="wiki_provider",
    version="0.1",
    packages=find_packages(),
    install_requires=['Django>=2.1', 'beautifulsoup4>=4.10.0', 'requests>=2.27.1'],
    entry_points={
        'core.django_apps':
            ['name=wiki_provider.apps.WikiProviderConfig'],
        'core.providers':
            ['wiki_provider=wiki_provider.services.WikiProvider:WikiProvider']
    },
    package_data={'wiki_provider': ['static/wiki_provider/styles/*.css', 'static/wiki_provider/scripts/*.js', 'templates/wiki_provider/*.html']},

    zip_safe=False
)
