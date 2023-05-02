def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix.
    """
    # Check that matrix is a list of lists of integers or floats
    if not all(isinstance(row, list) for row in matrix) or not all(
            isinstance(num, (int, float)) for row in matrix for num in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Check that each row of the matrix has the same size
    if len(set(len(row) for row in matrix)) > 1:
        raise TypeError("Each row of the matrix must have the same size")

    # Check that div is a number
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Check that div is not zero
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Divide all elements of the matrix by div, rounded to 2 decimal places
    return [[round(num / div, 2) for num in row] for row in matrix]
