#!/usr/bin/env python3
"""
Django backed for Psycopg 3
"""

# Copyright (C) 2021 The Psycopg Team

import os
from setuptools import setup, find_packages

# Read the description from the README
try:
    with open(os.path.join(os.path.dirname(__file__), "README.rst")) as f:
        readme = f.read()
except IOError:
    readme = __doc__

setup(
    name="django_psycopg3",
    description=readme.splitlines()[0],
    long_description="\n".join(readme.splitlines()[2:]).lstrip(),
    author="Daniele Varrazzo",
    author_email="daniele.varrazzo@gmail.com",
    version="3.0.dev3",
    python_requires=">=3.6",
    install_requires=[
        "psycopg ~= 3.0.4",
    ],
    zip_safe=False,
    include_package_data=True,
    packages=find_packages(exclude=["tests"]),
)
