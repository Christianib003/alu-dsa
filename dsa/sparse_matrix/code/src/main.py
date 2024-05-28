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
    input_base_path = 'dsa/sparse_matrix/sample_inputs/'
    matrix1_file_path = os.path.join(input_base_path, 'matrix1.txt')
    matrix2_file_path = os.path.join(input_base_path, 'matrix2.txt')

    matrix1 = SparseMatrix(matrix1_file_path)
    matrix2 = SparseMatrix(matrix2_file_path)
    result_add = matrix1.add(matrix2)

    output_path = 'dsa/sparse_matrix/sample_outputs/result_matrix.txt'
    result_add.save_result(output_path)

    print(result_add)

main()
