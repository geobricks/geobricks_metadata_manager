from setuptools import setup
from setuptools import find_packages

setup(
    name='GeobricksMetadataManager',
    version='0.1.1',
    author='Simone Murzilli; Guido Barbaglia',
    author_email='geobrickspy@gmail.com',
    packages=find_packages(),
    license='LICENSE.txt',
    long_description=open('README.md').read(),
    description='Geobricks library to manage Metadata.',
    install_requires=[
        'flask',
        'flask-cors',
        'GeobricksCommon'
    ],
    url='http://pypi.python.org/pypi/GeobricksGeoserverManager/',
    keywords=['geobricks', 'metadata', 'd3s']
)
