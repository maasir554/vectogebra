# NOTE:-
# every time you want to compile(build/ditributre)
# change the version 
# and run $ python -m build
# to upload : twine upload dist/*
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="vectogebra",
    version="0.0.10",
    author="Mohammad Maasir",
    license="MIT",
    author_email="maasir554@gmail.com",
    description="Package that helps you work with vector algebra !",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/maasir554/vectogebra",
    project_urls={
        "Bug Tracker": "https://github.com/maasir554/vectogebra/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)