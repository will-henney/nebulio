from __future__ import print_function
from setuptools import setup, find_packages
from os.path import join, dirname

import nebulio

setup(name='nebulio',
      version=nebulio.__version__,
      description='Derive emission line ratios from count rates in HST filters ',
      longdesc=open(join(dirname(__file__), 'README.md')).read(),
      url='https://github.com/deprecated/nebulio',
      author='William Henney',
      author_email='w.henney@crya.unam.mx',
      license='MIT',
      packages=find_packages(),
      install_requires=[
          'numpy',
          'matplotlib',
          'pysynphot',
      ],
      zip_safe=False)
