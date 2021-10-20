com = int(input())
edge = int(input())
node = [[]for row in range(com+1)]
for i in range(edge):
	a ,b = map(int,input().split())
	node[a].append(b)
	node[b].append(a)

cnt = 0
visited = [False]*(com+1)
def dfs(start):
	global cnt
	visited[start] = True
	for i in node[start]:
		if visited[i] == False:
			dfs(i)
			cnt += 1


dfs(1)
print(cnt)