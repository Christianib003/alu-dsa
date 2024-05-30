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

    def add(self, other):
        """
        Add two matrices
        """
        # Check if the matrices have the same dimensions
        if self.num_rows != other.num_rows or self.num_cols != other.num_cols:
            raise ValueError("Matrices dimensions do not match for addition")

        # Create a new matrix to store the result
        result = SparseMatrix(num_rows=self.num_rows, num_cols=self.num_cols)

        # Copy the elements of the first matrix to the result
        result.elements = self.elements.copy()

        # Add the elements of the second matrix to the result
        for (row, col), value in other.elements.items():
            # Add values located at the same row and column
            new_value = result.get_element(row, col) + value
            # Set the new value in the result matrix
            result.set_element(row, col, new_value)

        return result

    def subtract(self, other):
        """
        Subtract two matrices
        """
        # Check if the matrices have the same dimensions
        if self.num_rows != other.num_rows or self.num_cols != other.num_cols:
            raise ValueError("Matrices dimensions do not match for subtraction")

        # Create a new matrix to store the result
        result = SparseMatrix(num_rows=self.num_rows, num_cols=self.num_cols)

        # Copy the elements of the first matrix to the result
        result.elements = self.elements.copy()
        for (row, col), value in other.elements.items():
            # Subtract values located at the same row and column
            new_value = result.get_element(row, col) - value
            # Set the new value in the result matrix
            result.set_element(row, col, new_value)
        return result

    def multiply(self, other):
        """
        Multiply two matrices
        """
        # Check if the matrices have the same dimensions
        if self.num_cols != other.num_rows:
            raise ValueError("Matrices dimensions do not match for multiplication")
 
        # Create a new matrix to store the result
        result = SparseMatrix(num_rows=self.num_rows, num_cols=other.num_cols)

        # Multiply the matrices
        for (row1, col1), value1 in self.elements.items():
            for (row2, col2), value2 in other.elements.items():
                if col1 == row2:
                    result.set_element(row1, col2, result.get_element(row1, col2) + value1 * value2)
        return result

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

    def save_result(self, result_file_path):
        """
        Save the result matrix operation to a file
        """
        with open(result_file_path, 'w', encoding='utf-8') as file:
            file.write(f"rows={self.num_rows}\n")
            file.write(f"cols={self.num_cols}\n")
            for (row, col), value in self.elements.items():
                file.write(f"({row}, {col}, {value})\n")

    def get_element(self, curr_row, curr_col):
        """
        Get the element at the given row and column
        """
        return self.elements.get((curr_row, curr_col), 0)

    def set_element(self, curr_row, curr_col, value):
        """
        Set the element at the given row and column
        """
        if value != 0:
            self.elements[(curr_row, curr_col)] = value
        elif (curr_row, curr_col) in self.elements:
            del self.elements[(curr_row, curr_col)]

    def __str__(self):
        return f"rows={self.num_rows}\ncols={self.num_cols}\n(elements={self.elements})"
