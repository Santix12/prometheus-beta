import pytest
from src.add_without_plus import add_without_plus

def test_add_positive_numbers():
    """Test addition of positive numbers."""
    assert add_without_plus(3, 4) == 7
    assert add_without_plus(10, 20) == 30
    assert add_without_plus(0, 5) == 5
    assert add_without_plus(5, 0) == 5

def test_add_negative_numbers():
    """Test addition involving negative numbers."""
    assert add_without_plus(-3, 4) == 1
    assert add_without_plus(3, -4) == -1
    assert add_without_plus(-10, -20) == -30

def test_add_zero():
    """Test addition with zero."""
    assert add_without_plus(0, 0) == 0

def test_large_numbers():
    """Test addition of large numbers."""
    assert add_without_plus(1000, 2000) == 3000
    assert add_without_plus(-1000, 2000) == 1000

def test_invalid_input_types():
    """Test handling of invalid input types."""
    with pytest.raises(TypeError):
        add_without_plus('5', 3)
    with pytest.raises(TypeError):
        add_without_plus(5, '3')
    with pytest.raises(TypeError):
        add_without_plus(5.5, 3)
    with pytest.raises(TypeError):
        add_without_plus(5, [3])