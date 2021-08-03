﻿from setuptools import setup, find_packages
import io

def read(*filenames, **kwargs):
    encoding = kwargs.get('encoding', 'utf-8')
    sep = kwargs.get('sep', '\n')
    buf = []
    for filename in filenames:
        with io.open(filename, encoding=encoding) as f:
            buf.append(f.read())
    return sep.join(buf)

long_description = read('README.md')

setup(
    name='TURtLES',
    version=1.0,
    url='https://github.com/annehulsey/TURtLES',
    license='MIT License',
    author='Anne Hulsey',
    author_email='anne.hulsey@auckland.ac.nz',
    description='The Uncertainty in Regional-Level Earthquake Scenario simulation',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages = find_packages(),
    include_package_data=True,
    platforms='any',
    classifiers = [
        'Programming Language :: Python',
        'Natural Language :: English',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Topic :: Scientific/Engineering',
        ],
)