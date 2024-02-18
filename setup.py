from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    '''
    This function returns a list of packages from requirements.txt.
    '''
    requirements = []
    
    with open(file_path) as file_obj:
        # Read requirements from the file and remove newline characters
        requirements = [req.strip() for req in file_obj.readlines()]

        # Remove the editable package reference if present
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements

setup(
    name='ml_project',
    version='0.0.1',
    author='Ana Vitória',
    author_email='anavitorialouro.ml@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
