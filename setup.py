from setuptools import find_packages,setup
from typing import List


def get_requirements(file_path:str)->List[str]:
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]
    return requirements

setup(
    name='Crack Enhancer',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)