import os
from distutils.core import setup

# To install the trees library, open a Terminal, then run this file by typing:
#
# python setup.py install
#
# You need to have the setuptools module installed. Try reading the setuptools
# documentation: http://pypi.python.org/pypi/setuptools

here = os.path.abspath(os.path.dirname(__file__))
about = {}
with open(os.path.join(here, "trees", "__version__.py")) as f:
    exec(f.read(), about)

setup(
    name="trees",
    version=about["__version__"],
    author="Ceasar Bautista",
    author_email="cbautista2010@gmail.com",
    url="https://github.com/Ceasar/trees",
    description="Collection of various tree-like data structures",
    keywords=['tree', 'data', 'heap', 'autovivify'],
    packages=['trees'],
    install_requires=['six'],
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.5",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        ],
    long_description="""\
    A collection of various tree-like data structures.

    Includes:
    -   AutovivifiedDict
    -   ObjectifiedDict
    -   Heap (heapq wrapper)
     """)
