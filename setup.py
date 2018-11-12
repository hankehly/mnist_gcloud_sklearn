from subprocess import check_output

from setuptools import find_packages
from setuptools import setup

REQUIRED_PACKAGES = check_output(['cat', 'requirements.txt']).decode().split()

setup(
    name='trainer',
    version='0.1',
    install_requires=REQUIRED_PACKAGES,
    packages=find_packages(),
    include_package_data=True,
    description='My training application package.'
)
