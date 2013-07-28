from math import log

def sieve(n):
    primeBools = [True for i in range(n+2)] # primes[i] represents the number i
    for i in range(2, n):
        for j in range(2*i, n, i):
            primeBools[j] = False
    primes = []
    for i in range(2, n):
        if primeBools[i]:
            primes.append(i)
    return primes

def primeUpperBound(n):
    return int(round(n * log(n) + n * log(log(n))))
