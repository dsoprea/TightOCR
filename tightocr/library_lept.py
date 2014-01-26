from ctypes import cdll
from ctypes.util import find_library

_LEPT_FILEPATH = find_library('lept')
liblept = cdll.LoadLibrary(_LEPT_FILEPATH)

