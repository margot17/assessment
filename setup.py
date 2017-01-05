from setuptools import setup, find_packages
setup(
    name='greengraph',
    description='plots the portion of green pixels between two locations'
    version='0.1',
    author='Marietta Stasinou'
    packages=find_packages(exclude=['*test']),
    install_requires = ['argparse'
                       'geopy',
                       'numby',
                       'matplotlib']

)
Writing setup.py