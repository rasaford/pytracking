from setuptools import setup, find_packages

# this is an empty setup file to be able to import this library via pip
version = "0.0.1"
setup(name="pytracking-autolabel",
      version=version,


      packages=find_packages(include=["pytracking", "ltr"]))
