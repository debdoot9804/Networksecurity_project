from setuptools import find_packages,setup
from typing import List
def get_requirements()-> List[str]:
    """
    Function for returning list of requirements"""
    requirement_list=list()
    try:
        with open('requirements.txt','r') as file:
            lines=file.readlines()
            for line in lines:
                requirement=line.strip()
                #Ignore empty line & -e .
                if requirement and requirement!='-e .':
                    requirement_list.append(requirement)
    except FileNotFoundError:
        print("requiements.txt not found")
    return requirement_list
setup(
    name="Network Security",
    version="0.0.1",
    packages=find_packages(),
    install_required=get_requirements()

)                  



