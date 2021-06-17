#!/usr/bin/env python

"""
TODO Dive deep python包分发
"""

from distutils.core import setup

setup(
    name='dio',
    version='0.0.4',
    description='A layer between io and application',
    author='luoxiao1',
    author_email='luoxiao1@staff.weibo.com',
    url='',
    packages=[
        'dio',
        'dio.mixin',
        'dio.share',
        'dio.delegate',
        'dio.delegate.abstract', 'dio.delegate.exception', 'dio.delegate.helper', 'dio.delegate.impl',
        'dio.delegate.core', 'dio.delegate.core.option', 'dio.delegate.core.source',
        'dio.schemable', 'dio.schemable.schemable_python'
    ]
)
