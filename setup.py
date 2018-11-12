from setuptools import find_packages
from setuptools import setup

REQUIRED_PACKAGES = ['cycler==0.10.0', 'kiwisolver==1.0.1', 'mnist==0.2.2', 'numpy==1.15.4', 'pyparsing==2.3.0',
                     'python-dateutil==2.7.5', 'scikit-learn==0.20.0', 'scipy==1.1.0', 'six==1.11.0']

setup(
    name='trainer',
    version='0.1',
    install_requires=REQUIRED_PACKAGES,
    packages=find_packages(),
    include_package_data=True,
    description='My training application package.'
)
