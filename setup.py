import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    desc_long = f.read()

desc_short = "A package of helper functions."

setuptools.setup(
    name="dedejavu_squage",
    version="0.1.0",
    author="squage",
    author_email="",
    description=desc_short,
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src", exclude=["tests"]),


)
