import os
import sys
from setuptools import find_packages, setup

wd = os.path.dirname(os.path.abspath(__file__))
os.chdir(wd)
sys.path.insert(1, wd)

readme = open(os.path.join(wd, 'README.rst'), 'r').readlines()
long_description = ''.join(readme)

version = __import__('burninator').__version__

setup(
    name='burninator',
    version=version,
    description='Burnination Library for Python',
    long_description=long_description,
    author='Evan Cordell',
    author_email='cordell.evan@gmail.com',
    url='',
    license='MIT',
    packages=find_packages(exclude=['tests', 'tests.*']),
    include_package_data=True,
    install_requires=[
        'colorama>=0.3.2',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: Implementation :: PyPy'
    ]
)
