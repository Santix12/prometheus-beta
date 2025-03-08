"""
Sparse Matrix Multiplication using Dictionary Representation

This module provides functionality for sparse matrix multiplication 
where matrices are represented as dictionaries with row indices as keys 
and row vectors as values.
"""

def sparse_matrix_multiply(matrix_a, matrix_b):
    """
    Perform sparse matrix multiplication using dictionary representation.
    
    Args:
        matrix_a (dict): First sparse matrix represented as {row_index: row_vector}
        matrix_b (dict): Second sparse matrix represented as {row_index: row_vector}
    
    Returns:
        dict: Resulting sparse matrix after multiplication
    
    Raises:
        ValueError: If matrix dimensions are incompatible for multiplication
    """
    # Validate input matrices
    if not isinstance(matrix_a, dict) or not isinstance(matrix_b, dict):
        raise ValueError("Inputs must be dictionaries")
    
    # Check matrix compatibility
    if not matrix_a or not matrix_b:
        return {}
    
    # Precompute B columns and rows for efficiency
    b_cols = set()
    b_rows = {}
    for row_idx, row_vec in matrix_b.items():
        b_rows[row_idx] = row_vec
        b_cols.update(row_vec.keys())
    
    # Initialize result matrix
    result = {}
    
    # Perform multiplication
    for a_row, a_row_vec in matrix_a.items():
        # Only compute rows with non-zero entries in A
        result_row = {}
        
        for b_col in b_cols:
            # Compute dot product for this cell
            cell_value = 0
            for a_col, a_val in a_row_vec.items():
                # If this column index exists in B's rows
                if a_col in b_rows:
                    b_row_vec = b_rows[a_col]
                    if b_col in b_row_vec:
                        cell_value += a_val * b_row_vec[b_col]
            
            # Only store non-zero values
            if cell_value != 0:
                result_row[b_col] = cell_value
        
        # Only add non-empty rows to result
        if result_row:
            result[a_row] = result_row
    
    return result