from collections import deque
import sys 

# 입력
n = int(input())
# 상하좌우
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
	sheep = 0
	queue = deque()
	queue.append((x,y))
	sheep += 1
	while queue:
		x,y = queue.popleft()
		visited[x][y] = True
		for i in range(4):
			nx = x+dx[i]
			ny = y+dy[i]

			# 범위 벗어날 경우 무시
			if nx<0 or ny<0 or nx>=r or ny>=c:
				continue
			if not visited[nx][ny]:
				if graph[nx][ny] == '#':
					visited[nx][ny] = True
					queue.append((nx,ny))
					continue
	return sheep


for i in range(n):
	result = 0
	r,c = map(int,sys.stdin.readline().split())
	visited = [[False]*c for _ in range(r)]
	graph = []
	for _ in range(r):
		graph.append(list(sys.stdin.readline().strip()))

	for j in range(r):
		for k in range(c):
			if graph[j][k] == '#' and not visited[j][k]:
				result += bfs(j,k)
	
	print(result)

	











				