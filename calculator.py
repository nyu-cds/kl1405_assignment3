# -----------------------------------------------------------------------------
# calculator.py
# HW6
# Kaiwen liu
#
# cPython: original total time: 2.434s
#        multiply(),add(),sqrt() take majority of the time
#
# line_profiler: original total time: 2.991s
#                line 49: 26.2% time, xx=multiply(x,x)
#                line 50: 24.9% time, yy=multiply(y,y)
#                line 51: 26.5% time, zz=add(xx,yy)
#                line 52: 22.4% time, return sqrt(zz)
#
# Speedup (with %timeit hypotenuse(A,B)): 
#               2.25s /0.00859s = 261.932479627
# ----------------------------------------------------------------------------- 
import numpy as np
from math import sqrt

def add(x,y):
    """
    Add two arrays using a Python loop.
    x and y must be two-dimensional arrays of the same shape.
    """
    
    return np.add(x,y)


def multiply(x,y):
    """
    Multiply two arrays using a Python loop.
    x and y must be two-dimensional arrays of the same shape.
    """

    return np.multiply(x,y)


def sqrt(x):
    """
    Take the square root of the elements of an arrays using a Python loop.
    """

    return np.sqrt(x)


def hypotenuse(x,y):
    """
    Return sqrt(x**2 + y**2) for two arrays, a and b.
    x and y must be two-dimensional arrays of the same shape.
    """
    xx = multiply(x,x)
    yy = multiply(y,y)
    zz = add(xx, yy)
    return sqrt(zz)