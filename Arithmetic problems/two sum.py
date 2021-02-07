
nums = [2,7,11,15]
target = 9

for b in range(0,len(nums)):
    a = target - nums[b]
    if a in nums and b != nums.index(a):
        print([b,nums.index(a)])
        break


