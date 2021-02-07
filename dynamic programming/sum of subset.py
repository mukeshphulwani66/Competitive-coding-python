'''
sum of subset
A={3, 4, 5, 2},target=6
{},
{3,4},
{3,4,5}
{4,2} -> True
...
..
.
'''

def sumofSubset(A,target):
   n = len(A)
   dp = [[False for j in range(target+1)] for i in range(n+1)]
         #[[False,False,False,False,False,False,False],
         # [False,False,False,False,False,False,False],
         # [False,False,False,False,False,False,False],
         # [False,False,False,False,False,False,False],
         # [False,False,False,False,False,False,False],
         #]

   for i in range(n+1):
       dp[i][0] = True

   for j in range(1,target+1):
       dp[0][j] = False   

   for i in range(1,n+1):
       for j in range(1,target+1):
           if j < A[i-1]:
               dp[i][j] = dp[i-1][j]
           if j >= A[i-1]:
               dp[i][j] = dp[i-1][j] or dp[i-1][j-A[i-1]]

   print(dp)
   '''
   [[True, False, False, False, False, False, False],
    [True, False, False, True, False, False, False],
     [True, False, False, True, True, False, False], 
     [True, False, False, True, True, True, False],
     [True, False, True, True, True, True, True]]
   '''
   return dp[n][target]            

print(sumofSubset([3, 4, 5, 2],6))