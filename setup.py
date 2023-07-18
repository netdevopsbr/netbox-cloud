from setuptools import setup, find_packages
import pathlib

import env

# Get path to parent folder
here = pathlib.Path(__file__).parent.resolve()

# long_description = README.md
long_description = (here / 'README.md').read_text(encoding='utf-8')

github = 'https://github.com/netdevopsbr/netbox-cloud'

# Proxbox dependencies
requires = []

dev_requires = [
    'pytest>=3.7',
    'check-manifest',
    'twine',
    'setuptools',
    'wheel'
]

from env import *


setup(
    name=CONFIG_VARIABLES.get("name"),
    version=CONFIG_VARIABLES.get("version"),
    author=CONFIG_VARIABLES.get("author_name"),
    author_email=CONFIG_VARIABLES.get("author_email"),
    description=CONFIG_VARIABLES.get("description"),
    url=CONFIG_VARIABLES.get("github_url"),
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Framework :: Django",
        "Operating System :: Unix",
        "License :: OSI Approved :: Apache Software License",
    ],
    keywords="netbox netbox-plugin plugin cloud proxmox private-cloud hypervisor",
    project_urls={
        'Source': CONFIG_VARIABLES.get("github_url"),
    },
    packages=find_packages(),
    include_package_data=True,
    package_data={
        "": ['*','*/*','*/*/*'],
    },
    install_requires=requires,
    extras_require={
        "dev": dev_requires,
    },
    python_requires= f'>={CONFIG_VARIABLES.get("python_version")}',
)