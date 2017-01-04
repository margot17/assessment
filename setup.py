from setuptools import setup, find_packages
setup(
    name='greengraph',
    description='calculate green pixels'
    version='0.1',
    packages=find_packages(exclude=['*test']),
    install_requires = ['argparse']

)
Writing setup.py