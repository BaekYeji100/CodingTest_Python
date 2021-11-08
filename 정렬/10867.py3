import sys

n = int(sys.stdin.readline())
arr = list(map(int,sys.stdin.readline().split()))
arr = list(set(arr))
arr.sort()

for i in arr:
	print(i,end=" ")