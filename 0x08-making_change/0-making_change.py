#!/usr/bin/python3
"""_summary_
"""


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given amount total.

    Args:
        coins (list): A list of coin values.
        total (int): The target amount.

    Returns:
        int: The fewest number of coins needed to meet the total. Returns 0 if total is 0 or less, and -1 if total cannot be met.
    """
    # Create a list to store the minimum number of coins needed for each amount from 0 to total
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Base case: 0 coins needed to make 0 amount

    # Iterate over each coin value
    for coin in coins:
        # Iterate over each amount from the coin value to the total
        for i in range(coin, total + 1):
            # Update the minimum number of coins needed for the current amount
            dp[i] = min(dp[i], dp[i - coin] + 1)

    # Return the minimum number of coins needed to meet the total
    return dp[total] if dp[total] != float('inf') else -1
