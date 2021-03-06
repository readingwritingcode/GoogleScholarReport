#!/usr/bin/env python3
# coding: utf-8

# Copyright (c) Colav.
# Distributed under the terms of the Modified BSD License.

# -----------------------------------------------------------------------------
# Minimal Python version sanity check (from IPython)
# -----------------------------------------------------------------------------

# See https://stackoverflow.com/a/26737258/2268280
# sudo pip3 install twine
# python3 setup.py sdist bdist_wheel
# twine upload dist/*
# For test purposes
# twine upload --repository-url https://test.pypi.org/legacy/ dist/*

from __future__ import print_function
from setuptools import setup, find_packages

import os
import sys
import codecs


v = sys.version_info

def read(rel_path):
    here = os.path.abspath(os.path.dirname(__file__))
    with codecs.open(os.path.join(here, rel_path), 'r') as fp:
        return fp.read()


def get_version(rel_path):
    for line in read(rel_path).splitlines():
        if line.startswith('__version__'):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    else:
        raise RuntimeError("Unable to find version string.")

shell = False


if os.name in ('nt', 'dos'):
    shell = True
    warning = "WARNING: Windows is not officially supported"
    print(warning, file=sys.stderr)


def main():
    setup(
        # Application name:
        name="GoogleScholarReport",

        # Version number (initial):
        version="0.1.0",

        # Application author details:
        author="Colav",
        author_email="grupocolav@udea.edu.co",

        # Packages
        packages=find_packages(exclude=['tests']),

        # Include additional files into the package
        include_package_data=True,

        # Details
        url="https://github.com/readingwritingcode/google-scholar-report",

        #
        license="BSD",
        description="Bibliographic capture system for non-scrapping data sources",

        long_description=open("README.md").read(),

        long_description_content_type="text/markdown",

        # Dependent packages (distributions)
        install_requires=['beautifulsoup4==4.9.3',
              'bibtexparser==1.2.0',
              'bs4==0.0.1',
              'et-xmlfile==1.1.0',
              'future==0.18.2',
              'fuzzywuzzy==0.18.0',
              'helium==3.0.5',
              'lxml==4.6.2',
              'numpy==1.20.1',
              'openpyxl==3.0.7',
              'pandas==1.2.3',
              'pyparsing==2.4.7',
              'python-dateutil==2.8.1',
              'python-Levenshtein==0.12.2',
              'pytz==2021.1',
              'selenium==3.141.0',
              'six==1.15.0',
              'soupsieve==2.2.1',
              'Unidecode==1.2.0',
              'urllib3==1.26.3'],
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        ]
    )


if __name__ == "__main__":
    main()
