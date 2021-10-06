import sys

k = int(input())
result = []
for i in range(k):
	num = int(sys.stdin.readline())
	if num!=0:
		result.append(num)
	else:
		result.pop()


print(sum(result))