"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

def palindrome(num):
    n = num
    r = 0
    while n > 0:
        t = n % 10 # get last digit
        r = 10 * r + t # push it onto reversed number
        n /= 10 # trim off last digit
    return num == r

print max([x*y for x in range(100,1000) for y in range(x,1000) if palindrome(x*y)])
