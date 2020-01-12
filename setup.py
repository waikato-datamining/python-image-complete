# setup.py
# Copyright (C) 2019-2020 University of Waikato, Hamilton, NZ

from setuptools import setup


def _read(f):
    """
    Reads in the content of the file.
    :param f: the file to read
    :type f: str
    :return: the content
    :rtype: str
    """
    return open(f, 'rb').read()


setup(
    name="python-image-complete",
    description="Python3 library for checking whether images are complete.",
    long_description=(
        _read('DESCRIPTION.rst') + b'\n' +
        _read('CHANGES.rst')).decode('utf-8'),
    url="https://github.com/waikato-datamining/python-image-complete",
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Topic :: Multimedia :: Graphics',
        'Programming Language :: Python :: 3',
    ],
    license='MIT License',
    package_dir={
        '': 'src'
    },
    packages=[
        "image_complete",
    ],
    version="0.0.2",
    author='Peter Reutemann',
    author_email='fracpete@waikato.ac.nz',
)
