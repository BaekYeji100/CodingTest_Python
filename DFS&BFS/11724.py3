import sys
sys.setrecursionlimit(10000)

def dfs(node, start, visited):
	for n in node[start]:
		if not visited[n]:
			visited[n] = True
			dfs(node,n,visited)

n,m = map(int,sys.stdin.readline().split())
node = [[]for row in range(n+1)]
visited = [False]*(n+1)
visited[0] = True
result = 0
for i in range(m):
	u,v = map(int,sys.stdin.readline().split())
	node[u].append(v)
	node[v].append(u)

# 끊겼는지 확인 후 다시 dfs로 보내주기
for i in range(1,len(visited)):
	if not visited[i]:
		result += 1
		dfs(node,i,visited)
dfs(node,1,visited)

print(result)