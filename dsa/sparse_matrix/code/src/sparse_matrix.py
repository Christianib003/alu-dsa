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
        """
        try:
            with open(matrix_file_path, 'r', encoding='utf-8') as file:
                lines = file.readlines()

                # Read the first 2 lines to get the number of rows and columns
                self.num_rows = int(lines[0].split('=')[1].strip())
                self.num_cols = int(lines[1].split('=')[1].strip())

                # Read the rest of the lines to get the elements
                for line in lines[2:]:
                    line = line.strip()
                    if line:
                        # Parse the line to get the row, column and value
                        row, col, value = map(int, line.strip('()').split(','))
                        # Store the value in the elements dictionary
                        # format: {(row, col): value}
                        self.elements[(row, col)] = value
                return self.elements
        except ValueError as e:
            raise ValueError("Input file has wrong format") from e

    def get_element(self, curr_row, curr_col):
        """
        Get the element at the given row and column
        """
        return self.elements.get((curr_row, curr_col), 0)
