from setuptools import setup, find_packages

setup(
    name='pasha_bank_api',
    version='0.1.0',
    description='A Python client for interacting with PASHA Bank\'s API.',
    author='Your Name',
    author_email='elyas.ghausi@gmail.com',
    url='https://github.com/elyasomer/pasha-bank-api', 
    packages=find_packages(),
    install_requires=[
        'requests>=2.32.2',
    ],
    classifiers=[
        'Programming Language :: Python :: 3.11',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.11',
    include_package_data=True,
)
