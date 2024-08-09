#!/usr/bin/python3
def is_prime(n):
    """Check if a number is prime"""
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    max_divisor = int(n**0.5) + 1
    for d in range(3, max_divisor, 2):
        if n % d == 0:
            return False
    return True

def isWinner(x, nums):
    """Determine the winner of each game"""
    maria_wins = 0
    for n in nums:
        # Initialize the set of consecutive integers
        num_set = set(range(1, n + 1))
        
        # Initialize the current player
        player = "Maria"
        
        while True:
            # Find the smallest prime number in the set
            prime_num = next((num for num in sorted(num_set) if is_prime(num)), None)
            
            # If no prime number is found, the current player loses
            if prime_num is None:
                if player == "Maria":
                    maria_wins -= 1
                break
            
            # Remove the prime number and its multiples from the set
            num_set -= set(range(prime_num, n + 1, prime_num))
            
            # Switch the current player
            player = "Ben" if player == "Maria" else "Maria"
    
    # Determine the overall winner
    if maria_wins > x / 2:
        return "Maria"
    elif maria_wins < x / 2:
        return "Ben"
    else:
        return None
