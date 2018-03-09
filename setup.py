from setuptools import setup, find_packages


VERSION = '0.1.1'

setup(
    name='program_synthesis',
    version=VERSION,
    description='NEAR Program Synthesis',
    packages=find_packages(),
    author='NEAR Inc & Contributors',
    dependency_links=[
        'https://github.com/nearai/pytorch-tools/tarball/master#egg=pytorch-tools-0.0.1',
    ],
    install_requires=[
        'ipython==5.5.0',
        'numpy==1.13.0',
        'pytorch-tools==0.0.1',
        'ply==3.8',
        'pylru==1.0.9',
        'pyparsing==2.2.0',
        'python-Levenshtein==0.12.0',
        'prompt_toolkit==1.0.15',
        'tensorflow==1.5.0'
    ]
)