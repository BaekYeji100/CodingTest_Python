import sys

result = []
n = int(input())
for i in range(n):
	arr = list(map(int,sys.stdin.readline().split()))
	arr.sort(reverse=True)
	result.append(arr[2])

for i in result:
	print(i)