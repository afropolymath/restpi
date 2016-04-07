from setuptools import setup

setup(
    name='restpi',
    version='0.1',
    description='Nifty Library written in Python for controlling Raspberry Pi based devices remotely.',
    url='http://github.com/andela-cnnadi/restpi',
    author='Chidiebere Nnadi',
    author_email='chidiebere.nnadi@gmail.com',
    license='MIT',
    packages=['restpi'],
    install_requires=[
        'flask',
        'flask_restful',
        'RPi.GPIO',
        'docopt',
        'PyYAML'
    ],
    test_suite='nose.collector',
    tests_require=['nose'],
    scripts=['bin/restpi'],
    zip_safe=False)
