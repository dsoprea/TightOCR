from ctypes import cdll
from ctypes.util import find_library

_TESS_FILEPATH = find_library('ctesseract')
libctess = cdll.LoadLibrary(_TESS_FILEPATH)

