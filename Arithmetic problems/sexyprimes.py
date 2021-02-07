'''
Given a range of the form [L, R].The task is to print all the sexy prime pairs in the range.

Examples:

Input : L = 6, R = 59
Output : (7, 13) (11, 17) (13, 19) 
(17, 23) (23, 29) (31, 37) (37, 43) 
(41, 47) (47, 53) (53, 59) 

Input : L = 1, R = 19
Output : (5, 11) (7, 13) (11, 17) (13, 19)

'''
from math import sqrt

def generatePrimes(n):
    primes = [True] * (n+1)
    primes[0] = False
    primes[1] = False

    for i in range(2,int(sqrt(n))+1):
        if primes[i] == True:
            for j in range(i*i,n+1,i):
                primes[j] = False
    return primes


L = int(input())
R = int(input())

myprimesnos = generatePrimes(R)


for i in range(L,len(myprimesnos)-6):
    if myprimesnos[i] == True:
        x = i
        y = x + 6
        if myprimesnos[y] == True:
            print("({0},{1})".format(x,y))

          




