import os
import imp

from setuptools import setup, find_packages

setup(
    name="devnoah",
    version=imp.load_source("devnoah.version", os.path.join("devnoah", "version.py")).version,
    packages=find_packages(exclude=["tests", "tests.*"]),
    install_requires=[
        "requests",
        "requests_ntlm3",
    ],
    author="Deric Gape",
    author_email="gay@gmail.com",
    description="Gape",
    url="https://github.com/degagne/python-certsrv",
    keywords='ad adcs certsrv pki certificate',
    license="MIT",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: MIT License",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Security",
        "Topic :: System :: Systems Administration",
    ],
    python_requires=">=3.6",
)
