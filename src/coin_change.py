def min_coins(coins, amount):
    """
    Compute the minimum number of coins needed to make up a given amount.
    
    Args:
        coins (list): A list of coin denominations available
        amount (int): The target amount to make change for
    
    Returns:
        int: Minimum number of coins needed to make up the amount
             Returns -1 if the amount cannot be made up exactly
    
    Raises:
        ValueError: If coins list is empty or contains non-positive values
    """
    # Validate input
    if not coins:
        raise ValueError("Coin denominations list cannot be empty")
    
    if any(coin <= 0 for coin in coins):
        raise ValueError("All coin denominations must be positive")
    
    # Special case for 0 amount
    if amount == 0:
        return 0
    
    # Sort coins in descending order for greedy approach first
    coins.sort(reverse=True)
    
    # Initialize dp array with amount + 1 (impossible value)
    # dp[i] represents the minimum coins needed to make amount i
    dp = [amount + 1] * (amount + 1)
    dp[0] = 0
    
    # Build solution bottom-up
    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    
    # Return result or -1 if amount cannot be made
    return dp[amount] if dp[amount] <= amount else -1