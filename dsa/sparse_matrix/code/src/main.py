#! /usr/bin/python3
"""
A module to call the SparseMatrix class
"""

import os

from sparse_matrix import SparseMatrix


def main():
    """
    Main function
    """
    base_path = 'dsa/sparse_matrix/sample_inputs/'
    matrix1_file_path = os.path.join(base_path, 'matrix1.txt')
    matrix2_file_path = os.path.join(base_path, 'matrix2.txt')

    matrix1 = SparseMatrix(matrix1_file_path)
    matrix2 = SparseMatrix(matrix2_file_path)

    result_add = matrix1.add(matrix2)

    print(result_add)

main()