
def lcs(A,B):
    la = len(A)
    lb = len(B)
    table = [[-1 for x in range(lb+1)] for x in range(la+1) ]
            #[
            # [-1,-1,-1,-1,-1],
            # [-1,-1,-1,-1,-1],
            # [-1,-1,-1,-1,-1],
            #]
    for i in range(la+1):
        for j in range(lb+1):
            if i==0 or j==0:
                table[i][j] = 0    
            elif A[i-1] == B[j-1]:
                table[i][j]  = 1 + table[i-1][j-1]
            else:
                table[i][j] = max(table[i][j-1],table[i-1][j])    
    return table[la][lb]

                
print(lcs("abcdef","cef")) 
