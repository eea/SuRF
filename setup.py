""" Install
"""
import os
from setuptools import setup, find_packages

PACKAGE_NAME = "SuRF"
SUMMARY = (
    "SuRF"
)
DESCRIPTION = (
    open("README.rst", 'r').read() + '\n\n' +
    open(os.path.join("docs", 'HISTORY.txt')).read()
)

VERSION = open('version.txt').read().strip()

setup(
    name=PACKAGE_NAME,
    version=VERSION,
    description=SUMMARY,
    long_description=DESCRIPTION,
    author='Cosmin Basca',
    author_email='webadmin@eea.europa.eu',
    url='http://github.com/eea/SuRF',
    license='MPL',
    packages=find_packages(exclude=['surf.test']),
    entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
    classifiers=[
      'Environment :: Console',
      'Intended Audience :: Developers',
      "Programming Language :: Python",
      'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    install_requires=[
          'setuptools',
          'SPARQLWrapper',
          # -*- Extra requirements: -*-
          'rdflib >= 2.4.2',
    ]
)
