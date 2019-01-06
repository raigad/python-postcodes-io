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
    packages=setuptools.find_packages(exclude=['contrib', 'docs', 'tests*']),
    classifiers=[
        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
