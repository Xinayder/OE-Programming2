def triangular(n):
    """
    Calculates the nth triangular number. See https://oeis.org/A000217
    """
    return (n*(n+1)) // 2

limit = 30
seq = [triangular(n) for n in range(0, limit)]
print(f'\tCalculating the first {limit} triangular numbers:')
print(f'\t{seq}')
print()