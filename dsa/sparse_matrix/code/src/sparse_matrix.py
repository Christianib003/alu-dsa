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
