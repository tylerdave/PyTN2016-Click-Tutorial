"""A setuptools based setup module for click_tutorial"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from codecs import open
from os import path
from setuptools import setup, find_packages

import versioneer

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as readme_file:
    readme = readme_file.read()

with open(path.join(here, 'HISTORY.rst'), encoding='utf-8') as history_file:
    history = history_file.read().replace('.. :changelog:', '')

requirements = [
    'click>=6.0',
    'colorama',
    'requests>=2.0',
    'httpbin',
    'pytest',
    'reqcli',
]

test_requirements = [
    'pytest',
]

setup(
    name='click_tutorial',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description="Tutorial for writing command line applications using click.",
    long_description=readme + '\n\n' + history,
    author="Dave Forgac",
    author_email='tylerdave@tylerdave.com',
    url='https://github.com/tylerdave/click_tutorial',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    entry_points={
        'console_scripts':[
            'pytn=click_tutorial.cli:cli',
            'httpbin=click_tutorial.cli:run_httpbin',
            ],
        },
    include_package_data=True,
    install_requires=requirements,
    license="MIT",
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
