from ctypes import cdll
from ctypes.util import find_library

_LEPT_FILEPATH = find_library('lept')
if _LEPT_FILEPATH is None:
    _LEPT_FILEPATH = 'liblept.so'

liblept = cdll.LoadLibrary(_LEPT_FILEPATH)

