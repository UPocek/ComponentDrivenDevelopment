from setuptools import setup, find_packages

setup(
    name="ml-provider",
    version="0.1",
    packages=find_packages(),
    # entry_points={
    #     'core.django_apps':
    #         ['name=core.apps.CoreConfig']
    # },
    zip_safe=False
)
