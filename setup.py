import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="amobee-api-client",
    version="0.1.dev0",
    author="Matt Artingstall",
    author_email="matt@imagndesign.com",
    description="Simple wrapper for Amobee API",
    url="https://github.com/martingstall/amobee-api-client",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 2.7.3",
        "License :: GNU GENERAL PUBLIC LICENSE",
        "Operating System :: OS Independent",
    ],
)