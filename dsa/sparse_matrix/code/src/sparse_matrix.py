#! /usr/bin/python3
"""
A module holding a class representing a Sparse Matrix
operations
"""


class SparseMatrix:
    """
    A class used to represent a Sparse Matrix
    """
    def __init__(self, matrix_file_path=None, num_rows=None, num_cols=None):
        """
        Initialize the SparseMatrix object
        """
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.elements = {}
        if matrix_file_path:
            self.load_matrix(matrix_file_path)

    def load_matrix(self, matrix_file_path):
        """
        Load the matrix from a file

        Args:
            matrix_file_path: (_type_): _description_

        Raises:
            ValueError: Raise an error if the input file has wrong format
        """
        try:
            with open(matrix_file_path, 'r', encoding='utf-8') as file:
                lines = file.readlines()
                self.num_rows = int(lines[0].split('=')[1].strip())
                self.num_cols = int(lines[1].split('=')[1].strip())
                for line in lines[2:]:
                    line = line.strip()
                    if line:
                        row, col, value = map(int, line.strip('()').split(','))
                        self.elements[(row, col)] = value
        except ValueError as e:
            raise ValueError("Input file has wrong format") from e
