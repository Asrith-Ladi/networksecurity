from setuptools import find_packages,setup
from typing import List

requirement_lst:List[str]=[]
def get_requirements() -> List[str]:
    """ this function will return list of requirements"""
    
    try :
        with open ('requirements.txt','r') as file:
            # read lines from file
            lines=file.readlines()
            
            ##process each line
            for line in lines:
                requirement=line.strip()
                # ignore empty lines and -e .

                if requirement and requirement!='-e .':
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print("requirement file not found")
    return requirement_lst

setup(
    name="NetworkSecurity",
    version="0.0.1",
    author='Asrith Ladi',
    author_email ='asrithladi@gmail.com',
    packages = find_packages(),
    install_requires=get_requirements()
)

print(get_requirements())
                    