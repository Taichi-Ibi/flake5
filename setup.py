import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="flake5",
    version="0.0.2",
    author="t.ibi",
    author_email="t.ibi@estyle-inc.jp",
    description="search unnecessary imports in ipynb file",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Taichi-Ibi/flake5",
    packages=setuptools.find_packages(),
    entry_points={"console_scripts": ["flake5 = flake5:flake5"]},
    python_requires=">=3.8",
)
