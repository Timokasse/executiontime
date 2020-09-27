#!/usr/bin/env python3

"""
This allows to build the package and deploy it in PyPi:

> pip install -r requirements.txt
> rm -rf dist
> ./setup.py sdist bdist_wheel
> twine upload dist/*

"""

from pathlib import Path
from setuptools import find_packages, setup

HERE = Path(__file__).parent

README = (HERE / "README.md").read_text()

setup(
    name = 'executiontime',
    packages = find_packages(),
    version = '0.2.0',
    description = 'Utilities to show execution time during development of a module',
    long_description = README,
    long_description_content_type = "text/markdown",
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: French',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Testing',
    ],
    author = 'Timokasse',
    author_email = 'Timokasse@users.noreply.github.com',
    url = 'https://github.com/Timokasse/executiontime',
    download_url = 'https://github.com/Timokasse/executiontime/tarball/0.1', # I'll explain this in a second
    keywords = ['testing', 'logging', 'time', 'performance', 'execution'],
    license='MIT',
    install_requires=[
    ],
    include_package_data=True,
    zip_safe=False,
)
