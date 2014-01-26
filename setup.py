#!/usr/bin/env python2.7

from sys import exit

from setuptools import setup, find_packages
from setuptools.command.install import install

version = '0.4.1'

def pre_install():
    print("Checking for libctesseract.")

    try:
        from tightocr import library_ctess
    except:
        print("The libctesseract shared-library could not be found/imported.")
        exit(1)

    print("Checking for liblept.")

    try:
        from tightocr import library_lept
    except:
        print("The liblept shared-library could not be found/imported.")
        exit(1)

def post_install():
    pass

class custom_install(install):
    def run(self):
        pre_install()
        install.run(self)
        post_install()

setup(name='tightocr',
      version=version,
      description="Thin and pleasant wrapper for Tesseract OCR.",
      long_description="""\
A thin (non-SWiG) wrapper for Tesseract OCR using CTesseract.""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='ocr tesseract ctesseract',
      author='Dustin Oprea',
      author_email='myselfasunder@gmail.com',
      url='https://github.com/dsoprea/TightOCR',
      license='GPL 2',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=True,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      cmdclass={'install': custom_install
               },
      )
