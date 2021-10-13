n,m = map(int,input().split())
castle = []
result_row,result_col = 0,0
for _ in range(n):
	castle.append(input())

for i in range(n):
	if "X" not in castle[i]:
		result_row += 1

for j in range(m):
	if "X" not in [castle[i][j] for i in range(n)]:
		result_col += 1

print(max(result_row,result_col))