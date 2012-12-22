from setuptools import setup

setup(
    name='superbeta website',
    version='1.0',
    description='The web-based version of superbeta',
    packages=['superbeta',
              'climbs',
              'users'],
    install_requires=[
        'Django==1.4.2',
        'South==0.7.6',
        'django-autoslug==1.6.1',
        'PIL==1.1.7']
)



