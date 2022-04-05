# -*- coding: utf-8 -*-


"""setup.py: setuptools control."""


import re
from setuptools import setup
from setuptools import find_packages


version = re.search(
    '^__version__\s*=\s*"(.*)"',
    open('app/app.py').read(),
    re.M
    ).group(1)


with open("README.rst", "rb") as f:
    long_descr = f.read().decode("utf-8")


setup(
    name = "cmdline-my-app",
    packages=find_packages(include=['app', 'app.*']),
    entry_points = {
        "console_scripts": ['my-app = app.app:main']
        },
    version = version,
    description = "Python command line application template.",
    long_description = long_descr,
    author = "Adrian Lyxell",
    author_email = "adrian.lyxell@sdnit.se",
    #url = "http://github.com/wherethecodeis",
    )
