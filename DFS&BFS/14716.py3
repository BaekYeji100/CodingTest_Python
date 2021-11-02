from collections import deque
import sys 

# 입력
r,c = map(int,sys.stdin.readline().split())
graph = []
for _ in range(r):
	graph.append(list(sys.stdin.readline().split()))
# 방문확인용
visited = [[False]*c for _ in range(r)]
# 상하좌우,대각선 포함
dx = [-1,1,0,0,-1,-1,1,1]
dy = [0,0,-1,1,-1,1,-1,1]

def bfs(x,y):
	queue = deque()
	queue.append((x,y))

	while queue:

		x,y = queue.popleft()
		#print(x,y)
		visited[x][y] = True
		for i in range(8):
			nx = x+dx[i]
			ny = y+dy[i]
			# 캠퍼스 크기 벗어날 경우 무시
			if nx<0 or ny<0 or nx>=r or ny>=c:
				continue
			if not visited[nx][ny]:
				visited[nx][ny] = True
				if graph[nx][ny] == '0':
					continue
				if graph[nx][ny] == '1':
					queue.append((nx,ny))


result = 0
for i in range(r):
	for j in range(c):
		if graph[i][j] == '1' and not visited[i][j] :
			bfs(i,j)
			result += 1


print(result)