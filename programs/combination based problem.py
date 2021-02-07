'''
Write a program to find lowest number of integers in the array that sums up the given number. The program should ask user to input array of integers (“Input Array”) and the required sum (“Required Sum”). The output (“Output”) should list the lowest number of integers from the input array that sums up the “Required Sum”.  Refer to examples given below.

Input :

Array of integers
Required sum
Output :

Elements from array which makes sum equals to given value
Example:

Input Array : [10, 0, -1, 20, 25, 30]
Required Sum: 45
Output: [20, 25]

Required Sum: 59
Output: [10, -1, 20, 30]

Required Sum: 60
Output: [10, 20, 30]
'''


def combination(mylist,r):
    if r == 0:
        return [[]]
    L = []
    for i in range(0,len(mylist)):    
        first = mylist[i]
        rem = mylist[i+1:]
        combList = combination(rem,r-1)
        for x in combList:
            L.append([first]+x)
    return L        


def calculateResult(arr,target): 
    for r in range(1,len(arr)):
        for i in combination(arr,r):
            if sum(i) == target:
                return i


print(calculateResult([10, 0, -1, 20, 25, 30],60) )              
   




