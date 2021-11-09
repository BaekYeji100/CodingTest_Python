n, k = map(int,input().split())
arr = list(map(int,input().split()))
height_difference = []
for i in range(n-1):
	height_difference.append(arr[i+1]-arr[i])

height_difference.sort()
print(sum(height_difference[:n-k]))
	