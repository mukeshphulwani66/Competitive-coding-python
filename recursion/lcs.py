A = 'abcdefhbedfwuefiuniwedwoiefhfiurgnwruhwon'
B = 'acfibrfueofn4ufhneufhwerwierf'


memo = {
}
def lcs(i,j):
    k = str(i)+str(j)
    if k in memo:
        return memo[k]
    if i==0 or j==0:
        return 0
    elif A[i-1] == B[j-1]:
        value =  1 + lcs(i-1,j-1)
    else :
        value =  max(lcs(i,j-1),lcs(i-1,j))
    memo[k] = value
    return value


print(lcs(len(A),len(B)))
