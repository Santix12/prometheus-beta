import pytest
from src.coin_change import min_coins

def test_basic_coin_change():
    """Test basic coin change scenarios"""
    assert min_coins([1, 2, 5], 11) == 3  # 5 + 5 + 1
    assert min_coins([2], 3) == -1  # Cannot make 3 with only 2-cent coins
    assert min_coins([1], 0) == 0  # Zero amount

def test_edge_cases():
    """Test edge cases and error conditions"""
    # Empty coins list
    with pytest.raises(ValueError, match="Coin denominations list cannot be empty"):
        min_coins([], 10)
    
    # Non-positive coin values
    with pytest.raises(ValueError, match="All coin denominations must be positive"):
        min_coins([0, 1, 2], 5)
    with pytest.raises(ValueError, match="All coin denominations must be positive"):
        min_coins([-1, 2, 3], 5)

def test_complex_scenarios():
    """Test more complex coin change scenarios"""
    assert min_coins([1, 5, 10, 25], 67) == 6  # Correct minimum number of coins
    assert min_coins([186, 419, 83, 408], 6249) == 20
    
    # Large amount with limited coin denominations
    assert min_coins([1, 5, 10], 100) == 10  # 10x10-cent coins

def test_single_coin_type():
    """Test scenarios with a single coin type"""
    assert min_coins([1], 5) == 5  # 5x1-cent coins
    assert min_coins([2], 6) == 3  # 3x2-cent coins
    assert min_coins([5], 7) == -1  # Cannot make 7 with 5-cent coins