import pytest
from src.color_stack_sorter import ColorStackSorter

def test_initial_invalid_stack_lengths():
    """Test that an error is raised when stack lengths are unequal"""
    with pytest.raises(ValueError, match="All stacks must have equal number of balls"):
        ColorStackSorter(
            red_stack=['red', 'red'],
            blue_stack=['blue'],
            green_stack=['green', 'green', 'green']
        )

def test_invalid_ball_colors():
    """Test that an error is raised when invalid ball colors are used"""
    with pytest.raises(ValueError, match="Invalid ball colors"):
        ColorStackSorter(
            red_stack=['red', 'yellow'],
            blue_stack=['blue', 'blue'],
            green_stack=['green', 'green']
        )

def test_already_sorted_stacks():
    """Test sorting of stacks that are already sorted"""
    sorter = ColorStackSorter(
        red_stack=['red', 'red'],
        blue_stack=['blue', 'blue'],
        green_stack=['green', 'green']
    )
    moves = sorter.sort()
    assert len(moves) == 0
    
    # Verify stacks remain the same
    assert sorter.stacks['red'] == ['red', 'red']
    assert sorter.stacks['blue'] == ['blue', 'blue']
    assert sorter.stacks['green'] == ['green', 'green']

def test_mixed_stacks_sorting():
    """Test sorting of mixed color stacks"""
    sorter = ColorStackSorter(
        red_stack=['red', 'blue'],
        blue_stack=['green', 'red'],
        green_stack=['blue', 'green']
    )
    moves = sorter.sort()
    
    # Verify moves were made
    assert len(moves) > 0
    
    # Verify final state is sorted
    def is_single_color(stack):
        return len(set(stack)) == 1
    
    assert is_single_color(sorter.stacks['red'])
    assert is_single_color(sorter.stacks['blue'])
    assert is_single_color(sorter.stacks['green'])

def test_case_insensitivity():
    """Test that ball colors are case-insensitive"""
    sorter = ColorStackSorter(
        red_stack=['RED', 'blue'],
        blue_stack=['Green', 'red'],
        green_stack=['blue', 'GREEN']
    )
    moves = sorter.sort()
    
    # Verify moves were made
    assert len(moves) > 0
    
    # Verify final state is sorted
    def is_single_color(stack):
        return len(set(ball.lower() for ball in stack)) == 1
    
    assert is_single_color(sorter.stacks['red'])
    assert is_single_color(sorter.stacks['blue'])
    assert is_single_color(sorter.stacks['green'])

def test_edge_case_minimal_stacks():
    """Test sorting with minimal stack size"""
    sorter = ColorStackSorter(
        red_stack=['red'],
        blue_stack=['blue'],
        green_stack=['green']
    )
    moves = sorter.sort()
    
    # Verify final state is sorted
    def is_single_color(stack):
        return len(set(stack)) == 1
    
    assert is_single_color(sorter.stacks['red'])
    assert is_single_color(sorter.stacks['blue'])
    assert is_single_color(sorter.stacks['green'])