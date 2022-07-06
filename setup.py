from setuptools import setup, find_packages


with open("README.md", "r") as README:
    long_description = README.read()


setup(
    name="proton",
    version="0.1.0",
    author="Nandanunni A S",
    author_email="asnqln@gmail.com",
    description="A proton sized python framework for building backend web applications",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Nandan-unni/proton-py",
    packages=find_packages(),
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=["gunicorn==20.0.4", "colorama==0.4.4"],
)


# python3 setup.py sdist bdist_wheel
# python3 -m twine upload --repository testpypi dist/*
# python3 -m twine upload --repository-url https://upload.pypi.org/legacy/ dist/*
