Introduction
============

TightOCR provides a thin library to provide an efficient, pleasant, Pythonic 
interface to Tesseract. Tesseract (https://code.google.com/p/tesseract-ocr/) 
is the world's most universal OCR project, owned by Google. 

The primary goals of this implementation is to provide
the following functionalities to Python:

> OCR a document and return a block of text.
> OCR a document, and identify the various parts of a document to allow an
  application to take advantage of Tesseract's layout analysis.

Secondary functions that are available:

> Confidence of recognition
> HTML-formatted output
> Slope and margin of text

Though I have tried to provide access to as many of the API methods as 
possible, there is a very limited amount of documentation available, so many
of the more exotic functions haven't been properly tested. IF YOU WANT TO HELP
WITH THIS, JUST DO IT AND REGISTER ISSUES OR SUBMIT PULL-REQUESTS.


This library was built as an alternative to python-tesseract 
(http://code.google.com/p/python-tesseract) for the following reasons:

> The usage of SWIG produces an implementation that is excessive and 
  burdensome.
> python-tesseract is, ironically, incomplete. You are unable to enumerate the
  parts of the document (getIterator() is broken: 
  http://code.google.com/p/python-tesseract/issues/detail?id=50&can=4&sort=-id)


Requirements
============

CTesseract (https://github.com/dsoprea/CTesseract)
Leptonica (http://code.google.com/p/leptonica/)


Installation
============

The Leptonica and CTesseract shared-libraries (liblept.so, 
libctesseract.so) must be findable.


Usage
=====

Return the whole document as text:

    from tightocr.adapters.api_adapter import TessApi
    from tightocr.adapters.lept_adapter import pix_read

    t = TessApi(None, 'eng');

    p = pix_read('receipt.png')
    t.set_image_pix(p)

    t.recognize()
    if t.mean_text_confidence() < 85:
        raise Exception("Too much error.")

    print(t.get_utf8_text())

Enumerate individual blocks of text (referred to as "paragraphs"), driven by 
the document's layout:

    from tightocr.adapters.api_adapter import TessApi
    from tightocr.adapters.lept_adapter import pix_read
    from tightocr.constants import RIL_PARA

    t = TessApi(None, 'eng');
    p = pix_read('receipt.png')
    t.set_image_pix(p)
    t.recognize()

    if t.mean_text_confidence() < 85:
        raise Exception("Too much error.")

    for block in t.iterate(RIL_PARA):
        print block

