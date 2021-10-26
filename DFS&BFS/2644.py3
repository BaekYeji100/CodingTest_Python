def dfs(node,start,visited):
	for n in node[start]:
		if visited[n] == 0:
			visited[n] = visited[start]+1
			dfs(node,n,visited)

n = int(input())
a, b = map(int,input().split())
m = int(input())
node = [[]for row in range(n+1)]
visited = [0]*(n+1)

for i in range(m):
	x, y = map(int,input().split())
	node[x].append(y)
	node[y].append(x)

dfs(node,a,visited)

if visited[b] > 0:
	print(visited[b])
else:
	print("-1")