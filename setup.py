from setuptools import setup, find_packages
import os

# Utility function to read the README file.
# Used for the long_description. It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='geodjango-tigerline',
    version='1.0',
    description='A resuable app with the boilerplate necessary for getting TIGER/LINE data into a GeoDjango project.',
    author='Adam Fast',
    author_email='adamfast@gmail.com',
    url='https://github.com/adamfast/geodjango-tigerline',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    long_description=read('README'),
    license = "BSD",
    keywords = "django geodjango tigerline",
    classifiers = [
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
