'''
----- sum of n natural numbers ----

let N = 10 
Required Sum  = 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10
         Sum = 55

----- Find Sum of Multiples of 3 or 5 below N ------

let N = 50
s1 = 3 + 6 + 9 + 12 + 15 + 18 + 21 + 24 + 27 + 30 + 33 + 36 + 39 + 42 + 45 + 48
s2 = 5 + 10 + 15 + 20 + 25 + 30 + 35 + 40 + 45
s3 = 15 + 30 + 45

sum = ( n x [2a + (n-1) x d] ) / 2

----- Two Sum  ---

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
 
Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]

a  = target - b 

------- Chocolate puzzle ------

A teacher decided to motivate all her students for their grades by giving them chocolates.
On the first day she gave a certain number of chocolates and on the next day she gave twice the no of chocolates she gave on previous day and she doubled the no of chocolates every day.
find how many chcolates she bought ? given last day,say N

sample input (last day)
5  

sample output
62

explanation
on first day = 2
on second day = 2*2 = 4
on third day = 4*2 = 8
on fourth day = 8*2 = 16
on last day = 16*2 = 32

sum = 2 + 4 + 8 + 16 + 32 = 62
 
'''




