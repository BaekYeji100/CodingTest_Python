import sys

n = int(input())
num = [int(sys.stdin.readline().strip()) for _ in range(n)]
num.sort()

result = []
for i in range(n):
	num_com = set(range(num[i],num[i]+5))
	result.append(len(num_com.difference(set(num[i:i+5]))))

print(min(result))