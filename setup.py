#!/usr/bin/env python

from setuptools import setup

from vbump.__version__ import VERSION

with open("readme.md", "r") as fp:
    LONG_DESCRIPTION = fp.read()

setup(
    author="Jessy Williams",
    author_email="jessy@jessywilliams.com",
    description="Yet another version bumper",
    entry_points={"console_scripts": ["vbump=vbump.__main__:main"]},
    include_package_data=True,
    license="MIT",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    name="vbump",
    packages=["vbump"],
    url="https://github.com/jkwill87/vbump", 
    version=VERSION,
)
