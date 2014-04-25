#!/usr/bin/env python2.7

import sys
sys.path.insert(0, '..')

import os
import logging

os.environ['DYLD_LIBRARY_PATH'] = '/usr/local/Cellar/tesseract/3.02.02/lib:/Users/dustin/development/cpp/ctesseract/build'

from tightocr.adapters.api_adapter import TessApi
from tightocr.adapters.lept_adapter import pix_read
from tightocr.constants import RIL_PARA

def configure_logging():
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    # create console handler and set level to debug
    ch = logging.StreamHandler()

    # create formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # add formatter to ch
    ch.setFormatter(formatter)

    # add ch to logger
    logger.addHandler(ch)

configure_logging()

t = TessApi(None, 'eng');

t.set_variable('tessedit_char_whitelist', '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ\'".,;?!/\\$-()&%@')

p = pix_read('receipt.png')
t.set_image_pix(p)
t.recognize()

confidence = t.mean_text_confidence()
if confidence < 60:
    raise Exception("Too much error: %d" % (confidence))

for block in t.iterate(RIL_PARA):
    print(block)

#    direction = t.get_text_direction()
#    print(t.get_hocr_text(1))
#    print(t.get_utf8_text())
