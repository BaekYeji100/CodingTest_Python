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
	queue = deque()
	queue.append((x,y))
	result = 0
	while queue:

		x,y = queue.popleft()
		#print(x,y)
		visited[x][y] = True
		for i in range(4):
			nx = x+dx[i]
			ny = y+dy[i]
			# 캠퍼스 크기 벗어날 경우 무시
			if nx<0 or ny<0 or nx>=r or ny>=c:
				#print("1")
				continue
			if not visited[nx][ny]:
				visited[nx][ny] = True
				if graph[nx][ny] == 'X':
					continue
				elif graph[nx][ny] == 'P':
					result += 1		
				queue.append((nx,ny))
					

			# if graph[nx][ny] == 'P' and not visited[nx][ny]:
			# 	#print("3!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!11")
			# 	result += 1
			# 	queue.append((nx,ny))	
			# 	visited[nx][ny] = True
			# if graph[nx][ny] == 'X' or not visited[nx][ny]:
			# 	visited[nx][ny] = True				
			#print("i:",i)
	if result > 0:
		return result
	else:
		return False


for i in range(r):
	for j in range(c):
		if graph[i][j] == 'I':
			result = bfs(i,j)
			if not result:
				print("TT")
			else:
				print(result)
