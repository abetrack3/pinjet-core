import codecs

from setuptools import setup, find_packages


VERSION = '0.0.1-beta.1'
DESCRIPTION = 'Small like a pin, fast like a jet! A lightweight Dependency Injection library for python'
AUTHOR = 'abetrack3 (Abrar Shahriar Abeed)'
AUTHOR_EMAIL = '<abrarshahriar2361@gmail.com>'

with codecs.open('README.md', encoding='utf-8') as readme_file:
    long_description = '\n' + readme_file.read()
    print(long_description)

setup(
    name='pinjet-core',
    version=VERSION,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'pinjet-common~=1.0.2'
    ],
    keywords=[
        'python',
        'dependency injection',
        'di framework',
        'ioc',
        'inversion of control',
    ],
)
