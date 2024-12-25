#!/usr/bin/env python

import qtmodern6
from setuptools import setup

_version = qtmodern6.__version__

setup(name='qtmodern6',
      version=_version,
      packages=['qtmodern6'],
      description='PySide6 Widgets Modern User Interface',
      long_description=open('README.rst').read(),
      author='hua Layn',
      author_email='layn@jinkuni.com',
      url='https://www.github.com/hualayn/qtmodern6',
      license='MIT',
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Topic :: Software Development :: User Interfaces'
      ],
      package_data={
          'qtmodern6': ['resources/*']
      },
      install_requires=['PySide6>=6.0.0'])
