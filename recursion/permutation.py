# result = []

# def permutation(data,i,n):
#     if i == n:
#         result.append("".join(data)) #['A','B','C']
#     for j in range(i,n+1):
#         data[i],data[j] = data[j],data[i]
#         permutation(data,i+1,n)
#         data[i],data[j] = data[j],data[i] #backtraking


# data = "ABC" #['A','B','C']
# i = 0
# n = len(data)-1

# permutation(list(data),i,n)

# print(result)

from itertools import permutations

result =["".join(x) for x in list(permutations("ABC")) ]
print(result)
