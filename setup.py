from setuptools import setup, find_packages

setup(
    name="lstty",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "pyserial",
        "click"
    ],
    entry_points={
        "console_scripts": [
            "lstty=lstty.cli:main"
        ]
    },
    author="Ziv Barcesat",
    author_email="info@magrathea.co.il",
    description="A tool for listing serial ports with detailed information.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/barcesat/lstty",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
