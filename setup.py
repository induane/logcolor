from setuptools import setup, find_packages


TESTS_REQUIRE = []
INSTALL_REQUIRES = []


setup(
    name="log_color",
    author="Brant Watson",
    author_email="oldspiceap@gmail.com",
    description="Simple log formatters for colored output",
    version="1.0.6",
    url="https://github.com/induane/logcolor",
    license="wtfpl",
    packages=find_packages('src'),
    package_dir={"": "src"},
    install_requires=INSTALL_REQUIRES,
    tests_require=TESTS_REQUIRE,
)
