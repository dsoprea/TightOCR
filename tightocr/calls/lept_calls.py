from ctypes import c_char_p

from tightocr.library_lept import liblept
from tightocr.types import TessPixP

c_lept_pix_read = liblept.pixRead
c_lept_pix_read.argtypes = [c_char_p]
c_lept_pix_read.restype = TessPixP

