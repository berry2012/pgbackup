from setuptools import find_packages, setup

with open('README.md','r') as f:
    long_description = f.read()

setup(
    name='pgbackup',
    version='0.1.0',
    author='Olawale Olaleye',
    author_email='whaleberry@gmail.com',
    description='A utility tool to backup PostgreSQL databases',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/berry2012/pgbackup',
    packages=find_packages('src'),

)