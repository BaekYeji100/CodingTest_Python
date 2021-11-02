from collections import deque
import sys 

# 입력
r,c = map(int,sys.stdin.readline().split())
graph = []
for _ in range(r):
	graph.append(list(sys.stdin.readline().strip()))
# 방문확인용
visited = [[False]*c for _ in range(r)]
# 상하좌우
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
	v,o = 0,0
	queue = deque()
	queue.append((x,y))

	while queue:
		x, y = queue.popleft()
		if graph[x][y] == 'v':
			v += 1
		if graph[x][y] == 'o':
			o += 1
		graph[x][y] = '#'
		for i in range(4):
			nx = x + dx[i]
			ny = y + dy[i]
			if  0<=nx<r and 0<=ny<c and graph[nx][ny]!='#'and visited[nx][ny]==False:
				visited[nx][ny] = True
				queue.append((nx,ny))
	if o > v:
		v = 0
	else:
		o = 0		
	return v,o

result_V,result_O = 0,0
for i in range(r):
	for j in range(c):
		if graph[i][j] == 'o' or graph[i][j]=='v':
			v,o = bfs(i,j)
			#print(i,j,v,o)
			result_V += v
			result_O += o
			
print(result_O,result_V)

