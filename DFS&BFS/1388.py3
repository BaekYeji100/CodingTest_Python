n,m = map(int,input().split())
graph = [list(input()) for j in range(n)]
cnt = 0 

# - 개수 세기
for i in range(n):
	for j in range(m):
		if graph[i][j] == '-':
			if j+1 < m:
				if graph[i][j+1] == '|':
					cnt += 1
			else:
				cnt += 1

# | 개수 세기
for j in range(m):
	for i in range(n):
		if graph[i][j] == "|":
			if i+1 < n:
				if graph[i+1][j] == '-':
					cnt += 1
			else:
				cnt += 1

print(cnt)

		