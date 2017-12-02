#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

requirements = [
    'Click>=6.0',
    # TODO: put package requirements here
]

setup_requirements = [
    # TODO: put package setup requirements here
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='{{ cookiecutter.app_name }}',
    version='{{ cookiecutter.version }}',
    description="{{ cookiecutter.project_short_description }}",
    long_description=readme,
    author="{{ cookiecutter.full_name.replace('\"', '\\\"') }}",
    author_email='{{ cookiecutter.email }}',
    url='https://github.com/{{ cookiecutter.email }}/{{ cookiecutter.app_name }}',
    packages=find_packages(include=['{{ cookiecutter.app_name }}']),
    entry_points={
        # 'console_scripts': [
        #     '{{ cookiecutter.app_name }}={{ cookiecutter.app_name }}.cli:main'
        # ]
    },
    include_package_data=True,
    install_requires=requirements,
    zip_safe=False,
    keywords='{{ cookiecutter.app_name }}',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    test_suite='tests',
    tests_require=test_requirements,
    setup_requires=setup_requirements,
)
