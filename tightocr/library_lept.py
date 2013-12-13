from ctypes import cdll

_LEPT_FILEPATH = "liblept.so"
liblept = cdll.LoadLibrary(_LEPT_FILEPATH)

