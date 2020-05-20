from setuptools import setup, find_packages, Extension
NAME = 'caeli'

VERSION = '0.0.1'

DESCRIPTION = 'caeli'

LONG_DESCRIPTION = 'caeli, climate indices, drought indices (spi, spei, etc.)'

CLASSIFIERS = [  # https://pypi.python.org/pypi?:action=list_classifiers
    'Development Status :: 4 - Beta',
    'Environment :: Console',
    'Intended Audience :: Science/Research',
    'License :: OSI Approved :: MIT License',
    'Natural Language :: English',
    'Operating System :: OS Independent',
    'Programming Language :: Python :: 3',
    'Topic :: Scientific/Engineering :: Hydrology'
]

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    classifiers=CLASSIFIERS,
    author='Jackson Roehrig',
    author_email='Jackson.Roehrig@th-koeln.de',
    maintainer='Jackson.Roehrig@th-koeln.de',
    license='MIT',
    download_url='https://github.com/JRoehrig/caeli',
    packages=find_packages(),
    install_requires=['python-dateutil', 'numpy', 'scipy', 'pandas'],
    ext_modules=[],
    scripts=[]
)
