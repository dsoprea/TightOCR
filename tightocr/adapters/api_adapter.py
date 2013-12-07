from ctypes import byref, c_bool, c_int, byref, POINTER

from tightocr import types
#from tightocr.types import TessApi, TessPageIterator, TessString, \
#                           TessMrIterator
from tightocr.calls.api_calls import *
from tightocr import simple_ptr_result_checker, simple_boolean_error_checker

#from tightocr.adapters.lept_adapter import pix_read


class _ResourceWrapper(object):
    def __init__(self, data, close_cb):
        self.__data = data
        self.__close_cb = close_cb

    def __del__(self):
        close_cb(self.__data)

    @property
    def data(self):
        return self.__data


class TessApi(object):
    def __init__(self, data_path, language):
        assert(language is not None)

        api = types.TessApi()

        # The result is automatically checked.
        c_tess_create(data_path, language, byref(api))

        self.__api = api

    def __del__(self):
        c_tess_destroy(byref(self.__api))

    @classmethod
    def version(cls):
        return c_tess_version()

    def get_init_languages_as_string(self):
        str_ = c_tess_get_init_languages_as_string(byref(self.__api))

        simple_ptr_result_checker(str_)
        return str_

    @classmethod
    def make_tess_ocr_row(cls, baseline, xheight, descender, ascender):

        result = TessRow()
        c_tess_make_tess_ocr_row(baseline, 
                                 xheight, 
                                 descender, 
                                 ascender, 
                                 byref(result))

        return result

    @classmethod
    def make_tblob(cls, pix):
        result = TessBlob()
        c_tess_make_tblob(byref(result), byref(result))

        return result

    @classmethod
    def delete_block_list(cls, blocks):
        c_tess_delete_block_list(byref(blocks))

    @classmethod
    def delete_string(cls, text):
        c_tess_delete_string(text)

    def init_lang_mod(self, data_path, language):
        c_tess_init_lang_mod(byref(self.__api), data_path, language)

    def set_page_seg_mode(self, mode):
        c_tess_set_page_seg_mode(byref(self.__api), mode)

    def get_page_seg_mode(self):
        return c_tess_get_page_seg_mode(byref(self.__api))

    def clear_adaptive_classifier(self):
        c_tess_clear_adaptive_classifier(byref(self.__api))

    def set_image_pix(self, pix):
        c_tess_set_image_pix(byref(self.__api), pix)

    def set_source_resolution(self, ppi):
        c_tess_set_source_resolution(byref(self.__api), pp)

    def set_rectangle(self, left, top, width, height):
        c_tess_set_rectangle(byref(self.__api), left, top, width, height)

    def get_thresholded_image(self):
        return c_tess_get_thresholded_image(byref(self.__api))

    def get_regions(self, return_pixa=False):
        if return_pixa is True:
            pixa_p = PixaP()
            pixa_p_parm = byref(pixa_p)
        else:
            pixa_p = None
            pixa_p_parm = None
            
        boxa_p = c_tess_get_regions(byref(self.__api), pixa_p_parm)

        simple_ptr_result_checker(boxa_p)
# TODO: Wrap results to be freed.
        return (boxa_p, pixa_p)

    def get_text_lines(self, return_pixa=False, return_block_ids=False):

        if return_pixa is True:
            pixa_p = TessPixaP()
            pixa_p_parm = byref(pixa_p)
        else:
            pixa_p = None
            pixa_p_parm = None

        if return_block_ids is True:
            block_ids_p = POINTER(c_int)()
            block_ids_p_parm = byref(block_ids_p)
        else:
            block_ids_p = None
            block_ids_p_parm = None

        block_ids_p = POINTER(c_int)()
        boxa_p = c_tess_get_text_lines(byref(self.__api), 
                                       pixa_p_parm, 
                                       block_ids_p_parm)

        simple_ptr_result_checker(boxa_p)
# TODO: Wrap results to be freed.
        return (boxa_p, pixa_p, block_ids_p)

    def get_strips(self, return_pixa=False, return_block_ids=False):

        if return_pixa is True:
            pixa_p = TessPixaP()
            pixa_p_parm = byref(pixa_p)
        else:
            pixa_p = None
            pixa_p_parm = None

        if return_block_ids is True:
            block_ids_p = POINTER(c_int)()
            block_ids_p_parm = byref(block_ids_p)
        else:
            block_ids_p = None
            block_ids_p_parm = None

        boxa_p = c_tess_get_strips(byref(self.__api), 
                                   pixa_p_parm, 
                                   block_ids_parm)

        simple_ptr_result_checker(boxa_p)
# TODO: Wrap results to be freed.
        return (boxa_p, pixa_p, block_ids_p)

    def get_words(self, return_pixa=False):

        if return_pixa is True:
            pixa_p = PixaP()
            pixa_p_parm = byref(pixa_p)
        else:
            pixa_p = None
            pixa_p_parm = None

        boxa_p = c_tess_get_words(byref(self.__api), pixa_p_parm)

        simple_ptr_result_checker(boxa_p)
# TODO: Wrap results to be freed.
        return (boxa_p, pixa_p)

    def get_connected_components(self, return_pixa=False):
        if return_pixa is True:
            pixa_p = PixaP()
            pixa_p_parm = byref(pixa_p)
        else:
            pixa_p = None
            pixa_p_parm = None

        boxa_p = c_tess_get_connected_components(byref(self.__api), 
                                                 pixa_p_parm)

        simple_ptr_result_checker(boxa_p)
# TODO: Wrap results to be freed.
        return (boxa_p, pixa_p)

    def get_component_images(self, level, text_only_int, return_pixa=False, 
                             return_block_ids=False):

        if return_pixa is True:
            pixa_p = TessPixaP()
            pixa_p_parm = byref(pixa_p)
        else:
            pixa_p = None
            pixa_p_parm = None

        if return_block_ids is True:
            block_ids_p = POINTER(c_int)()
            block_ids_p_parm = byref(block_ids_p)
        else:
            block_ids_p = None
            block_ids_p_parm = None

        boxa_p = c_tess_get_component_images(byref(self.__api), 
                                             level, 
                                             bool(text_only_int),
                                             pixa_p_parm, 
                                             block_ids_p_parm)

        simple_ptr_result_checker(boxa_p)
# TODO: Wrap results to be freed.
        return (boxa_p, pixa_p, block_ids_p)

    def get_thresholded_image_scale_factor(self):
        return c_tess_get_thresholded_image_scale_factor(byref(self.__api))

    def dump_pgm(self, filename):
        c_tess_dump_pgm(byref(self.__api), filename)

    def analyse_layout(self):
        page_it = TessPageIterator()
        c_tess_analyse_layout(byref(self.__api), byref(page_it))
        return page_it

    def recognize(self):
        c_tess_recognize(byref(self.__api))

    def process_pages_string(self, filename, retry_config, timeout_millisec):
        text_out = TessString()
        result = c_tess_process_pages_string(filename, retry_config, 
                                             timeout_millisec, byref(text_out))
        if result == 0:
            raise ValueError("process_pages_string failed.")

        return str_out

    def process_page_string(self, pix, page_index, filename, retry_config, 
                            timeout_millisec):

        text_out = TessString()
        c_tess_process_page_string(byref(self.__api), pix, page_index, 
                                   filename, retry_config, timeout_millisec, 
                                   byref(text_out))

        return text_out

    def get_iterator(self):
        mr_iterator = TessMrIterator()
        c_tess_get_iterator(byref(self.__api), byref(mr_iterator))
        return mr_iterator

    def get_utf8_text(self):
        str_ = c_tess_get_utf8_text(byref(self.__api))
        simple_ptr_result_checker(str_)
        return str_

    def get_hocr_text(self, page_number):
        str_ = c_tess_get_hocr_text(byref(self.__api), page_number)
        simple_ptr_result_checker(str_)
        return str_

    def get_box_text(self, page_number):
        str_ = c_tess_get_box_text(byref(self.__api), page_number)
        simple_ptr_result_checker(str_)
        return str_

    def get_unlv_text(self):
        str_ = c_tess_get_unlv_text(byref(self.__api), page_number)
        simple_ptr_result_checker(str_)
        return str_

    def mean_text_conf(self):
        return c_tess_mean_text_conf(byref(self.__api))

    def all_word_confidences(self):
# TODO: Post-process result.
        return c_tess_all_word_confidences(byref(self.__api))

    def adapt_to_word_str(self, mode, word_string):
        return c_tess_adapt_to_word_str(byref(self.__api), mode, word_string)

    def clear(self):
        c_tess_clear(byref(self.__api))

    def is_valid_word(self, word):
        is_valid = c_tess_is_valid_word(byref(self.__api), word)
        return bool(is_valid)

    def get_text_direction(self):
        offset = c_int()
        slope = c_float()

        result = c_tess_get_text_direction(byref(self.__api), 
                                           byref(offset), 
                                           byref(slope))

        simple_boolean_error_checker(result)
        return (offset, slope)

    def find_row_for_box(self, block_list, left, top, right, 
                         bottom):

        row = TessRow()
        c_tess_find_row_for_box(byref(self.__api), 
                                block_list,
                                left,
                                top,
                                right,
                                bottom,
                                byref(row))

        return row

    def get_unichar(self, unichar_id):
        str_ = c_tess_get_unichar(byref(self.__api), unichar_id)
        
        simple_ptr_result_checker(str_)
        return str_

    def set_min_orientation_margin(self, margin):
        c_tess_set_min_orientation_margin(byref(self.__api), margin)

    def get_block_text_orientations(self):

        block_orientation = POINTER(c_int)()
        vertifcal_writing = POINTER(c_bool)()

        c_tess_get_block_text_orientations(byref(self.__api), 
                                           byref(block_orientation), 
                                           vertical_writing)
# TODO: Needs to be freed.
        return (block_orientation, vertical_writing)

    def find_lines_create_block_list(self):
        result = TessBlockList()
        c_tess_find_lines_create_block_list(byref(self.__api), byref(result))
        return result

