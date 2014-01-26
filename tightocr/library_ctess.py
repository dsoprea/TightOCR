from ctypes import cdll
from ctypes.util import find_library

_TESS_FILEPATH = find_library('ctesseract')
if _TESS_FILEPATH is None:
    _TESS_FILEPATH = 'libctesseract.so'

libctess = cdll.LoadLibrary(_TESS_FILEPATH)

