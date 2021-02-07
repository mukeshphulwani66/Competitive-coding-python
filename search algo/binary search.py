def binarySearch(mylist,target):
    left = 0
    right = len(mylist)-1
    while left <= right:
        middle = (left + right)//2
        if target == mylist[middle]:
           return middle
        elif  target >  mylist[middle]:
            left = middle +1
        else:
            right  = middle-1

    return -1


print(binarySearch([2,3,4,5],10))                

