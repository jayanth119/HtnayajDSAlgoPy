from setuptools import setup, find_packages

setup(
    name="HtnayajDSAlgoPy",
    version="0.1.0",
    author="Jayanth Chukka",
    description="A Python package for data structures and algorithms",
    packages=find_packages(),
    install_requires=[
        "numpy" , "heapy" 
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
