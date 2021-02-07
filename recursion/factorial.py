'''
5! =  5 * 4!
4! = 4 * 3!
3! = 3 * 2!
2! = 2 * 1!
1! = 1 * 0!

'''


def factorial(n):
    if n==0:
       return 1
    return n * factorial(n-1)


print(factorial(5))


