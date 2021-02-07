

def callme(n):
    if n==5:
        return
    callme(n+1)
    print(n)

'''
1 - no output
2 - 1-4
3 - 4 3 2 1

'''
callme(1)    
