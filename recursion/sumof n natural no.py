# s(10) = 10 + s(9)
# s(9) = 9 + s(8)
# s(8) = 8 + s(7)
# ..
# .
# .

# s(2) = 2 + s(1)
# s(1) = 1


def s(n):
    if n==1:
        return 1
    return n + s(n-1)


print(s(10))




