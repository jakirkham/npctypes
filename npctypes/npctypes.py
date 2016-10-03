__author__ = "John Kirkham <kirkhamj@janelia.hhmi.org>"
__date__ = "$Oct 03, 2016 14:19$"


import collections

import numpy


CTypesArray = collections.namedtuple(
    "CTypeArray",
    [
        "type",
        "data",
    ]
)

def tinfo(a_type):
    """
        Takes a ``numpy.dtype`` or any type that can be converted to a
        ``numpy.dtype`` and returns its info.

        Args:
            a_type(type):                  the type to find info for.

        Returns:
            (np.core.getlimits.info):      info about the type.

        Examples:
            >>> tinfo(float)
            finfo(resolution=1e-15, min=-1.7976931348623157e+308, max=1.7976931348623157e+308, dtype=float64)

            >>> tinfo(numpy.float64)
            finfo(resolution=1e-15, min=-1.7976931348623157e+308, max=1.7976931348623157e+308, dtype=float64)

            >>> tinfo(numpy.float32)
            finfo(resolution=1e-06, min=-3.4028235e+38, max=3.4028235e+38, dtype=float32)

            >>> tinfo(complex)
            finfo(resolution=1e-15, min=-1.7976931348623157e+308, max=1.7976931348623157e+308, dtype=float64)

            >>> tinfo(int)
            iinfo(min=-9223372036854775808, max=9223372036854775807, dtype=int64)
    """

    a_type = numpy.dtype(a_type).type

    if issubclass(a_type, numpy.integer):
        return(numpy.iinfo(a_type))
    else:
        return(numpy.finfo(a_type))


def ctype(a_type):
    """
        Takes a numpy.dtype or any type that can be converted to a numpy.dtype
        and returns its equivalent ctype.

        Args:
            a_type(type):      the type to find an equivalent ctype to.

        Returns:
            (ctype):           the ctype equivalent to the dtype provided.

        Examples:
            >>> ctype(float)
            <class 'ctypes.c_double'>

            >>> ctype(numpy.float64)
            <class 'ctypes.c_double'>

            >>> ctype(numpy.float32)
            <class 'ctypes.c_float'>

            >>> ctype(numpy.dtype(numpy.float32))
            <class 'ctypes.c_float'>

            >>> ctype(int)
            <class 'ctypes.c_long'>
    """

    return(type(numpy.ctypeslib.as_ctypes(numpy.array(0, dtype=a_type))))
