from ctypes import POINTER, c_int, c_char_p, c_void_p, c_ubyte, c_float, \
                   c_double

from tightocr.library_ctess import libctess
from tightocr.types import TessApiP, TessPixaP, TessPixP, TessBoxaP, \
                           TessPageIteratorP, TessMrIteratorP, TessStringP, \
                           TessBlockListP, TessRowP, TessBlobP, TessMrIteratorP

from tightocr import simple_nonzero_result_checker, \
                     simple_more_than_zero_result_checker

c_tess_create = libctess.tess_create
c_tess_create.argtypes = [c_char_p, c_char_p, TessApiP]
c_tess_create.restype = simple_nonzero_result_checker

c_tess_destroy = libctess.tess_destroy
c_tess_destroy.argtypes = [TessApiP]
c_tess_destroy.restype = simple_nonzero_result_checker

c_tess_version = libctess.tess_version
c_tess_version.argtypes = []
c_tess_version.restype = c_char_p

c_tess_get_init_languages_as_string = \
    libctess.tess_get_init_languages_as_string
c_tess_get_init_languages_as_string.argtypes = [TessApiP]
c_tess_get_init_languages_as_string.restype = c_char_p

c_tess_init_lang_mod = libctess.tess_init_lang_mod
c_tess_init_lang_mod.argtypes = [TessApiP, c_char_p, c_char_p]
c_tess_init_lang_mod.restype = simple_nonzero_result_checker

c_tess_set_page_seg_mode = libctess.tess_set_page_seg_mode
c_tess_set_page_seg_mode.argtypes = [TessApiP, c_int]
c_tess_set_page_seg_mode.restype = simple_nonzero_result_checker

c_tess_get_page_seg_mode = libctess.tess_get_page_seg_mode
c_tess_get_page_seg_mode.argtypes = [TessApiP]
c_tess_get_page_seg_mode.restype = simple_nonzero_result_checker

#c_tess_tesseract_rect = libctess.tess_tesseract_rect
#c_tess_tesseract_rect.argtypes = [TessApiP, POINTER(c_ubyte), c_int, c_int, 
#                                  c_int, c_int, c_int, c_int]
#c_tess_tesseract_rect.restype = c_char_p

c_tess_clear_adaptive_classifier = libctess.tess_clear_adaptive_classifier
c_tess_clear_adaptive_classifier.argtypes = [TessApiP]
c_tess_clear_adaptive_classifier.restype = simple_nonzero_result_checker

#c_tess_set_image_details = libctess.tess_set_image_details
#c_tess_set_image_details.argtypes = [TessApiP, POINTER(c_ubyte), c_int, c_int, 
#                                     c_int, c_int]
#c_tess_set_image_details.restype = simple_nonzero_result_checker

c_tess_set_image_pix = libctess.tess_set_image_pix
c_tess_set_image_pix.argtypes = [TessApiP, TessPixP]
c_tess_set_image_pix.restype = simple_nonzero_result_checker

c_tess_set_source_resolution = libctess.tess_set_source_resolution
c_tess_set_source_resolution.argtypes = [TessApiP, c_int]
c_tess_set_source_resolution.restype = simple_nonzero_result_checker

c_tess_set_rectangle = libctess.tess_set_rectangle
c_tess_set_rectangle.argtypes = [TessApiP, c_int, c_int, c_int, c_int]
c_tess_set_rectangle.restype = simple_nonzero_result_checker

c_tess_get_thresholded_image = libctess.tess_get_thresholded_image
c_tess_get_thresholded_image.argtypes = [TessApiP]
c_tess_get_thresholded_image.restype = TessPixaP

c_tess_get_regions = libctess.tess_get_regions
c_tess_get_regions.argtypes = [TessApiP, POINTER(TessPixaP)]
c_tess_get_regions.restype = TessBoxaP

c_tess_get_text_lines = libctess.tess_get_text_lines
c_tess_get_text_lines.argtypes = [TessApiP, 
                                  POINTER(TessPixaP), 
                                  POINTER(POINTER(c_int))]
c_tess_get_text_lines.restype = TessBoxaP

c_tess_get_strips = libctess.tess_get_strips
c_tess_get_strips.argtypes = [TessApiP, 
                              POINTER(TessPixaP), 
                              POINTER(POINTER(c_int))]
c_tess_get_strips.restype = TessBoxaP

c_tess_get_words = libctess.tess_get_words
c_tess_get_words.argtypes = [TessApiP, POINTER(TessPixaP)]
c_tess_get_words.restype = TessBoxaP

c_tess_get_connected_components = libctess.tess_get_connected_components
c_tess_get_connected_components.argtypes = [TessApiP, POINTER(TessPixaP)]
c_tess_get_connected_components.restype = TessBoxaP

c_tess_get_component_images = libctess.tess_get_component_images
c_tess_get_component_images.argtypes = [TessApiP, 
                                        c_int, 
                                        c_int, 
                                        POINTER(TessPixaP), 
                                        POINTER(POINTER(c_int))]
c_tess_get_component_images.restype = TessBoxaP

c_tess_get_thresholded_image_scale_factor = \
    libctess.tess_get_thresholded_image_scale_factor
c_tess_get_thresholded_image_scale_factor.argtypes = [TessApiP]
c_tess_get_thresholded_image_scale_factor.restype = simple_nonzero_result_checker

c_tess_dump_pgm = libctess.tess_dump_pgm
c_tess_dump_pgm.argtypes = [TessApiP, c_char_p]
c_tess_dump_pgm.restype = simple_nonzero_result_checker

c_tess_analyse_layout = libctess.tess_analyse_layout
c_tess_analyse_layout.argtypes = [TessApiP, TessPageIteratorP]
c_tess_analyse_layout.restype = simple_nonzero_result_checker

c_tess_recognize = libctess.tess_recognize
c_tess_recognize.argtypes = [TessApiP]
c_tess_recognize.restype = simple_nonzero_result_checker

c_tess_process_pages_string = libctess.tess_process_pages_string
c_tess_process_pages_string.argtypes = [TessApiP, c_char_p, c_char_p, c_int, 
                                        TessStringP]
c_tess_process_pages_string.restype = c_int

c_tess_process_page_string = libctess.tess_process_page_string
c_tess_process_page_string.argtypes = [TessApiP, 
                                       TessPixP,
                                       c_int, 
                                       c_char_p,
                                       c_char_p,
                                       c_int,
                                       TessStringP]
c_tess_process_page_string.restype = c_int

c_tess_get_iterator = libctess.tess_get_iterator
c_tess_get_iterator.argtypes = [TessApiP, TessMrIteratorP]
c_tess_get_iterator.restype = simple_nonzero_result_checker

c_tess_get_utf8_text = libctess.tess_get_utf8_text
c_tess_get_utf8_text.argtypes = [TessApiP]
c_tess_get_utf8_text.restype = c_void_p

c_tess_get_hocr_text = libctess.tess_get_hocr_text
c_tess_get_hocr_text.argtypes = [TessApiP, c_int]
c_tess_get_hocr_text.restype = c_char_p

c_tess_get_box_text = libctess.tess_get_box_text
c_tess_get_box_text.argtypes = [TessApiP, c_int]
c_tess_get_box_text.restype = c_char_p

c_tess_get_unlv_text = libctess.tess_get_unlv_text
c_tess_get_unlv_text.argtypes = [TessApiP]
c_tess_get_unlv_text.restype = c_char_p

c_tess_mean_text_conf = libctess.tess_mean_text_conf
c_tess_mean_text_conf.argtypes = [TessApiP]
c_tess_mean_text_conf.restype = c_int

c_tess_all_word_confidences = libctess.tess_all_word_confidences
c_tess_all_word_confidences.argtypes = [TessApiP]
c_tess_all_word_confidences.restype = POINTER(c_int)

c_tess_adapt_to_word_str = libctess.tess_adapt_to_word_str
c_tess_adapt_to_word_str.argtypes = [TessApiP, c_int, c_char_p]
c_tess_adapt_to_word_str.restype = c_int

c_tess_clear = libctess.tess_clear
c_tess_clear.argtypes = [TessApiP]
c_tess_clear.restype = simple_nonzero_result_checker

c_tess_is_valid_word = libctess.tess_is_valid_word
c_tess_is_valid_word.argtypes = [TessApiP, c_char_p]
c_tess_is_valid_word.restype = c_int

c_tess_get_text_direction = libctess.tess_get_text_direction
c_tess_get_text_direction.argtypes = [TessApiP, 
                                      POINTER(c_int), 
                                      POINTER(c_float)]
c_tess_get_text_direction.restype = c_int

c_tess_find_row_for_box = libctess.tess_find_row_for_box
c_tess_find_row_for_box.argtypes = [TessApiP, 
                                    TessBlockListP,
                                    c_int,
                                    c_int,
                                    c_int,
                                    c_int,
                                    TessRowP]
c_tess_find_row_for_box.restype = simple_nonzero_result_checker

c_tess_get_unichar = libctess.tess_get_unichar
c_tess_get_unichar.argtypes = [TessApiP, c_int]
c_tess_get_unichar.restype = c_char_p

c_tess_make_tess_ocr_row = libctess.tess_make_tess_ocr_row
c_tess_make_tess_ocr_row.argtypes = [c_float, 
                                     c_float, 
                                     c_float, 
                                     c_float, 
                                     TessRowP]
c_tess_make_tess_ocr_row.restype = simple_nonzero_result_checker

c_tess_make_tblob = libctess.tess_make_tblob
c_tess_make_tblob.argtypes = [TessPixP, TessBlobP]
c_tess_make_tblob.restype = simple_nonzero_result_checker

c_tess_set_min_orientation_margin = libctess.tess_set_min_orientation_margin
c_tess_set_min_orientation_margin.argtypes = [TessApiP, c_double]
c_tess_set_min_orientation_margin.restype = simple_nonzero_result_checker

c_tess_get_block_text_orientations = libctess.tess_get_block_text_orientations
c_tess_get_block_text_orientations.argtypes = [TessApiP, 
                                               POINTER(POINTER(c_int)),
                                               POINTER(c_void_p),
                                               POINTER(c_int)]
c_tess_get_block_text_orientations.restype = simple_nonzero_result_checker

c_tess_find_lines_create_block_list = \
    libctess.tess_find_lines_create_block_list
c_tess_find_lines_create_block_list.argtypes = [TessApiP, TessBlockListP]
c_tess_find_lines_create_block_list.restype = simple_nonzero_result_checker

c_tess_delete_block_list = libctess.tess_delete_block_list
c_tess_delete_block_list.argtypes = [TessBlockListP]
c_tess_delete_block_list.restype = simple_nonzero_result_checker

c_tess_delete_string = libctess.tess_delete_string
c_tess_delete_string.argtypes = [c_char_p]
c_tess_delete_string.restype = simple_nonzero_result_checker

# Handler for MR iterator.

c_tess_mr_it_next = libctess.tess_mr_it_next
c_tess_mr_it_next.argtypes = [TessMrIteratorP, c_int]
c_tess_mr_it_next.restype = simple_more_than_zero_result_checker

c_tess_mr_it_get_utf8_text = libctess.tess_mr_it_get_utf8_text
c_tess_mr_it_get_utf8_text.argtypes = [TessMrIteratorP, c_int]
c_tess_mr_it_get_utf8_text.restype = c_void_p

c_tess_mr_it_delete = libctess.tess_mr_it_delete
c_tess_mr_it_delete.argtypes = [TessMrIteratorP]
c_tess_mr_it_delete.restype = simple_nonzero_result_checker

c_tess_mr_it_empty = libctess.tess_mr_it_empty
c_tess_mr_it_empty.argtypes = [TessMrIteratorP, c_int]
c_tess_mr_it_empty.restype = simple_more_than_zero_result_checker

c_tess_set_variable = libctess.tess_set_variable
c_tess_set_variable.argtypes = [TessApiP, c_char_p, c_char_p]
c_tess_set_variable.restype = simple_nonzero_result_checker
