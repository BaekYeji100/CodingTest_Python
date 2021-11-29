#4963
from collections import deque
import sys 

def bfs(x,y):
	queue = deque()
	queue.append((x,y))

	while queue:
		x,y = queue.popleft()
		#print(x,y)
		visited[x][y] = True
		for i in range(8): # 대각선
			nx = x+dx[i]
			ny = y+dy[i]
			# 캠퍼스 크기 벗어날 경우 무시
			if nx<0 or ny<0 or nx>=h or ny>=w:
				continue
			if not visited[nx][ny]:
				visited[nx][ny] = True
				if graph[nx][ny] == '0':
					continue
				if graph[nx][ny] == '1':
					queue.append((nx,ny))
# 입력
while True:
  w,h = map(int,sys.stdin.readline().split())
  if w==0 and h==0: # 종료조건
    break
  graph = []
  for _ in range(h):
	  graph.append(list(sys.stdin.readline().split()))
  # 방문확인용
  visited = [[False]*w for _ in range(h)]

  dx = [1,-1,0,0,1,-1,1,-1]
  dy = [0,0,-1,1,-1,-1,1,1]

  result = 0
  for i in range(h):
    for j in range(w):
      if graph[i][j] == '1' and not visited[i][j] :
        bfs(i,j)
        result += 1

  print(result)
