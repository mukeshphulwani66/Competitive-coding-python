
N = 50

n1 = (N-1) // 3
n2 = (N-1) // 5
n3 = (N-1) // 15

s1 = n1 * (2*3+(n1-1)*3)//2
s2 = n2 * (2*5+(n2-1)*5)//2
s3 = n3 * (2*15+(n3-1)*15)//2

print(s1+s2-s3)