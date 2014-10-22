from setuptools import setup

setup(
    name="pyntercom",
    version="0.0.1",
    description="Python HTTP client for Intercom.io",
    long_description=open("README.md").read(),
    keywords="python, intercom.io",
    author="Jared Morse",
    author_email="jarcoal@gmail.com",
    url="https://github.com/jarcoal/pyntercom",
    license="MIT",
    packages=["pyntercom"],
    install_requires=["requests"],
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)