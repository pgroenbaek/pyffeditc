from setuptools import setup, find_packages

setup(
    name="pyffeditc",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
    ],
    author="Peter Grønbæk Andersen",
    author_email="peter@grnbk.io",
    description="A Python wrapper for the ffeditc_unicode.exe utility.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    project_urls={
        "Homepage": "https://github.com/pgroenbaek/pytkutils",
        "Issues": "https://github.com/pgroenbaek/pytkutils/issues",
        "Source": "https://github.com/pgroenbaek/pytkutils",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)