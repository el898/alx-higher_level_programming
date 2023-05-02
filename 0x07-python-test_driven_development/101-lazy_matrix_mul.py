#!/usr/bin/python3
"""this functuon multiplies a matrix  using NumPy."""
import numpy as nm


def lazy_matrix_mul(m_a, m_b):
    """Return:
        the multiplication of two matrices.
    Args:
        m_a (list of lists of ints/floats): The first matrix.
        m_b (list of lists of ints/floats): The second matrix.
    """

    return (nm.matmul(m_a, m_b))
