t = int(input())
result = []
for i in range(t):
	cnt = 0
	n,m = map(int,input().split())
	for j in range(n,m+1):
		cnt += str(j).count('0')
	result.append(cnt)

for i in result:
	print(i)
