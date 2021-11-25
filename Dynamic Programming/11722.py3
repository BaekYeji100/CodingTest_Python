# 11722

n = int(input())
arr = list(map(int, input().split()))

dp = [1] * n

for i in range(n):
    for j in range(i):
        if arr[j] > arr[i]:
            dp[i] = max(dp[i], dp[j] + 1)
print(max(dp))


# 10 X
# 30 X
# 10 O -> 30 & 10 -> 1+1
# 20 O -> 30 & 20 -> 1+1
# 20 O -> 30 & 20 -> 1+1
# 10 O -> 30 & 10 -> 1+1
#         20 & 10 -> 2+1!!
