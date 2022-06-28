#!/usr/bin/python3
"""
Module multiplies 2 matrices using numpy module
"""
import numpy


def lazy_matrix_mul(m_a, m_b):
    """
    multiply two giiven matrices
    Args:
        m_a: input first matrix
        m_b: input second matrix
    Returns:
        m_a * m_b
    """
    return numpy.matmul(m_a, m_b)
