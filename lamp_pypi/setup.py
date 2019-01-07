try:
    from setuptools import setup, find_packages

except ImportError:
    from distutils.core import setup



setup(
    name = 'lamp',
    version = '0.0.1',
    keywords = ['lamp', 'utils', 'try'],
    description = 'just for fun',
    license = 'MIT License',

    url = 'https://github.com/kerwin6182828/kerwin_code_files',
    author = 'kerwin',
    author_email = 'kerwin19950830@gmail.com',

    packages = find_packages(where=".", exclude=(), include=("*",)),
    install_requires = ["numpy"],
    include_package_data = True,
    platforms = 'any',
    long_description = 'just learn it, nothing special function...   ',
)

