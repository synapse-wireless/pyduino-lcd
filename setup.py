#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    name='pyduinolcd',
    description="LCD shield library for the Synapse Pyduino development board",
    maintainer='Tyler Crumpton',
    maintainer_email='tyler.crumpton@synapse-wireless.com',
    url='https://github.com/tylercrumpton/pyduino-lcd',
    packages=['pyduinolcd'],
    install_requires=[
        'vcversioner',
        'pyduinoincludes==2.1.0',
        'snappyatmega==1.0.1'
    ],
    dependency_links=[
        "git+https://github.com/synapse-wireless/pyduino-includes.git@v2.1.0#egg=pyduinoincludes-2.1.0",
        "git+https://github.com/synapse-wireless/snappy-atmega.git@v1.0.1#egg=snappyatmega-1.0.1"
    ],
    vcversioner={
        'version_module_paths': ['pyduinolcd/_version.py'],
    },
    classifiers=[
        'Development Status :: 1 - Planning',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 2.7',
        'Natural Language :: English',
    ],
)
