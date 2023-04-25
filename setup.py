from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT = '-e .'

def get_req(file_name:str) -> List[str]:

    with open(file_name) as file_instance:
        req = file_instance.readlines()
        req = [i.replace('\n','') for i in req]

    if HYPEN_E_DOT in req:
        req.remove(HYPEN_E_DOT)

    return req

setup(
    name='mlpipeline',
    version='0.0.1',
    author='Dhanush Jain',
    author_email='dhanushjain190@gmail.com',
    packages=find_packages(),
    install_requires = get_req('requirements.txt')
)