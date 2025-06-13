from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT = "-e ."

def get_requirements(file_path: str)-> List[str]:
    ''' this function will return the list of requirements'''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements] 
        '''this is done because when reading the new file we tend to read \n and we need to rempve that'''
        if HYPEN_E_DOT in requirements:  ## this is done because -e . should not be read from requirements.txt
            requirements.remove(HYPEN_E_DOT)
    
    return requirements



setup(
    name="ML Project",
    version="0.0.1",
    author="Rashtra Humane",
    author_email="rashtrahumane@gmail.com",
    packages=find_packages(),
    install_requires = get_requirements('requirements.txt')
)