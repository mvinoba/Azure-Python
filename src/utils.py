def is_prime(x):
    """Checks if x is prime in a not optimized way"""
    if x > 1:
        for i in range(2, x // 2):
            if (x % i) == 0:
                return False
        else:
            return True
    else:
        return False
