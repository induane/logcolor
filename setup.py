from setuptools import setup, find_packages

long_description = (
    "Logging formatters for colorized outputs. A simple domain specific "
    "language for log messages which can be used to colorize all or part of "
    "a particular log message. For example:\n\n"
    "LOG.debug('Found file at #g<%s>', path)\n\n"
    "would colorize the contents of the 'path' variable green when output to "
    "a command line terminal.\n\nA formatter which strips color sequences "
    "from the output is also included for situations like logging to files "
    "where it would not make sense to have ANSI color sequences embedded in "
    "the output."
)

setup(
    name="log_color",
    author="Brant Watson",
    author_email="oldspiceap@gmail.com",
    description="Simple log formatters for colored output",
    long_description=long_description,
    version="1.0.7",
    url="https://github.com/induane/logcolor",
    license="wtfpl",
    packages=find_packages("src"),
    package_dir={"": "src"},
    python_requires=">2.7, !=3.0.*, !=3.1.*, !=3.2.*",
)
