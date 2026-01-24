def lis(A, dp):
    for i in range(len(A)):
        j = i-1
        while j >= 0:
            if A[i] > A[j]:
                dp[i] = max(dp[i], dp[j]+1)
            j -= 1
    return dp
            
            
N = int(input())
A = list(map(int, input().split()))
dp = [1]*N

res = lis(A, dp)
print(max(res))