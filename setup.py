#!/usr/bin/env python

from setuptools import setup

setup(
    name='jfrog-python-example',
    version='1.0',
    description='Project example for building Python project with JFrog products',
    author='JFrog',
    author_email='jfrog@jfrog.com',
    url='https://github.com/carmithersh/carmit-testing',
    packages=['pythonExample'],
    install_requires=['PyYAML==5.4', 'nltk','paramiko==2.0.9', 'urllib3==1.26.19','redis == 4.6.0','Flask==2.3.2','gunicorn==22.0.0'],
)
