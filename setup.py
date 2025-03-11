from setuptools import setup, find_packages

# Path to your requirements.txt file
requirements_file = 'requirements.txt'

# Read the requirements.txt file
with open(requirements_file, 'r') as file:
    requirements = file.readlines()

setup(
    name="mask2former",  # Replace with your actual package name
    version="0.1.0",  # Replace with your version
    packages=find_packages(),
    install_requires=requirements,  # Install dependencies
)
