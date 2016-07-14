from setuptools import setup, find_packages


TESTS_REQUIRE = []
INSTALL_REQUIRES = []


setup(
    name="logcolor",
    version="1.0.0",
    packages=find_packages('src'),
    package_dir={"": "src"},
    install_requires=INSTALL_REQUIRES,
    tests_require=TESTS_REQUIRE,
)
