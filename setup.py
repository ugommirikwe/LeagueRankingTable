from importlib.metadata import entry_points
from setuptools import setup, find_packages

def read_requirements():
    with open('requirements.txt') as req:
        content = req.read()
        requirements = content.split('\n')
    
    return requirements

setup(
    name='leaguetable',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=read_requirements(),
    entry_points='''
        [console_scripts]
        leaguetable=leaguetable.main:cli
    '''
)
