from math import sqrt

n = 50

primes = [True] * (n+1)
primes[0] = False
primes[1] = False

for i in range(2,int(sqrt(n))+1):
    if primes[i] == True:
        for j in range(i*i,n+1,i):
            primes[j] = False


for i in range(len(primes)):
    if primes[i] == True:
        print(i)

