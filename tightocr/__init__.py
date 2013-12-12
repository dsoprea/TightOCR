class LibraryReturnError(ValueError):
    pass

def simple_nonzero_result_checker(value):
    if value != 0:
        raise LibraryReturnError("Library function returned failure (%d)." % 
                                 (value))

    return value

def simple_more_than_zero_result_checker(value):
    if value < 0:
        raise LibraryReturnError("Library function returned failure (%d)." % 
                                 (value))

    return value

def simple_ptr_result_checker(value):
    if value is None:
        raise LibraryReturnError("Library function returned failure (NULL).")

    return value

def simple_boolean_error_checker(value):
    if value == 0:
        raise LibraryReturnError("Library function returned failure (0).")

    return value

