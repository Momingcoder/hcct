#!/usr/bin/env python
# coding=utf-8

from setuptools import setup, find_packages

setup(
    name = 'Hachi_contact',
    version = '0.1',
    description = 'A plugin for Hachi',
    author = 'MomingCoder',
    author_email = 'a398445075@gmail.com',
    url = 'https://github.com/guokr/Hachi-contact',
    download_url = 'https://github.com/guokr/hachi-filter/tarball/0.1',
    license = 'MIT',
    keywords = ['filter', 'Hachi', 'plugin', 'contact'],
    classifiers = ['Topic :: Text Processing'],
    packages = find_packages(),
    install_requires = ['xpinyin',
                        'cnprep'],
    platform = ['Windows', 'Linux', 'Mac'],
)
