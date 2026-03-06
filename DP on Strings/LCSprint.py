s1 = "aggtab"
s2 = "gxtxayb"

n1 =len(s1)
n2 = len(s2)

# def f(i, j):
#     if i < 0 or j < 0:
#         return 0
#     if s1[i] == s2[j]:
#         return 1+f(i-1, j-1)
#     return max(f(i-1,j), f(i, j-1))
# print(f(n1-1, n2-1))

dp = [[-1]*(n2+1) for _ in range(n1+1)]
for i in range(n1+1):
    dp[i][0] = 0
for j in range(n2+1):
    dp[0][j] = 0

for i in range(1,n1+1):
    for j in range(1,n2+1):
        if s1[i-1] == s2[j-1]:
            dp[i][j] = 1 + dp[i-1][j-1]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[n1][n2])
i = n1
j = n2
res = ""
while i > 0 and j > 0:
    if s1[i-1] == s2[j-1]:
        res += s1[i-1]
        i-=1
        j-=1
    elif dp[i-1][j] > dp[i][j-1]:
        i = i-1
    else:
        j = j-1
print(res[::-1])

1