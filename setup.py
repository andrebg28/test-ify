from setuptools import setup, find_packages

setup(
    name="test-ify",
    version="0.0.1",
    description="Micro-framework de testes unitários minimalista",
    long_description=open("README.md","r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="Andre Luiz",
    author_email="andreluizmb28@gmail.com",
    url="https://github.com/andreluizmb82/micro_test.git",
    packages=find_packages(exclude=["tests*"]),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.12",
)