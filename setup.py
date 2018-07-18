#!/usr/bin/env python
import io
import os
import sys
from shutil import rmtree
from setuptools import setup, find_packages

# Package meta-data.
NAME = 'example'
DESCRIPTION = 'My short description for my project.'
URL = 'https://github.com/altereg0/3EQ4MRKk'
EMAIL = 'me@example.com'
AUTHOR = 'alter'
REQUIRES_PYTHON = '>=3.5.0'
VERSION = None
KEYWORDS = "falcon oauth"
# What packages are required for this module to be executed?
REQUIRED = [
    'falcon>=1.4.1',
    'gunicorn>=19.6.0',
    'docopt>=0.6.2',
    'jsonschema>=2.5.1',
    'sqlalchemy>=1.1.4',
    'aumbry[yaml]>=0.7.0'
]

# What packages are optional?
EXTRAS = {
    # 'fancy feature': ['django'],
}

# The rest you shouldn't have to touch too much :)
# ------------------------------------------------
# Except, perhaps the License and Trove Classifiers!
# If you do change the License, remember to change the Trove Classifier for that!

here = os.path.abspath(os.path.dirname(__file__))

# Import the README and use it as the long-description.
# Note: this will only work if 'README.md' is present in your MANIFEST.in file!
try:
    with io.open(os.path.join(here, 'README.rst'), encoding='utf-8') as f:
        long_description = '\n' + f.read()
except FileNotFoundError:
    long_description = DESCRIPTION

# Load the package's __version__.py module as a dictionary.
about = {}
if not VERSION:
    with open(os.path.join(here, NAME, '__version__.py')) as f:
        exec(f.read(), about)
else:
    about['__version__'] = VERSION

setup(
    name=NAME,
    version=about['__version__'],
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type='text/x-rst',
    author=AUTHOR,
    author_email=EMAIL,
    keywords=KEYWORDS,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    packages=find_packages(exclude=['contrib', 'docs', 'test*']),
    # If your package is a single module, use this instead of 'packages':
    # py_modules=['mypackage'],
    install_requires=REQUIRED,
    extras_require=EXTRAS,
    include_package_data=True,
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
    ],
    package_data={},
    data_files=[],
    # entry_points={
    #     'console_scripts': ['mycli=mymodule:cli'],
    # },
    entry_points={
        'console_scripts': [
            'falcon-example = example.__main__:main'
        ],
    },
)
