#-*- coding: utf-8 -*-


import os
import sys

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.txt')).read()
CHANGES = open(os.path.join(here, 'CHANGES.txt')).read()
requires = [
    'jsonpickle',
    'mock',
    'pymongo'
    ]


setup(name='paymapad',
      version='0.0',
      description='paymapad',
      long_description="ad map ",
      author='',
      author_email='',
      url='',
      keywords='paymapad',
      packages=find_packages('src'),
      package_dir={'': 'src'},
      include_package_data=True,
      install_requires = requires
      )

