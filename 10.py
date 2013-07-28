"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

from helpers import sieve

# this one was a bit too easy after writing the Sieve
print sum(sieve(2000000))
