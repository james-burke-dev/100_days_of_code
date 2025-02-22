def is_prime(num):
    if num < 4 or (num % 2 > 0 and num % 3 > 0):
        return True
    else:
        return False