#!/usr/bin/python3
''''This module defines two functions: get_matrix_sizes and 
    matrix_mul, which areused in a TDD project for computing and
    validating matrix sizes and performing matrix multiplication.
'''


def get_matrix_sizes(matrix_1, matrix_2, name_1, name_2):
    '''This function computes the rows and columns of the 
    two given matrices and some validation checks
    Args:
        matrix (list): The matrix.
        name (str): The name of the matrix.
    Returns:
        list: contains the rows and columns of the given matrix.
    '''
    funcs = (
        lambda txt: '{} must be a list'.format(txt),
        lambda txt: '{} can\'t be empty'.format(txt),
        lambda txt: '{} must be a list of lists'.format(txt),
        lambda txt: '{} should contain only integers or floats'.format(txt),
        lambda txt: 'each row of {} must be of the same size'.format(txt),
        lambda l: all(map(lambda n: isinstance(n, (int, float)), l)),
    )
    size0 = [0, 0]
    size1 = [0, 0]
    if not isinstance(matrix_1, list):
        raise TypeError(funcs[0](name_1))
    if not isinstance(matrix_2, list):
        raise TypeError(funcs[0](name_2))
    size0[0] = len(matrix_1)
    size1[0] = len(matrix_2)
    if size0[0] == 0:
        raise ValueError(funcs[1](name_1))
    if size1[0] == 0:
        raise ValueError(funcs[1](name_2))
