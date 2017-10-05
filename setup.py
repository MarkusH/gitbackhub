# -*- coding: utf-8 -*-
from setuptools import find_packages, setup

import codecs

import gitbackhub

_version = "0.1.0"

with codecs.open('README.rst', 'r', 'utf-8') as readme:
    _long_description = readme.read()

setup(
    name='gitbackhub',
    version=gitbackhub.__version__,
    description=readme,
    author=gitbackhub.__author__,
    author_email=gitbackhub.__email__,
    url="https://github.com/MarkusH/gitbackhub",
    license='MIT',
    packages=find_packages(),
    install_requires=[
        "Click>=6",
        "requests>=2.18.3",
    ],
    entry_points={
        'console_scripts': [
            'gitbackhub = gitbackhub.cli:cli',
        ],
    },
    classifiers=(
        "Development Status :: 3 - Alpha",
        # "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3.6",
        "Topic :: Software Development :: Version Control",
        "Topic :: System :: Archiving :: Backup",
        "Topic :: Utilities",
    ),
)
