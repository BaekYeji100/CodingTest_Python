import sys

n = int(input())
arr = [int(sys.stdin.readline().strip()) for _ in range(n)]
arr.sort()

cnt_num = []

for i in arr:
	cnt = 0
	for j in range(i,i+5):
		if j not in arr:
			cnt += 1
	cnt_num.append(cnt)


print(min(cnt_num))
