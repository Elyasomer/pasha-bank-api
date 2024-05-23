from setuptools import setup, find_packages

setup(
    name='pasha_bank_api',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
    author='Elyas Omar',
    author_email='elyas.ghausi@gmail.com',
    description='Python client for PASHA Bank API',
)
