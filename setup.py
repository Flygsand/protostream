# -*- mode: python; tab-width: 4; indent-tabs-mode: nil; encoding: utf-8 -*-

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)) + '/lib')

from setuptools import setup, find_packages
from protostream import __version__

setup(
    name='protostream',
    version=__version__,
    
    author='protomouse',
    author_email='root@protomou.se',
    license='GPLv3',
    url='http://github.com/protomouse/protostream',

    packages=find_packages('lib'),
    package_dir={'': 'lib'},
    package_data={'protostream':['templates/*.html']},
    scripts=['bin/protostream'],

    install_requires=[
        'cement>=2.0.2',
        'argparse>=1.2.1',
        'Jinja2>=2.6'
    ]
)