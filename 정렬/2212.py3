n = int(input())
k = int(input())
arr = list(map(int,input().split()))

arr.sort()
result = []

for i in range(n-1):
	result.append(arr[i+1]-arr[i])
result.sort()
# print(result)

print(sum(result[:n-k]))