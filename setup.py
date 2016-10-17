#!/usr/bin/env python
# coding=utf-8

from setuptools import setup, find_packages

setup(
    name = 'hcct',
    version = '0.0.3',
    description = 'A plugin for Hachi to detect contacts.',
    author = 'MomingCoder',
    author_email = 'a398445075@gmail.com',
    url = 'https://github.com/guokr/Hachi',
    license = 'MIT',
    keywords = ['filter', 'Hachi', 'plugin', 'contact'],
    classifiers = ['Topic :: Text Processing'],
    packages = find_packages(),
    install_requires = ['xpinyin',
                        'cnprep'],
    platform = ['Windows', 'Linux', 'Mac'],
)
