import codecs
import os
import re

from setuptools import find_packages, setup


###############################################################################

NAME = "postcodes-io-simple"
PACKAGES = find_packages(where="postcodes_io")
META_PATH = os.path.join("postcodes_io", "__init__.py")
KEYWORDS = ["uk", "postcode", "geocode", "coordinates", "latitude" "longitude" "postcodesio" "royalmail"]
PROJECT_URLS = {
    "Documentation": "https://github.com/raigad/python-postcodes-io",
    "Bug Tracker": "https://github.com/raigad/python-postcodes-io/issues",
    "Source Code": "https://github.com/raigad/python-postcodes-io",
}
CLASSIFIERS = [
    "Development Status :: 5 - Production/Stable",
    "Intended Audience :: Developers",
    "Natural Language :: English",
    "Programming Language :: Python",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.4",
    "Programming Language :: Python :: 3.5",
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: Implementation :: PyPy",
    "Topic :: Software Development :: Libraries :: Python Modules",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
]
INSTALL_REQUIRES = []


###############################################################################

HERE = os.path.abspath(os.path.dirname(__file__))


def read(*parts):
    """
    Build an absolute path from *parts* and and return the contents of the
    resulting file.  Assume UTF-8 encoding.
    """
    with codecs.open(os.path.join(HERE, *parts), "rb", "utf-8") as f:
        return f.read()


META_FILE = read(META_PATH)


def find_meta(meta):
    """
    Extract __*meta*__ from META_FILE.
    """
    meta_match = re.search(
        r"^__{meta}__ = ['\"]([^'\"]*)['\"]".format(meta=meta), META_FILE, re.M
    )
    if meta_match:
        return meta_match.group(1)
    raise RuntimeError("Unable to find __{meta}__ string.".format(meta=meta))


VERSION = find_meta("version")
URL = find_meta("url")
LONG = (
    read("README.md")
    + "\n\n"
)


if __name__ == "__main__":
    setup(
        name=NAME,
        description=find_meta("description"),
        license=find_meta("license"),
        url=URL,
        project_urls=PROJECT_URLS,
        version=VERSION,
        author=find_meta("author"),
        author_email=find_meta("email"),
        maintainer=find_meta("author"),
        maintainer_email=find_meta("email"),
        keywords=KEYWORDS,
        long_description=LONG,
        packages=PACKAGES,
        package_dir={"": "postcodes_io"},
        zip_safe=False,
        classifiers=CLASSIFIERS,
        install_requires=INSTALL_REQUIRES,
        include_package_data=True,
    )

"""
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="postcodes-io-simple",
    version="0.0.1",
    author="Rohit Deshmukh",
    author_email="raigad1630@gmail.com",
    description="A Python Wrapper for postcodes.io",
    long_description=long_description,
    license='MIT',
    keywords='uk postcode geocode coordinates latitude longitude postcodesio royalmail',
    python_requires='>=3',
    url="https://github.com/raigad/python-postcodes-io",
    packages=setuptools.find_packages(exclude=['contrib', 'docs']),
    classifiers=[
        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
"""
