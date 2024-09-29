from setuptools import setup, find_packages

# Project metadata (replace with your project details)
project_name = "OneGPT"
project_version = "0.0.1"
project_description = "A brief description of your project"
author = "Sumit Dhakad"
author_email = "sumit.dhakad9644@gmail.com"
license = "MIT"

# Dependencies (listed in requirements.txt)
with open("requirements.txt", "r") as f:
    requirements = f.readlines()

setup(
    name=project_name,
    version=project_version,
    description=project_description,
    author=author,
    author_email=author_email,
    license=license,
    packages=find_packages(exclude=[]),  # Exclude test and documentation folders
    install_requires=requirements,  # Read requirements from requirements.txt
    python_requires=">=3.10",  # Specify minimum Python version (optional)
)


# python setup.py sdist  # Creates a source distribution
# python setup.py bdist_wheel  # Creates a wheel distribution