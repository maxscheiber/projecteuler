"""
Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
"""

n0 = 0
n1 = 1
s = 0
while n0 + n1 <= 4000000:
    temp = n0
    n0 = n1
    n1 += temp # n1 is now n0 + n1
    if n1 % 2 == 0:
        s += n1
print s
