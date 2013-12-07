from ctypes import cdll

_TESS_FILEPATH = "libctesseract.so"
libctess = cdll.LoadLibrary(_TESS_FILEPATH)

