#11651
import sys

n = int(sys.stdin.readline())
arr = []
for _ in range(n):
	x,y = map(int,sys.stdin.readline().split())
	arr.append((y,x))

arr.sort()

for i in arr:
	print(i[1],i[0])
