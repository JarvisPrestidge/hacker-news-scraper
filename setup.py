#!/usr/bin/env python3
"""
A setuptools based setup module.
"""

from setuptools import setup

def readme():
    """
    Reads README.md file into 'long_description' variable.
    """
    with open('README.md') as file:
        return file.read()

setup(
    name='hacker-news-scraper',
    version='1.0',
    license='MIT',
    description='Hacker news post scraper.',
    long_description=readme(),
    author='Jarvis Prestidge',
    author_email='jarvisprestidge@gmail.com',
    url='https://github.com/JarvisPrestidge/hacker-news',
    packages=['hackernews'],
    install_requires=[
        'BeautifulSoup4',
        'Requests',
        'Click'
    ],
    classifiers=[
        'Natural Language :: English',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3.5',
        'License :: OSI Approved :: MIT License',
    ]
)
