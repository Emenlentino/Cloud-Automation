from setuptools import setup, find_packages

setup(
    name='cloud_automation',
    version='1.0',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
)
