# given number n, find no of primes less than n

from math import sqrt
def is_Prime(k):
    if k % 2 == 0:
        return 0
    for i in range(3, int(sqrt(k) + 1), 2):
        if k % i == 0:
            return 0
    return 1

def solve(n):
    if n <= 2:
        return 0
    count = 1
    for i in range(3, n, 2):
        if is_Prime(i):
            count += 1
    return count

print(solve(10))


# Method 2: Sieve of eratosthenes
# Instead of checking all numbers is prime of not, we can store prime numbers in array

def solve(n):
    primes = [1]*(n+1)
    for i in range(2, int(sqrt(n) + 1)):
        if primes[i] == 1:
            # Mark all multiples False
            for j in range(2*i, n+1, i):
                primes[j] = 0
    
    count = 0
    for i in range(2,n):
        if primes[i]:
            count += 1
    return count

print(solve(10))
print()

def solve(n):
    primes = [1]*(n+1)
    for i in range(2, int(sqrt(n) + 1)):
        if primes[i] == 1:
            for j in range(i*i, n+1, i):
                primes[j] = 0
    count = 0
    for i in range(2, n):
        if primes[i]:
            count += 1
    return count

print(solve(10))