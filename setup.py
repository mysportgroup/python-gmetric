#!/usr/bin/env python
# -*- coding: utf-8 -*-

import setuptools
from distutils.core import setup


setup(
        name='python-gmetric',
        version='3.1',
        description='A python lib and cmd tool for gmetric (ganglia).',
        author='Vladimir Vuksan',
        #author_email='r.wittler@mysportgroup.de',
        maintainer='Robin Wittler',
        maintainer_email='r.wittler@mysportgroup.de',
        license='GPL3+',
        url='https://github.com/robin-wittler/python-gmetric',
        packages=['pygmetric'],
        platforms='POSIX',
)



# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
