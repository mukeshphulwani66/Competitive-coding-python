'''
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.
Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
Output: 7
Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.
Example 2:
Input: grid = [[1,2,3],[4,5,6]]
Output: 12   

'''

grid = [[1,2,3],
        [4,5,6]]

m = len(grid) #row length 3
n = len(grid[0]) #column length 3

result = [[0 for x in range(n) ] for x in range(m) ]
         #[
         # [0,0,0]
         # [0,0,0]
         # [0,0,0]
         # ]

result[0][0]   = grid[0][0]

for j in range(1,n):#1,2
      result[0][j] = grid[0][j] + result[0][j-1]

for i in range(1,m):#1,2
      result[i][0]  = grid[i][0] + result[i-1][0]

for i in range(1,m):
    for j in range(1,n):
        result[i][j] = grid[i][j] + min(result[i-1][j],result[i][j-1])
        
print(result)
print(result[m-1][n-1])


  



