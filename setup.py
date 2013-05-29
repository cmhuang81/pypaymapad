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


setup(name='pypaymapad',
      version='0.1',
      description='paymapad python version',
      long_description="ad map ",
      author='',
      author_email='',
      url='',
      keywords='pypaymapad',
      packages=find_packages('src'),
      package_dir={'': 'src'},
      include_package_data=True,
      install_requires = requires
      )

