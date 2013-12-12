from ctypes import Structure, POINTER, c_void_p, c_int

class TessApi(Structure):
    _fields_ = [('opaque', c_void_p)]

TessApiP = POINTER(TessApi)

class TessPix(Structure):
# TODO: Finish.
    _fields_ = []

TessPixP = POINTER(TessPix)

class TessPixa(Structure):
# TODO: Finish.
    _fields_ = []

TessPixaP = POINTER(TessPixa)

class TessBoxa(Structure):
# TODO: Finish.
    _fields_ = []

TessBoxaP = POINTER(TessBoxa)

class TessPageIterator(Structure):
# TODO: Finish.
    _fields_ = []

TessPageIteratorP = POINTER(TessPageIterator)

class TessMrIterator(Structure):
# TODO: Finish.
    _fields_ = []

TessMrIteratorP = POINTER(TessMrIterator)

class TessString(Structure):
# TODO: Finish.
    _fields_ = []

TessStringP = POINTER(TessString)

class TessBlockList(Structure):
# TODO: Finish.
    _fields_ = []

TessBlockListP = POINTER(TessBlockList)

class TessRow(Structure):
# TODO: Finish.
    _fields_ = []

TessRowP = POINTER(TessRow)

class TessBlob(Structure):
# TODO: Finish.
    _fields_ = []

TessBlobP = POINTER(TessBlob)

class TessMrIterator(Structure):
# TODO: Finish.
    _fields_ = [('iterator', c_void_p), 
                ('type', c_int)]

TessMrIteratorP = POINTER(TessMrIterator)

