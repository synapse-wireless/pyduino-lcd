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
    install_requires=['vcversioner'],
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
