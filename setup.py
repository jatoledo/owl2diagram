import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

description = """Generate a diagram of a given ontology"""

# The text of the README file
with open("README.md") as f:
    README = f.read()
    lines = README.split('\n')
    desc_lines = [line for line in lines if line[:2] != "[!"]
    README = "\n".join(desc_lines)
# This call to setup() does all the work
setup(
    name="owl2diagram",
    version="1.0.0",
    description=description,
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/jatoledo/owl2diagram",
    author="John Toledo",
    author_email="",
    license="Apache2",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    packages=["owl2diagram"],
    include_package_data=True,
    install_requires=["rdflib", "Jinja2"]
)
