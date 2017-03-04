# -*- coding: UTF-8 -*-

import setuptools
from distutils.core import setup

# http://stackoverflow.com/a/7071358/735926
import re
VERSIONFILE='eolas/__init__.py'
verstrline = open(VERSIONFILE, 'rt').read()
VSRE = r'^__version__\s+=\s+[\'"]([^\'"]+)[\'"]'
mo = re.search(VSRE, verstrline, re.M)
if mo:
    verstr = mo.group(1)
else:
    raise RuntimeError("Unable to find version string in %s." % VERSIONFILE)

setup(
    name='eolas',
    version=verstr,
    author='Baptiste Fontaine',
    author_email='b@ptistefontaine.fr',
    packages=['eolas'],
    url='https://github.com/bfontaine/eolas',
    license=open('LICENSE', 'r').read(),
    description='Eolas interpreter',
    long_description=open('README.rst', 'r').read(),
    install_requires=[
        'appdirs==1.4.2',
        'packaging==16.8',
        'ply==3.10',
        'pyparsing==2.1.10',
        'six==1.10.0',
    ],
    classifiers=[
        'Environment :: Console',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
    entry_points={
        'console_scripts':[
            'eolas = eolas.interpreter:main',
        ]
    },
)
