from ctypes import cdll

_LEPT_FILEPATH = "libtesseract.so"
liblept = cdll.LoadLibrary(_LEPT_FILEPATH)

