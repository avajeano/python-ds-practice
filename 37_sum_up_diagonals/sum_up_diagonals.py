def sum_up_diagonals(matrix):
    """Given a matrix [square list of lists], return sum of diagonals.

    Sum of TL-to-BR diagonal along with BL-to-TR diagonal:

        >>> m1 = [
        ...     [1,   2],
        ...     [30, 40],
        ... ]
        >>> sum_up_diagonals(m1)
        73

        >>> m2 = [
        ...    [1, 2, 3],
        ...    [4, 5, 6],
        ...    [7, 8, 9],
        ... ]
        >>> sum_up_diagonals(m2)
        30
    """

    sum_tl_to_br = 0
    sum_br_to_tl = 0

    for i in range(len(matrix)):
        sum_tl_to_br += matrix[i][i]
        sum_br_to_tl += matrix[i][len(matrix) -1  -i]
    
    return sum_tl_to_br + sum_br_to_tl