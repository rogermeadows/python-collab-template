"""
#
# Template setup.py
#
"""

from setuptools import setup, find_packages


version = '0.0.1'

setup(
    name='python-collab-template',
    version=version,
    url='https://github.com/rogermeadows/python-collab-template',
    license='GPL',
    author='John Smith',
    author_email='josh.smith@foo.io',
    description='Python Collab Template',
    long_description='Python Collab Template',
    packages=find_packages(
        exclude=(
           '.*',
           'EGG-INFO',
           '*.egg-info',
           '_trial*',
           '*.tests',
           '*.tests.*',
           'tests.*',
           'tests',
           'examples.*',
           'examples',
        )
    ),
    include_package_data=True,
    install_requires=[
    ],
    entry_points={
        'console_scripts': [
        ],
    },
)
