'''
Febonacci sequence
index   -> 0,1,2,3,4,5,6, 7, 8
fib seq -> 0,1,1,2,3,5,8,13,21

problem - write function to return nth term of finonacci sequence

feb(5th) = feb(4) + feb(3)
feb(4) = feb(3) + feb(2)
feb(3) = feb(2) + feb(1)
feb(2) = feb(1) + feb(0)
feb(1) = 1
feb(0) = 0
'''

# def feb(n):
#     if n == 1 or n==0:
#         return n
#     return feb(n-1) + feb(n-2)
# O(2^n)
# for i in range(51):
#     print(i,feb(i))

'''
Dynamic programming
we can use if there is overlapping subproblem
-Memoization
-Tabular

'''

# memo = {1:1,0:0}
# def feb(n):
#     if n in memo:
#         return memo[n]
#     value =  feb(n-1) + feb(n-2)
#     memo[n] = value
#     return value

# for i in range(50):
#     print(i,feb(i)) 
# O(n)   


def feb(n):
    table = [0]*(n+1) #[0,1,1,2,3,5]
    table[1] = 1
    for i in range(2,n+1):
        table[i] = table[i-1] + table[i-2]
    return table[n]

#O(n)
print(feb(6))        

'''
[
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,ans],
]
'''












