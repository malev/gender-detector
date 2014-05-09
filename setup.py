from distutils.core import setup
from gender_detector import version

version = '.'.join([str(x) for x in version])

setup(name='gender-detector',
    version = version,
    description = "Gender detection library",
    author = "Marcos Vanetta",
    author_email = "marcosvanetta@gmail.com",
    url = "http://codingnews.org",
    license = 'GPL2',
    keywords = "gender detection",
    packages = ['gender_detector', 'gender_detector.tests'],
    package_data = {
        'gender_detector': ['data/*.csv']
    }
)