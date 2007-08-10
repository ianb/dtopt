from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='dtopt',
      version=version,
      description="Add options to doctest examples while they are running",
      long_description="""\
""",
      classifiers=[], # Get strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      keywords='doctest',
      author='Ian Bicking',
      author_email='ianb@colorstudy.com',
      url='',
      license='MIT',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
