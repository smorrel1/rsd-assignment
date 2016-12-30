# Greengraph plots a line showing the percentage of green pixels between
# two points.  Copyright (C) 2016 Stephen Morrell. See LICENCE for details.

# execute with: sudo python setup.py install

from setuptools import setup, find_packages

setup(
    name = "Greengraph",
    version = "0.1",
    packages = find_packages(exclude=['*test']),
    scripts = ['scripts/greengraph'],
    install_requires = ['argparse']
)
