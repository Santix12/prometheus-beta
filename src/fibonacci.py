from functools import lru_cache
from typing import List, Generator

@lru_cache(maxsize=None)
def fibonacci_sequence(n: int) -> List[int]:
    """
    Generate the first n numbers of the Fibonacci sequence.
    
    Args:
        n (int): Number of Fibonacci sequence elements to generate. 
                 Must be a non-negative integer.
    
    Returns:
        List[int]: A list containing the first n Fibonacci numbers.
    
    Raises:
        ValueError: If n is negative.
    
    Time Complexity: O(n)
    Space Complexity: O(n)
    
    Examples:
        >>> fibonacci_sequence(0)
        []
        >>> fibonacci_sequence(1)
        [0]
        >>> fibonacci_sequence(5)
        [0, 1, 1, 2, 3]
    """
    # Validate input
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    
    # Handle base cases
    if n == 0:
        return []
    if n == 1:
        return [0]
    if n == 2:
        return [0, 1]
    
    # Recursive generation with memoization
    def fib_generator() -> Generator[int, None, None]:
        """Generate Fibonacci numbers using memoized recursive approach."""
        # Use a dictionary to cache computed values
        memo = {0: 0, 1: 1}
        
        def fib(k: int) -> int:
            """Compute Fibonacci number with memoization."""
            if k not in memo:
                memo[k] = fib(k-1) + fib(k-2)
            return memo[k]
        
        # Generate first n Fibonacci numbers
        for i in range(n):
            yield fib(i)
    
    # Convert generator to list
    return list(fib_generator())