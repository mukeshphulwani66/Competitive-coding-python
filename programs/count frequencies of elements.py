''''
Input :  arr= [10, 20, 20, 10, 10, 20, 5, 20]
Output : 10 3
         20 4
         5  1

Input : arr = [10, 20, 20]
Output : 10 1
         20 2
'''         
arr= [10, 20, 20, 10, 10, 20, 5, 20]

mydict = {
}

for elem in arr:
   if elem not in mydict: 
      mydict[elem] = 1
   else:
     mydict[elem] = mydict[elem] + 1

for i in mydict:
    print(i,"  ",mydict[i])













