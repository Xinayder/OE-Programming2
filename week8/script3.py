import math

def catalan(n):
    """
    Calculates the nth Catalan number. 
    See https://en.wikipedia.org/wiki/Catalan_number and https://oeis.org/A000108
    """
    return (math.factorial(2*n)) // (math.factorial(n+1) * math.factorial(n))

limit = 30
seq = [catalan(n) for n in range(limit)]
print(f'\tCalculating the first {limit} terms of the Catalan sequence:')
print(f'\t{seq}')
print()