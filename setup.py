#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='ember-gae',
    version='0.0.1',
    description='Google App Engine NDB <> Ember Data',
    author='Mitchel Kelonye',
    author_email='kelonyemitchel@gmail.com',
    url='https://github.com/kelonye/ember-gae',
    packages=['ember_gae',],
    package_dir = {'ember_gae': 'lib'},
    packages=find_packages(),
    license='MIT License',
    zip_safe=True
)