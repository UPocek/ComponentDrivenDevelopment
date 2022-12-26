from setuptools import setup, find_packages

setup(
    name="core",
    version="0.1",
    packages=find_packages(),
    entry_points={
        'core.django_apps':
            ['name=core.apps.CoreConfig']
    },
    package_data={'core': ['static/core/styles/*.css', 'static/core/scripts/*.js', 'templates/core/*.html']},
    zip_safe=False
)
