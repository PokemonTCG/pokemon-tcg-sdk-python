import sys, os
from setuptools import setup, find_packages
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'pokemontcgsdk'))
from config import __version__, __pypi_packagename__, __github_username__, __github_reponame__

tests_require = [
    'mock',
    'nose',
    'coverage',
    'yanc',
    'preggy',
    'tox',
    'ipdb',
    'coveralls',
    'sphinx',
    'vcrpy'
]

url='https://github.com/' + __github_username__ + '/' + __github_reponame__
download_url="{}/tarball/{}".format(url, __version__)

setup(
    name=__pypi_packagename__,
    version=__version__,
    description='Pokemon TCG SDK for pokemontcg.io',
    long_description='''
Pokemon TCG SDK is a python wrapper around the Pokemon TCG API located at pokemontcg.io
''',
    keywords='pokemon tcg sdk trading card game api rest',
    author='Andrew Backes',
    author_email='backes.andrew@gmail.com',
    url=url,
    download_url=download_url,
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: Unix',
        'Programming Language :: Python :: 3.9',
        'Operating System :: OS Independent',
    ],
    packages=find_packages(),
    include_package_data=False,
    install_requires=[
        # add your dependencies here
        # remember to use 'package-name>=x.y.z,<x.y+1.0' notation (this way you get bugfixes)
        'dacite>=1.6.0',
    ],
    extras_require={
        'tests': tests_require,
    },
    entry_points={
        'console_scripts': [
            # add cli scripts here in this form:
            # 'pokemontcgsdk=pokemontcgsdk.cli:main',
        ],
    },
)
