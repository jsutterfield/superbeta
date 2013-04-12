from setuptools import setup

setup(
    name='superbeta website',
    version='1.0',
    description='The web-based version of superbeta',
    packages=['superbeta',
              'climbs',],
    install_requires=[
        'Django == 1.4.5',
        'South == 0.7.6',
        'PIL == 1.1.7',
        'requests == 1.0.4']
)



