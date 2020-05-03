"""Module setup."""

import runpy
from setuptools import setup, find_packages

PACKAGE_NAME = "piweatherrock-data-climacell"
version_meta = runpy.run_path("./version.py")
VERSION = version_meta["__version__"]


with open("README.md", "r") as fh:
    long_description = fh.read()


def parse_requirements(filename):
    """Load requirements from a pip requirements file."""
    lineiter = (line.strip() for line in open(filename))
    return [line for line in lineiter if line and not line.startswith("#")]


if __name__ == "__main__":
    setup(
        name=PACKAGE_NAME,
        version=VERSION,
        packages=find_packages(),
        install_requires=parse_requirements("requirements.txt"),
        python_requires=">=3.7",
        scripts=["scripts/pwr-climacell-data"],
        description="Provides forecast data from ClimaCell for PiWeatherRock",
        long_description=long_description,
        long_description_content_type="text/markdown",
        license='MIT',
        url='https://github.com/genebean/python-piweatherrock-data-climacell',
        classifiers=[
            'License :: OSI Approved :: MIT License',
        ],
    )
