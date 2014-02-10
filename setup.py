try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'An implementation of finding the median of a list of numbers from a stream',
    'author': 'Archit Baweja',
    'url': 'https://github.com/archit/median_finder'
    'download_url': 'https://github.com/archit/median_finder.git',
    'author_email': 'architbaweja@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['median_finder'],
    'scripts': [],
    'name': 'median_finder'
}

setup(**config)
