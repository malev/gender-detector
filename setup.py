from distutils.core import setup
from gender_detector import version

version = '.'.join([str(x) for x in version])

setup(name='gender-detector',
    version=version,
    description="Gender detection library",
    author="Marcos Vanetta",
    author_email="Marcos Vanetta",
    url="http://codingnews.org",
    packages = ['gender_detector', 'gender_detector.tests'],
)