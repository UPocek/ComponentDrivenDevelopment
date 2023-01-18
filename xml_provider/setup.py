from setuptools import setup, find_packages

setup(
    name="xml_provider",
    version="0.1",
    packages=find_packages(),
    # entry_points={
    #     'core.django_apps':
    #         ['name=core.apps.CoreConfig']
    # },
    entry_points={
        'core.django_apps':
            ['name=xml_provider.apps.XmlProviderConfig'],
        'core.providers':
            ['xml_provider=xml_provider.services.XmlProvider:XmlProvider']
    },
    package_data={'xml_provider': ['static/xml_provider/styles/*.css', 'static/xml_provider/scripts/*.js', 'templates/xml_provider/*.html']},

    zip_safe=False
)
