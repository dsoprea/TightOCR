from sys import exit

from setuptools import setup, find_packages
from setuptools.command.install import install

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

class custom_install(install):
    def run(self):
        pre_install()
        install.run(self)

long_description = "A thin (non-SWiG) wrapper for Tesseract OCR using "\
                   "CTesseract."

setup(name='tightocr',
      version='0.4.4',
      description="Thin and pleasant wrapper for Tesseract OCR.",
      long_description=long_description,
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='ocr tesseract ctesseract',
      author='Dustin Oprea',
      author_email='myselfasunder@gmail.com',
      url='https://github.com/dsoprea/TightOCR',
      license='GPL 2',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=True,
      install_requires=[],
      cmdclass={ 'install': custom_install },
)
