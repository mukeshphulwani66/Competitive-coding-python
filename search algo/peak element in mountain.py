'''
Peak Index in a Mountain Array
Input: arr = [0,2,1,0]
Output: 1
Example 3:

Input: arr = [0,10,5,2]
Output: 1
Example 4:

Input: arr = [3,4,5,1]
Output: 2
Example 5:

Input: arr = [24,69,100,99,79,78,67,36,26,19]
Output: 2

solve it without using max function
'''

arr =  [24,69,100,99,79,78,67,36,26,19]

# for i in range(0,len(arr)):
#     if arr[i+1] < arr[i]:
#         print(i)
#         break 

def peakOfMountain(arr):
    left = 0
    right = len(arr) -1
    while left < right:
        mid = (left+right)//2
        if arr[mid] < arr[mid+1]:
            left = mid+1
        else:    
            right = mid
    return right
    

print(peakOfMountain( [0,10,5,2]))    


