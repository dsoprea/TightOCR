from tightocr.calls.lept_calls import c_lept_pix_read
from tightocr.types import TessPixP
from tightocr import simple_ptr_result_checker

def pix_read(file_path):
    pix_p = c_lept_pix_read(file_path)
    simple_ptr_result_checker(pix_p)

    return pix_p

