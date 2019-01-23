#!/usr/bin/env python

from setuptools import setup

def readme():
    with open('README.md') as readmemd:
        return readmemd.read()

setup(
    name = 'executiontime',
    packages = ['executiontime'],
    version = '0.1.1',
    description = 'Utilities to show execution time during development of a module',
    long_description = readme(),
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
    author = 'Pierre Cart-Grandjean',
    author_email = 'timok@free.fr',
    url = 'https://github.com/Timokasse/executiontime',
    download_url = 'https://github.com/Timokasse/executiontime/tarball/0.1', # I'll explain this in a second
    keywords = ['testing', 'logging', 'time'],
    license='MIT',
    install_requires=[
    ],
    include_package_data=True,
    zip_safe=False,
)
