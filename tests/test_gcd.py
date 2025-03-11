import pytest
from src.gcd import gcd

def test_gcd_basic_numbers():
    """Test GCD of basic positive integers"""
    assert gcd(48, 18) == 6
    assert gcd(54, 24) == 6
    assert gcd(17, 23) == 1

def test_gcd_zero():
    """Test GCD when one or both inputs are zero"""
    assert gcd(0, 5) == 5
    assert gcd(5, 0) == 5
    assert gcd(0, 0) == 0

def test_gcd_one():
    """Test GCD with one as an input"""
    assert gcd(1, 5) == 1
    assert gcd(5, 1) == 1

def test_gcd_same_number():
    """Test GCD when both inputs are the same"""
    assert gcd(7, 7) == 7
    assert gcd(13, 13) == 13

def test_gcd_large_numbers():
    """Test GCD with larger numbers"""
    assert gcd(1071, 462) == 21
    assert gcd(3279, 2016) == 3

def test_invalid_input_type():
    """Test that TypeError is raised for non-integer inputs"""
    with pytest.raises(TypeError):
        gcd(4.5, 3)
    with pytest.raises(TypeError):
        gcd("10", 5)
    with pytest.raises(TypeError):
        gcd([10], 5)

def test_negative_input():
    """Test that ValueError is raised for negative inputs"""
    with pytest.raises(ValueError):
        gcd(-5, 10)
    with pytest.raises(ValueError):
        gcd(5, -10)
    with pytest.raises(ValueError):
        gcd(-5, -10)