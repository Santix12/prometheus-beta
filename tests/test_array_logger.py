import pytest
from src.array_logger import log_array_as_table

def test_log_array_of_lists():
    """Test logging a basic list of lists"""
    arr = [[1, 2, 3], [4, 5, 6]]
    result = log_array_as_table(arr)
    assert '1 │ 2 │ 3' in result
    assert '4 │ 5 │ 6' in result

def test_log_array_of_dicts():
    """Test logging an array of dictionaries"""
    arr = [
        {'name': 'Alice', 'age': 30},
        {'name': 'Bob', 'age': 25}
    ]
    result = log_array_as_table(arr)
    assert 'Alice' in result
    assert 'Bob' in result
    assert '30' in result
    assert '25' in result

def test_log_array_of_primitives():
    """Test logging a simple list of primitives"""
    arr = [1, 2, 3, 4, 5]
    result = log_array_as_table(arr)
    assert 'Value' in result
    for item in arr:
        assert str(item) in result

def test_custom_headers():
    """Test using custom headers"""
    arr = [[1, 2, 3], [4, 5, 6]]
    headers = ['X', 'Y', 'Z']
    result = log_array_as_table(arr, headers)
    assert 'X │ Y │ Z' in result

def test_dict_with_custom_headers():
    """Test dict array with custom headers"""
    arr = [
        {'name': 'Alice', 'age': 30},
        {'name': 'Bob', 'age': 25}
    ]
    headers = ['Full Name', 'Years Old']
    result = log_array_as_table(arr, headers=['Full Name', 'Years Old'])
    assert 'Full Name │ Years Old' in result

def test_empty_array_error():
    """Test error handling for empty array"""
    with pytest.raises(ValueError, match="Input array cannot be empty"):
        log_array_as_table([])

def test_invalid_input_type():
    """Test error handling for invalid input type"""
    with pytest.raises(TypeError, match="Input must be a list"):
        log_array_as_table("not a list")

def test_inconsistent_dict_keys():
    """Test handling of dictionaries with inconsistent keys"""
    arr = [
        {'name': 'Alice', 'age': 30},
        {'city': 'New York'}
    ]
    result = log_array_as_table(arr)
    assert 'name' in result
    assert 'age' in result
    assert 'city' in result