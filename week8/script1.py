def fibonacci(n):
    """
    Calculates the next number of the Fibonacci sequence.
    """
    if n == 0 or n == 1:
        return n
    
    return fibonacci(n - 1) + fibonacci(n - 2)

limit = 30
seq = [fibonacci(n) for n in range(limit)]
print(f'\tCalculating the first {limit} terms of the Fibonacci sequence:')
print(f'\t{seq}')
print()